from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses_api.views import (
    CoursesViewSet,
    TeacherViewSet,
    MembersViewSet,
    CoursesTokenRefreshView,
    CoursesTokenObtainPairView,
)

router = DefaultRouter()
router.register('courses', CoursesViewSet)
router.register('teachers', TeacherViewSet)
router.register('members', MembersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses-token/', CoursesTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('courses-token/refresh/', CoursesTokenRefreshView.as_view(), name='token_refresh'),
]
