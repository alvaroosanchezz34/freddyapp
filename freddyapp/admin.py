from django.contrib import admin
from .models import Animatronic, Party

# Register Animatronic and Party models in Django admin
admin.site.register(Animatronic)
admin.site.register(Party)
