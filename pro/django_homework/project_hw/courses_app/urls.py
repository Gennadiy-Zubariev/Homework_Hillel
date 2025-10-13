from django.urls import path
from courses_app.views import courses_list, course_detail

urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('<int:pk>/', course_detail, name='course_detail'),

]
