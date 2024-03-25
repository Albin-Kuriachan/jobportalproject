from django.contrib import admin
from .models import CompanyData,JobData

class JobDataInline(admin.TabularInline):
    model = JobData
    extra = 0  # Controls the number of empty forms displayed

@admin.register(CompanyData)
class CompanyDataAdmin(admin.ModelAdmin):
    inlines = [JobDataInline]

admin.site.register(JobData)
