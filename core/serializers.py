from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from core.models import University
from core.models import Campus
from core.models import Vehicle
from core.models import Student
from core.models import StudentVehicle
from core.models import RideRequest
from core.models import RideDriver
from core.models import Schedule
from core.models import ScheduleCancel
from core.models import Route
from core.models import Review


class UniversitySerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CampusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'
class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class StudentVehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentVehicle
        fields = '__all__'

class RideRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = RideRequest
        fields = '__all__'
class RideDriverSerializers(serializers.ModelSerializer):
    class Meta:
        model = RideDriver
        fields = '__all__'
class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
class ScheduleCancelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCancel
        fields = '__all__'
class RouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'