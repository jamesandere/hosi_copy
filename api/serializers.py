from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source='doctor.get_full_name')
    patient = serializers.ReadOnlyField(source='patient.get_full_name')

    class Meta:
        model = Appointment
        fields = ['id', 'description', 'doctor', 'patient', 'appointment_date', 'start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']