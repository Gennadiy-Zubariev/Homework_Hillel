from django.urls import path
from django.contrib.auth.views import LoginView
from members_app.views import MemberRegistrationView, MemberProfileView, MemberLogoutView, UnenrollCourseView

urlpatterns = [
    path('register/', MemberRegistrationView.as_view(), name='register'),
    path('profile/', MemberProfileView.as_view(), name='profile'),
    path('unenroll/<int:course_id>/', UnenrollCourseView.as_view(), name='unenroll'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='members/login.html'), name='login'),
]
