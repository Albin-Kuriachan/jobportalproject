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






class JobFilterForm(forms.Form):
    EMPLOYMENT = [
        ('', 'Employment Type'),
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Temporary', 'Temporary'),
        ('Remote', 'Remote'),

        ('Other', 'Other')
    ]
    CATEGORY_CHOICES = [
        ('', 'Category'),
        ('Accounting / Finance', 'Accounting / Finance'),
        ('Automotive Jobs', 'Automotive Jobs'),
        ('Customer', 'Customer'),
        ('Design', 'Design'),
        ('Development', 'Development'),
        ('Health and Care', 'Health and Care'),
        ('Human Resource', 'Human Resource'),
        ('Marketing', 'Marketing'),
        ('Project Management', 'Project Management'),
    ]

    EXPERIENCE_LEVEL_CHOICES =[
        ('Fresher', 'Fresher'),
        ('Less than 1 year', 'Less than 1 year'),
        ('1-3 years', '1-3 years'),
        ('3-5 years', '3-5 years'),
        ('5-10 years', '5-10 years'),
        ('More than 10 years', 'More than 10 years'),
        ('Any', 'Any'),
    ]
    POSTED_DATE_CHOICES = [
        ('24_hours', '24 hours'),
        ('7_days', ' 7 days'),
        ('30_days', ' 30 days'),
        ('all', 'Show all')
    ]
    job_title = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Job Title'})
    )

    location = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Location'})
    )

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Category'})
    )
    employment_type = forms.ChoiceField(
        choices=EMPLOYMENT,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Email'})
    )

    experience_level = forms.MultipleChoiceField(
        choices=EXPERIENCE_LEVEL_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-list'})
    )

    posted_date = forms.ChoiceField(
        choices=POSTED_DATE_CHOICES,
        required=False,
        widget=forms.RadioSelect
    )

    # experience = forms.IntegerField()
    # salary = forms.DecimalField(max_digits=10, decimal_places=2)
    # category = forms.CharField(max_length=100)
    #     email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Email'}))
    #
    # employment_type = forms.ChoiceField(choices=EMPLOYMENT, required=False(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Email'})))
    # location = forms.CharField(max_length=100, required=False)
    # job_title = forms.CharField(max_length=100, required=False)
    # category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
