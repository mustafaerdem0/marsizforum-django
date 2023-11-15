from django.forms import ModelForm
from django import forms
from .models import MyUser

class ProfileSettingsForm(forms.ModelForm):
    birthday = forms.DateField( 
        widget=forms.DateInput
(
       
        ))
    class Meta:
        model = MyUser
        fields = ['avatar','banner','birthday','location','website','about']
class ProfileAuthSettings(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email']