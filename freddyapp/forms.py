from django import forms
from django.core.exceptions import ValidationError
from .models import Animatronic, Party


class AnimatronicForm(forms.ModelForm):
    """Formulario para crear y editar animatrónicos con validaciones específicas"""
    
    # Custom field for animal choice
    animal = forms.ChoiceField(
        choices=Animatronic.ANIMAL_CHOICES,
        label="Animal type",
        required=True
    )
    
    # Custom field for build_date to show calendar widget
    build_date = forms.DateField(
        label="Build date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        error_messages={
            'required': 'The build date is required'
        }
    )
    
    class Meta:
        model = Animatronic
        fields = ['name', 'animal', 'build_date', 'decommissioned', 'parties']
        labels = {
            'name': 'Name',
            'animal': 'Animal type',
            'build_date': 'Build date',
            'decommissioned': 'Decommissioned',
            'parties': 'Parties',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'animal': forms.Select(attrs={'class': 'form-control'}),
            'build_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'decommissioned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'parties': forms.CheckboxSelectMultiple(),
        }
        error_messages = {
            'name': {
                'max_length': 'The name of the animatronic must not be more than 50 characters long',
                'required': 'The name of the animatronic is required',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set required for animal field
        self.fields['animal'].required = True
        # Set required for decommissioned field
        self.fields['decommissioned'].required = True
        # Set not required for parties field
        self.fields['parties'].required = False

    def clean_name(self):
        """Validar nombre del animatrónico"""
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('The name of the animatronic is required')
        if len(name) > 50:
            raise ValidationError('The name of the animatronic must not be more than 50 characters long')
        return name

    def clean_animal(self):
        """Validar animal type"""
        animal = self.cleaned_data.get('animal')
        if not animal:
            raise ValidationError('Animal type is required')
        if len(animal) > 2:
            raise ValidationError('Animal type must not be more than 2 characters long')
        return animal

    def clean_build_date(self):
        """Validar fecha de construcción"""
        build_date = self.cleaned_data.get('build_date')
        if not build_date:
            raise ValidationError('The build date is required')
        return build_date

    def clean_decommissioned(self):
        """Validar field decommissioned"""
        decommissioned = self.cleaned_data.get('decommissioned')
        # decommissioned puede ser True o False, ambos son válidos
        return decommissioned
