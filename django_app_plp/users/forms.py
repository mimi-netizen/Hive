from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from localflavor.us.forms import USZipCodeField

from .models import Location, Profile



class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')





class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}