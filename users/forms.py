from django.forms import fields
import requests
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (UserCreationForm,PasswordChangeForm,PasswordResetForm,AuthenticationForm)

from .models import User

class RegistrationForm(UserCreationForm):
    email_confirm=forms.EmailField(
        label='Email confirmation',
        max_length = 254,
        help_text = 'Enter the same EMail'
    )
    phone_number = forms.IntegerField(
        label='phone number'
    )

    class Meta:
        model = User
        fields=['username','email','phone_number']

class ContactForm(forms.Form):
    subject =  forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)