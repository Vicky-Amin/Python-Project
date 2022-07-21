from django.db import models

# # Create your models here.

class User (models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    otp = models.IntegerField(default=123)
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) ->str:
        return self.email

class Doctor(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30,blank=True, null=True)
    qualification = models.CharField(max_length=30,blank=True, null=True)
    specification = models.CharField(max_length=50, blank=True,null=True)
    availabal_time = models.CharField(max_length=50, blank=True,null=True)
    experiance = models.CharField(max_length=50, blank=True,null=True)
    clinic_name = models.CharField(max_length=50, blank=True,null=True)
    clinic_city = models.CharField(max_length=50, blank=True,null=True)
    clinic_address = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    pic = models.FileField(upload_to='media/images',default='media/default_doc.png')


    def __str__(self) ->str:
        return self.firstname

class Patient (models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField(default=True,blank=True,null=True)
    gender = models.BooleanField(default=True,blank=True,null=True)
    birthdate = models.DateTimeField(auto_created=False,blank=True,null=True)
    bloodgroup = models.CharField(max_length=10,blank=True,null=True)
    height = models.FloatField (max_length=10,blank=True,null=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    weight = models.FloatField(max_length=10,blank=True,null=True)
    patient_address = models.TextField(blank=True,null=True)

    def __str__(self) ->str:
        return self.firstname

class Appointment(models.Model):
    Patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    a_data = models.DateField(max_length=30)
    a_time = models.CharField(max_length=30)
    reason = models.TextField()
    status = models.CharField(max_length=30,default='Pending')
    doc_note = models.TextField(blank=True)
    case_status = models.CharField(max_length=30)