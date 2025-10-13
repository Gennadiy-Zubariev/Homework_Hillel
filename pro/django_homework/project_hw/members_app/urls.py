from django.urls import path
from django.contrib.auth.views import LoginView
from members_app.views import register, profile, current, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('current/<int:course_id>/', current, name='current'),
    path('logout/', user_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='members/login.html'), name='login'),
]
