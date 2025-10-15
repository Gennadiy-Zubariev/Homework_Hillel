from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses_app.models import Courses
from members_app.models import Members


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


@login_required()
def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    current_users = course.members.all()
    if request.method == 'POST':
        profile, created = Members.objects.get_or_create(
            user=request.user,
            defaults={
                'full_name': request.user.username,
            }
        )
        if not profile.courses.filter(pk=course.pk).exists():  # Швидша перевірка
            profile.courses.add(course)
        return redirect('course_detail', pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course, 'current_users': current_users})
