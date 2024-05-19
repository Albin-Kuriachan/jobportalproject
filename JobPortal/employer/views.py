from django.db.models import Count
from django.shortcuts import redirect, render, get_object_or_404
from candidate.views import index
from candidate.models import ApplyJob
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from account.models import CustomUser
from .models import CompanyData, JobData
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from account.views import *
from account.send_email import job_apply_candidate_email, job_apply_empoloyer_email

from candidate.models import CandidateProfile


@login_required
def company_homepage(request):
    company_data = CompanyData.objects.get(user=request.user)
    recent_apply = ApplyJob.objects.filter(job__company=company_data)
    job_post_count = JobData.objects.filter(company=company_data).count()
    apply_count = recent_apply.count()

    status_counts = recent_apply.values('status').annotate(count=Count('id'))
    # shortlist_count = status_counts.get(status="Shortlist")['count']
    # pending_count = status_counts.get(status="Pending")['count']
    # rejected_count = status_counts.get(status="Rejected")['count']
    # status_counts = jobdata.values('status').annotate(count=Count('id'))

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

    context = {
        'company_data': company_data,
        'recent_apply': recent_apply,
        'job_post_count': job_post_count,
        'apply_count': apply_count,
        'shortlist_count': shortlist_count,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
        'cf': 'company_home'
    }
    return render(request, 'company_homepage.html', context)


@login_required
def company_info(request):
    company_data = CompanyData.objects.get(user=request.user)

    if request.method == 'POST':
        form = CompanyDataForm(request.POST, request.FILES, instance=company_data)
        if form.is_valid():
            profile = form.save(commit=False)
            new_image = request.FILES.get('image')

            print(new_image)

            if new_image:
                profile.logo = new_image
            profile.save()

            # if new_image:
            #     job_data.image = new_image
            #
            # return redirect(company_info)
    else:
        form = CompanyDataForm(instance=company_data)
    return render(request, 'company_profile.html', {'form': form, "cf": "company_info", 'company_data': company_data})


# def company_register(request):
#     # form = UserAdminCreationForm()
#     # if request.method == 'POST':
#     #     form = UserAdminCreationForm(request.POST)
#     #     if form.is_valid():
#             #   CustomUser.objects.create_user( email=email, password=password)
#     #         form.save()
#     #         return redirect(company_login)
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirmpassword = request.POST.get('confirmpassword')
#         usertype = request.POST.get('usertype')
#         print("Please enter your",usertype)
#
#         if password == confirmpassword:
#                 user = CustomUser.objects.create_user( email=email, password=password,user_type=usertype)
#                 user.save();
#                 messages.success(request, 'Registration successful')
#
#                 return redirect(company_login)
#         else:
#             messages.success(request, 'Password not match')
#             return redirect(company_login)
#     return redirect(company_login)
#
#                     # messages.success(request, 'Password not match')
#     # return render(request, 'company_register.html', {'form': form})
#
# # def company_register(request):
# #     if request.method == 'POST':
# #         form = UserAdminCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             email = form.cleaned_data.get('email')
# #             password = form.cleaned_data.get('password1')
# #             user = authenticate(email=email, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 return redirect('company_login')  # assuming 'company_login' is the name of your login URL pattern
# #             else:
# #                 # Handle the case where authentication fails
# #                 pass
# #     else:
# #         form = UserAdminCreationForm()
#
# #     return render(request, 'company_register.html', {'form': form})
#
#
# def company_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             print(user)
#
#             if user is not None:
#                 if user.user_type == 'employer':
#                     login(request, user)
#                     return redirect('company_homepage')  # Redirect to company homepage
#                 else:
#                     login(request, user)
#                     return redirect('index')  # Redirect to index page
#             else:
#                 form.add_error(None, 'Invalid username or password.')
#     else:
#         form = LoginForm()
#     return render(request, 'company_login.html', {'form': form})
#
# # if user is not None :
# #                 login(request, user)
# #                 return redirect(company_homepage)
# #             else:
# #                 form.add_error(None, 'Invalid username or password.')
#
# # def company_login(request):
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         password = request.POST.get('password')
#
# #         print(email,password)
#
# #         user = authenticate(request, username=email, password=password)
# #         if user is not None:
# #             login(request, user)
# #             return redirect(company_homepage)  # Assuming company_homepage is a URL name or path
# #         else:
# #             # Handle invalid login credentials
# #             # You might want to add an error message here
# #             pass
#
# #     return render(request, 'company_login.html')
#
#
# @login_required
# def company_logout(request):
#     auth.logout(request)
#     return redirect(company_login)


@login_required
# def postjob(request):
#     # user_id = CompanyData.objects.get(id=id)
#     company_data= CompanyData.objects.get(user=request.user)
#
#     if request.method == 'POST':
#         form = JobDataForm(request.POST, request.FILES)
#         print("139")
#         if form.is_valid():
#             print('141')
#             job_data = form.save(commit=False)
#             job_data.company = company_data
#             job_data.expiry_date=request.POST.get('expiry_date')
#             print(request.POST.get('expiry_date'))
#             job_data.save()
#             return redirect('display_job_post')
#     else:
#         form = JobDataForm()
#
#     return render(request,'post_job.html',{'form': form})
#

