from django.contrib import admin
# from .models import CandidateProfile, QualificationType, QualificationData, Course, Expriance
from .models import *
# Register your models here.
admin.site.register(QualificationType)
admin.site.register(Course)

class QualificationDataInline(admin.TabularInline):
    model = QualificationData
    extra = 0

class ExperienceInline(admin.TabularInline):
    model = Expriance
    extra = 0

class ApplyInline(admin.TabularInline):
    model = ApplyJob
    extra = 0


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    inlines = [QualificationDataInline, ExperienceInline,ApplyInline]


class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job')  # Display fields in the list view

admin.site.register(ApplyJob, ApplyJobAdmin)