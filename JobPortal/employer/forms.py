from django import forms
from .models import CompanyData,JobData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    

class CompanyDataForm(forms.ModelForm):
    class Meta:
        model = CompanyData
        fields = ['company_name', 'location', 'email', 'phone', 'logo', 'website']
        widgets = {
            'logo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            
        }


class JobDataForm(forms.ModelForm):
    expairy_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
        help_text='Enter the expiration date in dd mm yyyy format'
    )

    class Meta:
        model = JobData
        fields = ['job_title', 'description', 'employment_type', 'location', 'expairy_date']

    def __init__(self, *args, **kwargs):
        super(JobDataForm, self).__init__(*args, **kwargs)
        # Set all fields as required
        for field_name, field in self.fields.items():
            field.required = True




class UserAdminCreationForm(UserCreationForm):
   
    class Meta:
        model = get_user_model()
        fields = ['email']