from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.ApplicationView.as_view(),name='add_applicant'),
    path('show/',views.ShowData.as_view(),name='details'),
    path('update/<int:i>/',views.ApplicationUpdate.as_view(),name='update'),
    path('delete/<int:i>/',views.ApplicantDelete.as_view(),name='delete'),
    path('details/<int:i>/',views.ApplicantDetails.as_view(),name='applicant_details')
]