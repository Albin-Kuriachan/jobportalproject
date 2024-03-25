from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from account.models import CustomUser
# Create your models here.


class CompanyData(models.Model):
        user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=True) 
        company_name = models.CharField(max_length=100,blank=True,null=True)
        location = models.CharField(max_length=100,blank=True,null=True)
        email = models.EmailField(max_length=100,blank=True,null=True)
        phone = models.IntegerField(blank=True,null=True)
        logo = models.ImageField(upload_to='company_logo', blank=True, null=True)
        website = models.URLField(blank=True, null=True)

        def __str__(self):
                return f"{self.company_name} "
      

    

@receiver(post_save, sender=CustomUser) 
def create_company_data(sender, instance, created, **kwargs):
    if created:
        CompanyData.objects.create(user=instance, email=instance.email)





class JobData(models.Model):
    EMPLOYMENT = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
        ('Temporary', 'Temporary'),
        ('Remote', 'Remote'),
        ('Other', 'Other')
    ]

    company = models.ForeignKey('CompanyData', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    posted_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(blank=True, null=True)
    salary = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='jobimage',null=True, blank=True)

    def __str__(self):
        return f"{self.company.company_name} - {self.job_title}"


