from django import forms
from .models import ContactDetails, ServiceDescription, ServiceOwner, EndUser, AdministrativeLevel

#class ServiceContextForm(forms.ModelForm):

 #   class Meta:
  #      model = ServiceLandscape
   #     fields = ('name', 'email', 'cell_phone', 'public_service',              'public_administration', 'end_user', 'main_administrative_level', 'alternative_administrative_level') 

class ContactDetailsForm(forms.ModelForm):

    class Meta:
        model = ContactDetails
        fields = ('name', 'email', 'cell_phone') 

class ServiceDescriptionForm(forms.ModelForm):

    class Meta:
        model = ServiceDescription
        fields = ('service_description',)
 
class ServiceOwnerForm(forms.ModelForm):

    class Meta:
        model = ServiceOwner
        fields = ('public_administration',) 

class EndUserForm(forms.ModelForm):

    class Meta:
        model = EndUser
        fields = ('end_user',) 

class AdministrativeLevelForm(forms.ModelForm):

    class Meta:
        model = AdministrativeLevel
        fields = ('main_administrative_level', 'alternative_administrative_level') 

