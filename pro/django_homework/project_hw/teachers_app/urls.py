from django.urls import path
from teachers_app.views import teacher_detail, AddTeacherView

urlpatterns = [
    path('<int:pk>/', teacher_detail, name='teacher_detail'),
    path('add/', AddTeacherView.as_view(), name='add_teacher')
]