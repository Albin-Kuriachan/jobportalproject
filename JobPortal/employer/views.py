from django.shortcuts import redirect, render,get_object_or_404
from candidate.models import ApplyJob
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from account.models import CustomUser
from .models import CompanyData,JobData
from django.contrib.auth.decorators import login_required


@login_required
def company_homepage(request):
    return render(request, 'company_homepage.html')

@login_required
def company_info(request):
    company = CompanyData.objects.get(user=request.user)
    if request.method == 'POST':
        form = CompanyDataForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect(company_homepage)  
    else:
        form = CompanyDataForm(instance=company)
    return render(request, 'company_create.html', {'form': form})


def company_register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(company_login)
    return render(request, 'company_register.html', {'form': form})


def company_login(request):
     if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None :
                login(request, user)
                return redirect(company_homepage)
            else:
                form.add_error(None, 'Invalid username or password.')
     else:
        form = LoginForm()
     return render(request, 'company_login.html', {'form': form})



@login_required
def company_logout(request):
    auth.logout(request)
    return redirect(company_login) 


@login_required
def postjob(request):
    # user_id = CompanyData.objects.get(id=id)
    company_id = CompanyData.objects.get(user=request.user)

    if request.method == 'POST':
        form = JobDataForm(request.POST)
        if form.is_valid():
            job_data = form.save(commit=False)  
            job_data.company = company_id  
            job_data.save()  
            return redirect('postjob')  
    else:
        form = JobDataForm()

    return render(request,'post_job.html',{'form': form})


def display_job_post(request):
    company_id = CompanyData.objects.get(user=request.user)
    job_data = JobData.objects.filter(company=company_id)

    return render(request,'display_job_post.html',{'job_data': job_data})   


@login_required
def edit_job_post(request, job_id):
    job_instance = get_object_or_404(JobData, id=job_id)
    
    if request.method == 'POST':
        form = JobDataForm(request.POST, instance=job_instance)
        if form.is_valid():
            form.save()
            return redirect('display_job_post')  
    else:
        form = JobDataForm(instance=job_instance)

    return render(request, 'edit_job_post.html', {'form': form})

@login_required
def delete_job_post(request, job_id):
    JobData.objects.filter(id=job_id).delete()
    return redirect('display_job_post')  

@login_required
def appliedCadidate(request):
    company_data = CompanyData.objects.get(user=request.user)
    appleddata = ApplyJob.objects.filter(job__company=company_data)
    return render(request, 'appliedCadidate.html',{'appleddata':appleddata})

@login_required
def singleJopbAppled(request,job_id):
    company_data = CompanyData.objects.get(user=request.user)
    appleddata = ApplyJob.objects.filter(job__company=company_data,job_id=job_id)
    return render(request, 'singleJopbAppled.html',{'appleddata':appleddata})





