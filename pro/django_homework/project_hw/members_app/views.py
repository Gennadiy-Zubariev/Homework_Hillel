from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
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
    profile, created = Members.objects.get_or_create(
        user=request.user,
        defaults={
            'full_name': request.user.username,
            'birth_date': '2000-01-01'
        }
    )
    current = request.user.current_users.all()
    return render(request, 'members/profile.html', {'profile': profile, 'current': current})


@login_required
def current(request, course_id):
    course = Courses.objects.get(id=course_id)
    course.current_users.remove(request.user)
    return redirect('profile')


def user_logout(request):
    logout(request)
    return redirect('courses_list')
