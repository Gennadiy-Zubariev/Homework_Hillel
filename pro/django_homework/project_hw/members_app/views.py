from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from courses_app.models import Courses
from members_app.models import Members
from django.contrib.auth.decorators import login_required
from members_app.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses_list')
    else:
        form = RegistrationForm()

    return render(request, 'members/register.html', {'form': form})


@login_required
def profile(request):
    profile, created = Members.objects.get_or_create(m_user=request.user)
    current = profile.m_courses.all()
    return render(request, 'members/profile.html', {'profile': profile, 'current': current})


@login_required
def current(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    profile, created = Members.objects.get_or_create(m_user=request.user)
    if profile.m_courses.filter(pk=course.pk).exists():
        profile.m_courses.remove(course)
    return redirect('profile')


def user_logout(request):
    logout(request)
    return redirect('courses_list')
