from django.core.mail import send_mail
from django.conf import settings


# def send_forget_password_mail(email, token):
#     subject = 'Your forget password link'
#     message = f'Click the link to register http://127.0.0.1:8000/change-password/{token}/'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message, email_from, recipient_list)
#     return True


def job_apply_candidate_email(email,subject, message):
    # subject = 'Job Application'
    # message = f' Yor appliction for  {job_title} submitted successfully'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def job_apply_empoloyer_email(employer_email, job_title):
    subject = 'Job Application'
    message = f'New application for {job_title} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [employer_email]
    send_mail(subject, message, email_from, recipient_list)
    return True
