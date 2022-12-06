from django import forms

from .models import User


class RegistrationForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email Address', 'name': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password', 'name': 'password'})
        }