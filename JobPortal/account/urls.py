


from django.urls import path
from account import views

urlpatterns = [

    path('company_login/', views.company_login,name='company_login'),
    path('company_register/', views.company_register,name='company_register'),
    path('company_logout/', views.company_logout, name='company_logout'),



]