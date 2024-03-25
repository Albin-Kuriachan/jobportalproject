
from django.urls import path
from employer import views

urlpatterns = [
    path('', views.company_homepage,name='company_homepage'),
    path('company_info', views.company_info,name='company_info'),
    path('company_login/', views.company_login,name='company_login'),
    path('company_register/', views.company_register,name='company_register'),
    path('company_logout/', views.company_logout,name='company_logout'),
    path('company_info/', views.company_info,name='company_info'),
    path('postjob/', views.postjob,name='postjob'),
    path('display_job_post/', views.display_job_post,name='display_job_post'),

    path('edit_job_post/<int:job_id>/', views.edit_job_post, name='edit_job_post'),
    path('delete_job_post/<int:job_id>/', views.delete_job_post, name='delete_job_post'),


    path('appliedCadidate/', views.appliedCadidate, name='appliedCadidate'),
    path('singleJopbAppled/<int:job_id>/', views.singleJopbAppled, name='singleJopbAppled'),







    # path('postjob/<int:id>/',views.postjob,name='postjob'),



]
