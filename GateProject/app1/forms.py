from django import forms
from .models import Applicant

class ApplicantModelForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'