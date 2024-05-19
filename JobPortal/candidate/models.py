from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from account.models import CustomUser
from employer.models import JobData


# Create your models here.
class CandidateProfile(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=CustomUser)
def create_company_data(sender, instance, created, **kwargs):
    if created and instance.user_type == 'candidate':
        CandidateProfile.objects.create(user=instance, email=instance.email)


class QualificationType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    country = models.ForeignKey(QualificationType, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class QualificationData(models.Model):
    user = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    qualifiction_type = models.ForeignKey(QualificationType, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    year_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.qualifiction_type.name},  {self.course}"


class Expriance(models.Model):
    user = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, blank=True, null=True)
    companyname = models.CharField(max_length=100)
    numberofyears = models.IntegerField()

    def __str__(self):
        return f"  {self.companyname} "


class ApplyJob(models.Model):
    APPLY_STATUS = [
        ('Pending', 'Pending'),
        ('Shortlist', 'Shortlist'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved')
    ]
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(JobData, on_delete=models.CASCADE)
    qualification = models.ManyToManyField(QualificationData, blank=True)
    experiences = models.ManyToManyField(Expriance, blank=True)
    apply_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=APPLY_STATUS, default='Pending')

    def __str__(self):
        return f"ApplyJob ID: {self.id}, Candidate: {self.candidate}"

    def get_applied_experiences(self):
        return self.candidate.expriance_set.all()
