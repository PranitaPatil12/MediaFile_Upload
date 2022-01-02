from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import ApplicantModelForm
from .models import Applicant
from django.views import View




class ApplicationView(View):
    def get(self,request):
        form = ApplicantModelForm
        template_name = 'app1/applicationform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = ApplicantModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("details")
        template_name = 'app1/applicationform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowData(View):
    def get(self,request):
        applicant_list = Applicant.objects.all()
        template_name = 'app1/details.html'
        context = {'applicant_list': applicant_list}
        return render(request, template_name, context)

class ApplicationUpdate(View):
    def get(self,request,i):
        laptop = Applicant.objects.get(id=i)
        form = ApplicantModelForm(instance=laptop)
        template_name = 'app1/applicationform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Applicant.objects.get(id=i)
        form = ApplicantModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("details")
        template_name = 'app1/applicationform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ApplicantDelete(View):

    def post(self,request,i):
        laptop = Applicant.objects.get(id=i)
        laptop.delete()
        return redirect("details")

class ApplicantDetails(View):
    def get(self,request,i):
        applicant = Applicant.objects.get(id=i)
        template_name = 'app1/applicant_details.html'
        context = {'applicant': applicant}
        return render(request, template_name, context)