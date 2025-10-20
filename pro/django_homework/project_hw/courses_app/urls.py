from django.urls import path
from courses_app.views import courses_list, course_detail, add_course, edit_course, delete_course

urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('<int:pk>/', course_detail, name='course_detail'),
    path('create/', add_course, name='add_course'),
    path('edit/<int:pk>/', edit_course, name='edit_course'),
    path('<int:pk>/delete/', delete_course, name='delete_course')

]
