
from rest_framework import routers
from django.urls import path, include

from core.viewsets import UniversityViewSet
from core.viewsets import CampusViewSet
from core.viewsets import VehicleViewSet
from core.viewsets import StudentViewSet
from core.viewsets import StudentVehicleViewSet
from core.viewsets import RideRequestViewSet
from core.viewsets import RideDriverViewSet
from core.viewsets import ScheduleViewSet
from core.viewsets import ScheduleCancelViewSet
from core.viewsets import RouteViewSet
from core.viewsets import ReviewViewSet


router = routers.DefaultRouter()

router.register( 'university' ,UniversityViewSet)
router.register( 'campus' ,CampusViewSet)
router.register( 'vehicle' ,VehicleViewSet)
router.register( 'student' ,StudentViewSet)
router.register( 'studentvehicle' ,StudentVehicleViewSet)
router.register( 'riderequest' ,RideRequestViewSet)
router.register( 'ridedriver' ,RideDriverViewSet)
router.register( 'schedule' ,ScheduleViewSet)
router.register( 'schedulecancel' ,ScheduleCancelViewSet)
router.register( 'route' ,RouteViewSet)
router.register( 'review' ,ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]