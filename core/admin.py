from django.contrib import admin

# Register your models here.
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


admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Vehicle)
admin.site.register(Student)
admin.site.register(StudentVehicle)
admin.site.register(RideRequest)
admin.site.register(RideDriver)
admin.site.register(Schedule)
admin.site.register(ScheduleCancel)
admin.site.register(Route)
admin.site.register(Review)