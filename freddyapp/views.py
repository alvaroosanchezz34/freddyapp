from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from .models import Animatronic, Party
from .forms import AnimatronicForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# ============ ANIMATRONIC VIEWS ============

def animatronic_list(request):
    """Vista que muestra la lista de todos los animatrónicos"""
    animatronics = Animatronic.objects.all()
    context = {
        'animatronics': animatronics,
    }
    return render(request, 'freddyapp/animatronic_list.html', context)


@login_required
@permission_required('freddyapp.add_animatronic', raise_exception=True)
def animatronic_new(request):
    """Vista para crear un nuevo animatrónico"""
    if request.method == 'POST':
        form = AnimatronicForm(request.POST)
        if form.is_valid():
            animatronic = form.save()
            return redirect('animatronic_view', pk=animatronic.pk)
    else:
        form = AnimatronicForm()
    
    context = {
        'form': form,
        'title': 'Create Animatronic'
    }
    return render(request, 'freddyapp/animatronic_new.html', context)


@login_required
def animatronic_view(request, pk):
    """Vista que muestra los detalles de un animatrónico"""
    # Check if user has permission to view
    if not request.user.has_perm('freddyapp.view_animatronic') and not request.user.has_perm('freddyapp.change_animatronic'):
        redirect_to_list = redirect('animatronic_list')
        return redirect_to_list
    
    animatronic = get_object_or_404(Animatronic, pk=pk)
    context = {
        'animatronic': animatronic,
    }
    return render(request, 'freddyapp/animatronic_view.html', context)


class AnimatronicUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Vista para editar un animatrónico (clase)"""
    model = Animatronic
    form_class = AnimatronicForm
    template_name = 'freddyapp/animatronic_edit.html'
    permission_required = 'freddyapp.change_animatronic'
    
    def get_success_url(self):
        return reverse_lazy('animatronic_view', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Animatronic'
        return context


class AnimatronicDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Vista para eliminar un animatrónico (clase)"""
    model = Animatronic
    template_name = 'freddyapp/animatronic_confirm_delete.html'
    success_url = reverse_lazy('animatronic_list')
    permission_required = 'freddyapp.delete_animatronic'


# ============ AUTHENTICATION VIEWS ============

def register_user(request):
    """Vista para registrar un nuevo usuario"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add user to Client group by default
            client_group = Group.objects.get(name='Client')
            user.groups.add(client_group)
            login(request, user)
            return redirect('animatronic_list')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'freddyapp/register.html', context)


class LoginView(View):
    """Vista de login (clase)"""
    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'freddyapp/login.html', context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('animatronic_list')
        else:
            context = {'form': form}
            return render(request, 'freddyapp/login.html', context)


class LogoutView(View):
    """Vista de logout (clase)"""
    def get(self, request):
        logout(request)
        return redirect('animatronic_list')


# ============ COOKIE/THEME VIEWS ============

def set_theme_dark(request):
    """Vista que establece el tema oscuro mediante una cookie"""
    response = redirect('animatronic_list')
    response.set_cookie('theme', 'dark', max_age=31536000)  # 1 year
    return response


def clear_cookies(request):
    """Vista que borra la cookie de tema"""
    response = redirect('animatronic_list')
    response.delete_cookie('theme')
    return response
