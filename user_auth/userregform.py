from django import forms
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from user_auth.models import User
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core import validators
from django import forms
from user_auth.models import User   



class UserRegisterForm(forms.ModelForm):


    class Meta:
        model = User
        fields = '__all__'
#    def clean(self):
#        total_cleaned_data=super().clean()
#        fpwd=total_cleaned_data['password1']
#        spwd=total_cleaned_data['password2']
#        if fpwd != spwd:
#            raise forms.ValidationError('Both passwords must be matched')
