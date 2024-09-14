from .views import StudentViewSet

from rest_framework.routers import DefaultRouter

from django.urls import path, include



router = DefaultRouter()
# basename="" -> Blank to avoid 'student/' again as endpoint, because already redirected by student/
router.register(r'student', StudentViewSet, basename="student")


urlpatterns = [
    path('', include(router.urls)),
]
