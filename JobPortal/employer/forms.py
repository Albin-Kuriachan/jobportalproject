from django import forms
from .models import CompanyData,JobData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(forms.Form):
#     email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Password'}))
#     # email = forms.EmailField()
#     # password = forms.CharField(widget=forms.PasswordInput())
#
#     # widgets = {
#     #     'email':forms.TextInput(attrs={'class':"form-control"}),
#
#     # }
#
#
#
# # class RegisterForm(UserCreationForm):
# #     email = forms.EmailField()
#
# #     class Meta:
# #         model = User
# #         fields = [ 'email', 'password1', 'password2']
#
# class RegisterForm(UserCreationForm):
#     # email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = [ 'email', 'password1', 'password2']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'off','id':'password'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         }

class CompanyDataForm(forms.ModelForm):
    class Meta:
        model = CompanyData
        fields = ['company_name', 'location', 'email', 'phone', 'logo', 'website','description']
        widgets = {
            'logo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            
        }


class JobDataForm(forms.ModelForm):
    # expairy_date = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
    #     help_text='Enter the expiration date in dd mm yyyy format'
    # )
    salary = forms.DecimalField(
        min_value=0,
        widget=forms.NumberInput(attrs={'min': 0})
    )

    class Meta:
        model = JobData
        fields = ['job_title', 'description', 'employment_type',
                  'location', 'gender',
                  'post_no','experience','salary','category']

    def __init__(self, *args, **kwargs):
        super(JobDataForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = True


class ApplyStatusForm(forms.ModelForm):
    class Meta:
        model = JobData
        fields = ['status']



class UserAdminCreationForm(UserCreationForm):
   
    class Meta:
        model = get_user_model()
        fields = ['email']