def postjob(request):
    # company_data = CompanyData.objects.get(user=request.user)
    company_data = CompanyData.objects.get(user=request.user)

    if request.method == 'POST':
        form = JobDataForm(request.POST, request.FILES)
        if form.is_valid():
            job_data = form.save(commit=False)
            job_data.company = company_data
            image_file = request.FILES.get('image')
            job_data.image = image_file
            expiry_date_str = request.POST.get('expairy_date')
            print(expiry_date_str)
            expiry_date_str = expiry_date_str.strip().replace('“', '').replace('”', '')
            expiry_date = datetime.strptime(expiry_date_str, '%B %d, %Y').date()

            print(expiry_date)

            job_data.expiry_date = expiry_date
            job_data.save()
            return redirect('display_job_post')
    else:
        form = JobDataForm()
    context = {
        'company_data': company_data,
        'form': form,
        'cf': 'postjob'
    }

    return render(request, 'post_job.html', context)


def display_job_post(request):
    company_data = CompanyData.objects.get(user=request.user)
    job_data = JobData.objects.filter(company=company_data)

    apply_counts = {}
    for job in job_data:
        apply_count = ApplyJob.objects.filter(job__id=job.id).count()
        apply_counts[job.id] = apply_count

    return render(request, 'display_job_post.html', {'job_data': job_data, 'apply_counts': apply_counts})


@login_required
def edit_job_post(request, job_id):
    job_instance = get_object_or_404(JobData, id=job_id)

    print(job_instance.expiry_date)

    if request.method == 'POST':
        form = JobDataForm(request.POST, request.FILES, instance=job_instance)
        if form.is_valid():
            job_data = form.save(commit=False)
            expiry_date_str = request.POST.get('expairy_date')
            print(expiry_date_str)
            expiry_date_str = expiry_date_str.strip().replace('“', '').replace('”', '')
            expiry_date = datetime.strptime(expiry_date_str, '%B %d, %Y').date()

            print(expiry_date)

            job_data.expiry_date = expiry_date

            new_image = request.FILES.get('image')

            if new_image:
                job_data.image = new_image
            job_data.save()
            return redirect('employer_job_details', job_id=job_id)
    else:
        form = JobDataForm(instance=job_instance)

    return render(request, 'edit_job_post.html', {'form': form, 'job_instance': job_instance})


@login_required
def delete_job_post(request, job_id):
    JobData.objects.filter(id=job_id).delete()
    return redirect('job_apply_display')


@login_required
def appliedCadidate(request):
    company_data = CompanyData.objects.get(user=request.user)
    appleddata = ApplyJob.objects.filter(job__company=company_data)
    job_data = JobData.objects.filter(company=company_data)

    return render(request, 'appliedCadidate.html', {'appleddata': appleddata, 'job_data': job_data})


def apply_status(request, pk, apply_id):
    print(apply_id)

    print(pk)

    job = ApplyJob.objects.get(id=apply_id)
    # jk = ApplyJob.objects.all()
    # for j in jk:
    #     print(j.id)



    if pk == 1:
        job.status = 'Pending'
    elif pk == 2:
        job.status = 'Shortlist'
    elif pk == 3:
        job.status = 'Approved'
    elif pk == 4:
        job.status = 'Rejected'
    job.save()

    subject = 'Job Application update'
    message = f' Yor appliction for  {job.job.job_title} at {job.job.company.company_name} is {job.status}'
    email = job.candidate.user.email
    # Send email to candidate and employer
    job_apply_candidate_email(email, subject, message)

    return redirect(appliedCadidate)


@login_required
def singleJopbAppled(request, job_id):
    company_data = CompanyData.objects.get(user=request.user)
    appleddata = ApplyJob.objects.filter(job__company=company_data, job_id=job_id)
    return render(request, 'singleJopbAppled.html', {'appleddata': appleddata})


def jobpost(request):
    company_id = CompanyData.objects.get(user=request.user)
    job_data = JobData.objects.filter(company=company_id)
    applyed_number = ApplyJob.objects.all()

    return render(request, 'jobpost.html', {'job_data': job_data, 'applyed_number': applyed_number})


def job_apply_display(request):
    company_data = CompanyData.objects.get(user=request.user)
    job_data = JobData.objects.filter(company=company_data)

    apply_counts = {}
    for job in job_data:
        apply_count = ApplyJob.objects.filter(job__id=job.id).count()
        apply_counts[job.id] = apply_count
    context = {'job_data': job_data,
               'apply_counts': apply_counts,
               'cf': 'job_apply_display',
               'company_data': company_data
               }

    return render(request, 'job_display.html', context)


def employer_job_details(request, job_id):
    job_details = JobData.objects.filter(id=job_id)
    # candidate = CandidateProfile.objects.get(user=request.user)
    # applyOrNot = ApplyJob.objects.filter(candidate=candidate, job_id=job_id).exists()
    company = CompanyData.objects.filter(id=job_id)
    print('company data', company)
    context = {
        'job_details': job_details,
        # 'applyOrNot': applyOrNot,
        'company': company
    }

    return render(request, 'employer_job_details.html', context)


def employer_base(request):
    return render(request, 'employer_base.html')


def update_job_status(request, job_id):
    job = get_object_or_404(JobData, id=job_id)
    job.status = not job.status
    job.save()
    return redirect('job_apply_display')


# def apply_candidate_profile(request,pk):
#     candidate = CandidateProfile.objects.get(id=pk)
#     return render(request,'apply_candidate_profile.html',{'candidate':candidate})

def apply_candidate_profile(request,pk,apply_id):
    candidate = CandidateProfile.objects.get(id=pk)
    return render(request,'apply_candidate_profile.html',{'candidate':candidate,'apply_id':apply_id})

