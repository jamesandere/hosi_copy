from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    specialty = models.TextField(blank=True)

    class Meta:

        db_table = 'doctors'

    def __str__(self):
        return self.first_name + ' ' + self.last_name   

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"  

class Patient(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    diagnosis = models.CharField(blank=True, default='')
    # doctor = models.ForeignKey('Doctor', related_name='patients', on_delete=models.CASCADE)

    class Meta:

        db_table = 'patients'

    def __str__(self):
        return self.first_name + ' ' + self.last_name   
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    description = models.TextField(blank=True, default='')
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'appointments'