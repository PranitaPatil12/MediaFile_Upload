from django.contrib import admin
from .models import Applicant

# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['Applicant_name','Mobile_No','Gender','Address','Aadhar_No','Picture','document']

admin.site.register(Applicant,ApplicantAdmin)