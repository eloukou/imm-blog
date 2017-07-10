from django import forms
from .models import ContactDetails, ServiceDescription, ServiceOwner, EndUser, AdministrativeLevel, DeliveryChannel, AccessibilityOption, Accessibility, ServiceConsumption, ReuseAndSharing
from multiselectfield import MultiSelectFormField

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
        fields = ('administrative_level',) 

class DeliveryChannelForm(forms.ModelForm):

    class Meta:
        model = DeliveryChannel
        fields = ('traditional_channel', 'digital_channel',)

class AccessibilityForm(forms.ModelForm):

    class Meta:
        model = Accessibility
        fields = ('question', 'accessibility', 'maturityscoring',)

class ServiceConsumptionForm(forms.ModelForm):

    class Meta:
        model = ServiceConsumption
        fields = ('service_consumption',)


class ReuseAndSharingForm(forms.ModelForm):
    
    class Meta:
        model = ReuseAndSharing
        fields = ('reuse_and_sharing',) 


