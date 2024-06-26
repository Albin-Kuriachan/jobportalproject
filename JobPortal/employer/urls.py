
from django.urls import path
from employer import views

urlpatterns = [
    path('', views.company_homepage,name='company_homepage'),
    path('company_info/', views.company_info,name='company_info'),
    # path('register_or_login/', views.register_or_login,name='register_or_login'),
    # path('company_login/', views.company_login,name='company_login'),
    # path('company_register/', views.company_register,name='company_register'),
    # path('company_logout/', views.company_logout,name='company_logout'),
    path('company_info/', views.company_info,name='company_info'),
    path('postjob/', views.postjob,name='postjob'),
    path('display_job_post/', views.display_job_post,name='display_job_post'),

    path('edit_job_post/<int:job_id>/', views.edit_job_post, name='edit_job_post'),
    path('delete_job_post/<int:job_id>/', views.delete_job_post, name='delete_job_post'),


    path('appliedCadidate/', views.appliedCadidate, name='appliedCadidate'),
    path('singleJopbAppled/<int:job_id>/', views.singleJopbAppled, name='singleJopbAppled'),

    path('jobpost/', views.jobpost,name='jobpost'),
    path('job_apply_display/', views.job_apply_display,name='job_apply_display'),

    path('employer_job_details/<int:job_id>/', views.employer_job_details, name='employer_job_details'),

    # path('postjob/<int:id>/',views.postjob,name='postjob'),
    path('employer_base/', views.employer_base, name='employer_base'),
    path('update-job-status/<int:job_id>/', views.update_job_status, name='update_job_status'),
    path('apply_status/<int:pk>/<int:apply_id>/', views.apply_status, name='apply_status'),
    # path('apply_candidate_profile/<int:pk>/', views.apply_candidate_profile, name='apply_candidate_profile'),
    path('apply_candidate_profile/<int:pk>/<int:apply_id>/', views.apply_candidate_profile, name='apply_candidate_profile'),


]
