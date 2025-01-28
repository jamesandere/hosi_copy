from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('patients/', views.PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),
    path('appointments/', views.AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
]
