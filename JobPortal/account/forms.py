from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField \
        (widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Email'}))
    password = forms.CharField \
        (widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Password'}))
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())

    # widgets = {
    #     'email':forms.TextInput(attrs={'class':"form-control"}),

    # }



# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = [ 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}),
            'password1': forms.PasswordInput
                (attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'off' ,'id' :'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
