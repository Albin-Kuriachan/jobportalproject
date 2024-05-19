import json
from datetime import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from account.models import CustomUser
from .models import *
from employer.models import CompanyData, JobData
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from account.send_email import job_apply_candidate_email, job_apply_empoloyer_email
import re

from employer.forms import JobDataForm


# Create your views here.

@login_required
def candidate_homepage(request):
    return render(request, 'candidate_homepage.html')


def index(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    jobdata = ApplyJob.objects.filter(candidate=candidate)

    apply_count = jobdata.count()

    status_counts = jobdata.values('status').annotate(count=models.Count('id'))

    try:
        shortlist_count = status_counts.get(status="Shortlist")['count']
    except ApplyJob.DoesNotExist:
        shortlist_count = 0

    try:
        pending_count = status_counts.get(status="Pending")['count']
    except ApplyJob.DoesNotExist:
        pending_count = 0

    try:
        rejected_count = status_counts.get(status="Rejected")['count']
    except ApplyJob.DoesNotExist:
        rejected_count = 0

    jobdata = jobdata.order_by('-id')[:4]

    context = {
        'jobdata': jobdata,
        'candidate': candidate,
        'apply_count': apply_count,
        'shortlist_count': shortlist_count,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
        'cf': 'index'
    }
    return render(request, 'temp/index.html', context)

@login_required
def add_profile_data(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = CandidateProfileData(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('add_profile_data')  # Redirect to a success URL after saving
    else:
        form = CandidateProfileData(instance=candidate)

    return render(request, 'add_profile_data.html', {'form': form, 'cf': 'add_profile_data'})

@login_required
def add_education(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    print("candadte user", candidate.user.id)
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

    return render(request, 'education\display_education_added.html', {'edu_data': edu_data})

@login_required
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

@login_required
def delete_eduaction_data(request, edu_id):
    QualificationData.objects.filter(id=edu_id).delete()
    return redirect('display_education_added')

@login_required
def create_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_experience')  # Redirect to a success page
    else:
        form = ExperienceForm()
    return render(request, 'experience\experience_form.html', {'form': form})

@login_required
def display_experience(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    exprience = Expriance.objects.filter(user=candidate)

    return render(request, 'experience\display_experience.html', {'exp_data': exprience})

@login_required
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

@login_required
def delete_experience(request, exp_id):
    Expriance.objects.filter(id=exp_id).delete()
    return redirect('display_experience')


@login_required
def display_job(request):
    jobdata = JobData.objects.all()
    form = JobFilterForm()

    if request.method == 'POST':
        form = JobFilterForm(request.POST)

        if form.is_valid():
            job_title_pattern = form.cleaned_data['job_title']
            print(job_title_pattern)
            location_pattern = form.cleaned_data['location']
            category_pattern = form.cleaned_data['category']
            print(category_pattern)
            emp_type_pattern = form.cleaned_data['employment_type']
            experience_levels_selected = form.cleaned_data['experience_level']
            print(experience_levels_selected)
            posted_date_selected = form.cleaned_data.get('posted_date')
            print(posted_date_selected)

            salary_from = request.POST.get('salary-from')
            print(salary_from)
            salary_to = request.POST.get('salary-to')
            print(salary_to)


            if job_title_pattern:
                jobdata = jobdata.filter(job_title__iregex=job_title_pattern)

            if location_pattern:
                jobdata = jobdata.filter(location__iregex=location_pattern)

            if category_pattern:
                jobdata = jobdata.filter(category__iregex=category_pattern)

            if emp_type_pattern:
                jobdata = jobdata.filter(employment_type__iregex=emp_type_pattern)

            if experience_levels_selected:
                if 'Any' in experience_levels_selected:
                    jobdata = jobdata.filter(Q(experience='Any') | Q(experience__in=experience_levels_selected))
                else:
                    experience_levels_selected.append('Any')
                    jobdata = jobdata.filter(experience__in=experience_levels_selected)

            if posted_date_selected == '24_hours':
                jobdata = jobdata.filter(posted_date__gte=timezone.now() - timedelta(hours=24))
            elif posted_date_selected == '7_days':
                jobdata = jobdata.filter(posted_date__gte=timezone.now() - timedelta(days=7))
            elif posted_date_selected == '30_days':
                jobdata = jobdata.filter(posted_date__gte=timezone.now() - timedelta(days=30))
            elif posted_date_selected == 'all':
                pass

            if salary_from is not None and salary_to is not None:
                jobdata = jobdata.filter(salary__range=(salary_from, salary_to))

                # Sort by salary
            # if salary_sort == 'ascending':
            #     jobdata = jobdata.order_by('salary')
            # elif salary_sort == 'descending':
            #     jobdata = jobdata.order_by('-salary')

    context = {
        'jobdata': jobdata,
        'form': form,
    }
    return render(request, "jobdata/display_job.html", context)


@login_required
def job_details(request, job_id):
    job_details = JobData.objects.filter(id=job_id)
    candidate = CandidateProfile.objects.get(user=request.user)
    applyOrNot = ApplyJob.objects.filter(candidate=candidate, job_id=job_id).exists()
    company = CompanyData.objects.filter(id=job_id)
    print('company data', company)
    context = {
        'job_details': job_details,
        'applyOrNot': applyOrNot,
        'company': company
    }
    return render(request, "jobdata\jobdetails.html", context)




@login_required
def job_filter(request):
    job_listings = JobData.objects.all()

    if request.method == 'GET':
        job_title_pattern = request.GET.get('job_title')
        location_pattern = request.GET.get('location')

        if job_title_pattern:
            job_listings = [job for job in job_listings if re.search(job_title_pattern, job.job_title, re.IGNORECASE)]

        if location_pattern:
            job_listings = [job for job in job_listings if re.search(location_pattern, job.location, re.IGNORECASE)]

    return render(request, "jobdata/job_filter.html", {'job_listings': job_listings})

@login_required
def apply_job(request, job_id):
    candidate = CandidateProfile.objects.get(user=request.user)

    qualifications = QualificationData.objects.filter(user=candidate)
    experiences = Expriance.objects.filter(user=candidate)

    job = get_object_or_404(JobData, pk=job_id)
    email = candidate.email
    job_title = job.job_title
    employer_email = job.company.email
    subject = 'Job Application'
    message = f' Yor appliction for  {job_title} submitted successfully'

    # Send email to candidate and employer
    job_apply_candidate_email(email, subject, message)
    job_apply_empoloyer_email(employer_email, job_title)

    apply_job_instance = ApplyJob.objects.create(candidate=candidate, job=job)

    apply_job_instance.qualification.set(qualifications)
    apply_job_instance.experiences.set(experiences)

    return redirect('job_details', job_id=job_id)

@login_required
def companyDisplay(request):
    company = CompanyData.objects.all()
    return render(request, 'company/companydisplay.html', {"company": company})

@login_required
def profileDetails(request):
    return render(request, 'profile\profofiledisplay.html')

@login_required
def profileDataAdd(request):
    candidate = CandidateProfile.objects.get(user=request.user)

    if request.method == 'POST':

        candidate.first_name = request.POST.get('first_name')
        candidate.last_name = request.POST.get('last_name')
        candidate.phone = request.POST.get('phone')
        candidate.email = request.POST.get('email')
        candidate.gender = request.POST.get('gender')
        candidate.bio = request.POST.get('bio')
        dob = request.POST.get('dob')

        dob = dob.strip().replace('“', '').replace('”', '')
        dob = datetime.strptime(dob, '%B %d, %Y').date()
        candidate.dob = dob
        new_image = request.FILES.get('image')

        if new_image:
            candidate.image = new_image

        candidate.save()
    context = {'candidate': candidate, 'cf': 'profileDataAdd'}

    return render(request, 'profile\profileDataAdd.html', context)

@login_required
def myapplyed(request):
    candidate = CandidateProfile.objects.get(user=request.user)
    applydata = ApplyJob.objects.filter(candidate=candidate)

    context = {'applydata': applydata, 'candidate': candidate, 'cf': 'myapplyed'}

    return render(request, 'jobdata\myapplyed.html', context)


def base(request):
    return render(request, 'temp/base.html')



