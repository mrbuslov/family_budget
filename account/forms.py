import imp
from django.forms import ModelForm
from account.models import Account
from django import forms
from django.utils.translation import gettext_lazy as _

class ProfileEditForm(ModelForm):
    class Meta:
        model = Account
        fields=('first_name', 'last_name')    

        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last name'}),
        } 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

