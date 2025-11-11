from django.urls import path
from teachers_app.views import AddTeacherView, TeacherDetailView, DeleteTeacherView

urlpatterns = [
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('add/', AddTeacherView.as_view(), name='add_teacher'),
    path('<int:pk>/delete/', DeleteTeacherView.as_view(), name='delete_teacher')
]
