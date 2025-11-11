from django.urls import path
# from courses_app.views import courses_list, course_detail, add_course, edit_course, delete_course
from courses_app.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='add_course'),
    path('edit/<int:pk>/', CourseUpdateView.as_view(), name='edit_course'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='delete_course'),

]
