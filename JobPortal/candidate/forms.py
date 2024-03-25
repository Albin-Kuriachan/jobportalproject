from django.utils import timezone
from datetime import timedelta
from django import forms

from .models import *





class CandidateProfileData(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    

    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': timezone.now().strftime('%Y-%m-%d')}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    bio = forms.CharField(max_length=200, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = CandidateProfile
        fields = ['email', 'first_name', 'last_name', 'dob', 'gender', 'bio', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

class QualificationForm(forms.ModelForm):
    year_completed = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'max': timezone.now().strftime('%Y-%m-%d')}),
        help_text='Enter the expiration date in dd mm yyyy format'
    )
    class Meta:
        model = QualificationData
        fields = [ 'qualifiction_type', 'course', 'year_completed']


class ExperienceForm(forms.ModelForm):
    numberofyears = forms.IntegerField(min_value=1)

    class Meta:
        model = Expriance
        fields = ['companyname', 'numberofyears']


# class AppdyjobForm(forms.ModelForm):
#     class Meta:
#         model = ApplyJob
#         fields = ['resume', 'cover_letter']  # Include the necessary fields from the model

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)        