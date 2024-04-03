
from django.urls import path
from candidate import views

urlpatterns = [
    path('', views.candidate_homepage,name='candidate_homepage'),
    path('index/', views.index,name='index'),
    path('add_profile_data/', views.add_profile_data,name='add_profile_data'),
    path('add_education/', views.add_education,name='add_education'),
    path('display_education_added/', views.display_education_added,name='display_education_added'),
    path('edit_eduaction_data/<int:edu_id>/', views.edit_eduaction_data,name='edit_eduaction_data'),
    path('delete_eduaction_data/<int:edu_id>', views.delete_eduaction_data,name='delete_eduaction_data'),
    path('create_experience/', views.create_experience,name='create_experience'),
    path('display_experience/', views.display_experience, name='display_experience'),
    path('edit_experience/<int:exp_id>/', views.edit_experience, name='edit_experience'),
    path('delete_experience/<int:exp_id>/', views.delete_experience, name='delete_experience'),
    path('display_job/', views.display_job,name='display_job'),
    path('job_details/<int:job_id>/', views.job_details,name='job_details'),
    path('apply_job/<int:job_id>/', views.apply_job,name='apply_job'),
    path('companyDisplay/', views.companyDisplay,name='companyDisplay'),

    path('profileDetails/', views.profileDetails,name='profileDetails'),
    path('profileDataAdd/', views.profileDataAdd,name='profileDataAdd'),
    path('myapplyed/', views.myapplyed,name='myapplyed'),
    path('base/', views.base,name='base'),




    



    


]
