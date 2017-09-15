from django.contrib import admin
from .models import Gato


@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ('name', 'patas',)
