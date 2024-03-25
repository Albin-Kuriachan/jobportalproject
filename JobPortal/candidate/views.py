import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from account.models import  CustomUser
from .models import *
from employer.models import CompanyData, JobData
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required

def candidate_homepage(request):

    return render(request, 'candidate_homepage.html')


def index(request):
    jobdata=JobData.objects.all()
    context={
        'jobdata': jobdata
    }
    return render(request, 'temp\index.html',context)


def add_profile_data(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CandidateProfileData(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('add_profile_data')  # Redirect to a success URL after saving
    else:
        form = CandidateProfileData(instance=candidate)
    
    return render(request, 'add_profile_data.html', {'form': form})






def add_education(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    print("candadte user",candidate.user.id )
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = candidate        
            education.save()
            return redirect('add_education')  
    else:
        form = QualificationForm(instance=candidate)
   
    return render(request, "education\education.html", {'form': form})  


def display_education_added(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    edu_data = QualificationData.objects.filter(user=candidate)

    return render(request,'education\display_education_added.html',{'edu_data': edu_data})


def edit_eduaction_data(request, edu_id):
    education_instance = get_object_or_404(QualificationData, id=edu_id)
    
    if request.method == 'POST':
        form = QualificationForm(request.POST, instance=education_instance)
        if form.is_valid():
            form.save()
            return redirect('display_education_added')  
    else:
        form = QualificationForm(instance=education_instance)

    return render(request, 'education\edit_eduaction_data.html', {'form': form})


def delete_eduaction_data(request, edu_id):
    QualificationData.objects.filter(id=edu_id).delete()
    return redirect('display_education_added')  




def create_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_experience')  # Redirect to a success page
    else:
        form = ExperienceForm()
    return render(request, 'experience\experience_form.html', {'form': form})


def display_experience(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    exprience = Expriance.objects.filter(user=candidate)

    return render(request,'experience\display_experience.html',{'exp_data': exprience})


def edit_experience(request, exp_id):
    exprience_instance = get_object_or_404(QualificationData, id=exp_id)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exprience_instance)
        if form.is_valid():
            form.save()
            return redirect('experience\display_education_added')  
    else:
        form = ExperienceForm(instance=exprience_instance)

    return render(request, 'experience\edit_experience.html', {'form': form})


def delete_experience(request, exp_id):
    Expriance.objects.filter(id=exp_id).delete()
    return redirect('display_experience')  



def display_job(request):
    jobdata=JobData.objects.all()
    context={
        'jobdata': jobdata
    }
    return render(request ,"jobdata\display_job.html",context)



def job_details(request,job_id):
    job_details=JobData.objects.filter(id=job_id)
    candidate = CandidateProfile.objects.get(user=request.user)
    applyOrNot = ApplyJob.objects.filter(candidate=candidate, job_id=job_id).exists()
    company = CompanyData.objects.filter(id=job_id)
    print( 'company data' ,company)
    context={
        'job_details':job_details,
        'applyOrNot':applyOrNot,
        'company':company
    }
    return render(request,"jobdata\jobdetails.html",context)




def apply_job(request, job_id):
    candidate = CandidateProfile.objects.get(user=request.user)
    
    qualifications = QualificationData.objects.filter(user=candidate)
    experiences = Expriance.objects.filter(user=candidate)
    
    job = get_object_or_404(JobData, pk=job_id)
    
    apply_job_instance = ApplyJob.objects.create(candidate=candidate, job=job)
    
    apply_job_instance.qualification.set(qualifications)
    apply_job_instance.experiences.set(experiences)
    
    return redirect('display_job')


def companyDisplay(request):
    company=CompanyData.objects.all()
    return render(request, 'company/companydisplay.html',{"company":company})
