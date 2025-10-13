from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses_app.models import Courses


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


@login_required()
def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    current_users = course.current_users.all()
    if request.method == 'POST':
        if request.user not in current_users:
            course.current_users.add(request.user)
        return redirect('course_detail', pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course, 'current_users': current_users})
