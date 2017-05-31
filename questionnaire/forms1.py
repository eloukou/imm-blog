from django import forms
from .models import ServiceLandscape

class ServiceContextForm(forms.ModelForm):

    class Meta:
        model = ServiceLandscape
        fields = ('name', 'email', 'cell_phone', 'public_service',           'public_administration', end_user', 'main_administrative_level', 'alternative_administrative_level') 

