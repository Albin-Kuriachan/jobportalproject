from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import  CustomUser
from django.contrib import messages, auth
from .forms import *


def company_register(request):
    # form = UserAdminCreationForm()
    # if request.method == 'POST':
    #     form = UserAdminCreationForm(request.POST)
    #     if form.is_valid():
    #   CustomUser.objects.create_user( email=email, password=password)
    #         form.save()
    #         return redirect(company_login)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        usertype = request.POST.get('usertype')
        print("Please enter your", usertype)

        if password == confirmpassword:
            user = CustomUser.objects.create_user(email=email, password=password, user_type=usertype)
            user.save();
            messages.success(request, 'Registration successful')

            return redirect(company_login)
        else:
            messages.success(request, 'Password not match')
            return redirect(company_login)
    return redirect(company_login)

    # messages.success(request, 'Password not match')
    # return render(request, 'company_register.html', {'form': form})


# def company_register(request):
#     if request.method == 'POST':
#         form = UserAdminCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('company_login')  # assuming 'company_login' is the name of your login URL pattern
#             else:
#                 # Handle the case where authentication fails
#                 pass
#     else:
#         form = UserAdminCreationForm()

#     return render(request, 'company_register.html', {'form': form})


def company_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)

            if user is not None:
                if user.user_type == 'employer':
                    login(request, user)
                    return redirect('company_homepage')  # Redirect to company homepage
                else:
                    login(request, user)
                    return redirect('index')  # Redirect to index page
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'company_login.html', {'form': form})


# if user is not None :
#                 login(request, user)
#                 return redirect(company_homepage)
#             else:
#                 form.add_error(None, 'Invalid username or password.')

# def company_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         print(email,password)

#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(company_homepage)  # Assuming company_homepage is a URL name or path
#         else:
#             # Handle invalid login credentials
#             # You might want to add an error message here
#             pass

#     return render(request, 'company_login.html')


@login_required
def company_logout(request):
    auth.logout(request)
    return redirect(company_login)