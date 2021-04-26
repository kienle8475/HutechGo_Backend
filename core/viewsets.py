from os import error
from rest_framework import viewsets, permissions
from rest_framework.response import Response

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

from core.serializers import UniversitySerializers
from core.serializers import CampusSerializers
from core.serializers import VehicleSerializers
from core.serializers import StudentSerializers
from core.serializers import StudentVehicleSerializers
from core.serializers import RideRequestSerializers
from core.serializers import RideDriverSerializers
from core.serializers import ScheduleSerializers
from core.serializers import ScheduleCancelSerializers
from core.serializers import RouteSerializers
from core.serializers import ReviewSerializers


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UniversitySerializers

class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CampusSerializers

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VehicleSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializers

class StudentVehicleViewSet(viewsets.ModelViewSet):
    queryset = StudentVehicle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentVehicleSerializers

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RideRequestSerializers


class RideDriverViewSet(viewsets.ModelViewSet):
    queryset = RideDriver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RideDriverSerializers

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScheduleSerializers

class ScheduleCancelViewSet(viewsets.ModelViewSet):
    queryset = ScheduleCancel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScheduleCancelSerializers

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RouteSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReviewSerializers