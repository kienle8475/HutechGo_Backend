from django.db import models
import uuid
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

def upload_to_student_profile(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/%s.%s" % (instance.student_id, uuid.uuid4(), extension)

def upload_to_student_idcard(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/%s.%s" % (instance.student_id, uuid.uuid4(), extension)

def upload_to_vehicle_image(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/vehicle/vei_%s.%s" % (instance.student_id, uuid.uuid4(), extension)

def upload_to_vehicle_license_plate(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/vehicle/vlp%s.%s" % (instance.student_id, uuid.uuid4(), extension)

def upload_to_driving_license_front(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/dlf%s.%s" % (instance.student_id, uuid.uuid4(), extension)

def upload_to_driving_license_back(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/dlb%s.%s" % (instance.student_id, uuid.uuid4(), extension)
# ---------------------------------------------------------------------------------------

class University(models.Model):
    uni_id = models.CharField(max_length=8, primary_key=True)
    uni_name = models.CharField(max_length= 100)
    uni_city = models.CharField(max_length=50)

class Campus(models.Model):
    campus_id = models.CharField(max_length=1, primary_key=True)
    campus_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    university = models.ForeignKey(University, on_delete=models.PROTECT)

class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=8, primary_key=True)
    vehicle_name = models.CharField(max_length=30)
    vehicle_manufacturer = models.CharField(max_length=20)
    cylinder_capacity =  models.IntegerField()

class Student(models.Model):
    MALE = "M"
    FEMALE = "F"
    ENABLE = 1
    DISABLE = 0
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    
    student_id = models.CharField(max_length=10, primary_key=True)
    phone_number = models.CharField(max_length=10, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthday = models.DateField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    profile_image = models.ImageField(upload_to=upload_to_student_profile)
    idcard_image = models.ImageField(upload_to = upload_to_student_idcard)
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)
    is_driver = models.BooleanField()
    
class StudentVehicle(models.Model):
    svehicle_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    color = models.CharField(max_length=10)
    lp_number = models.CharField(max_length=20)
    lp_image = models.ImageField(upload_to= upload_to_vehicle_license_plate)
    ve_image = models.ImageField(upload_to = upload_to_vehicle_image)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
class RideRequest(models.Model):

    rid = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    time_create = models.TimeField(blank=True, null = True)
    time_pickup = models.TimeField(blank = True, null = True)
    recommended_price = models.FloatField(blank =True, null = True)
    point = models.FloatField(blank = True, null = True)
    status = models.CharField(max_length=100, blank = True)

class RideDriver(models.Model):
    did = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    location_start = models.CharField(max_length=100)
    location_end = models.CharField(max_length=100)
    time_start = models.TimeField()
    time_end = models.TimeField()
    point = models.FloatField()
    status = models.CharField(max_length=100)
    
class Schedule(models.Model):
    sid = models.AutoField(primary_key=True)
    did = models.ForeignKey(RideDriver, on_delete= models.CASCADE)
    rid = models.ForeignKey(RideRequest, on_delete=models.CASCADE)
    location_pickup = models.CharField(max_length=100)
    location_to = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(max_length=100)
    
class ScheduleCancel(models.Model):
    cid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    reason = models.TextField()

    
class Route(models.Model):
    rid= models.AutoField(primary_key=True)
    sid = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    location_pickup = models.CharField(max_length=100)
    location_end = models.CharField(max_length=100)
    time_start = models.TimeField()
    time_end = models.TimeField()
    lenght = models.FloatField()
    duration = models.IntegerField()
    status = models.CharField(max_length=100)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    rid = models.ForeignKey(Route, on_delete=models.CASCADE)
    comment = models.TextField()
     
