from django import forms
from .models import Contact, Wizard

class ContactForm(forms.ModelForm):
     
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email')

class WizardForm(forms.ModelForm):
     
    class Meta:
        model = Wizard
        fields = ('first_name', 'last_name', 'email', 'avatar_image', 'child', 'minor', 'adult', 'adresse', 'country')
