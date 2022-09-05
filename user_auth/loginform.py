from user_auth.models import User
from django import forms
class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=63)
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password1')
