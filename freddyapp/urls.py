from django.urls import path
from . import views

# URL patterns for freddyapp
urlpatterns = [
    # Animatronic routes
    path('list/', views.animatronic_list, name='animatronic_list'),
    path('new/', views.animatronic_new, name='animatronic_new'),
    path('<int:pk>/view/', views.animatronic_view, name='animatronic_view'),
    path('<int:pk>/edit/', views.AnimatronicUpdate.as_view(), name='animatronic_edit'),
    path('<int:pk>/delete/', views.AnimatronicDelete.as_view(), name='animatronic_delete'),
    
    # Authentication routes
    path('newuser/', views.register_user, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    # Theme routes
    path('theme/', views.set_theme_dark, name='set_theme'),
    path('clearcookies/', views.clear_cookies, name='clear_cookies'),
]
