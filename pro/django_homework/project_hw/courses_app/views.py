from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses_app.models import Courses
from members_app.models import Members
from courses_app.forms import CourseForm


def courses_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})


@login_required()
def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    current_users = course.rn_members.all()

    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = course.rn_members.filter(m_user=request.user).exists()

    if request.method == 'POST':
        action = request.POST.get('action')
        profile, created = Members.objects.get_or_create(m_user=request.user)

        if action == 'add':
            if not profile.m_courses.filter(pk=course.pk).exists():
                profile.m_courses.add(course)

        if action == 'remove':
            if profile.m_courses.filter(pk=course.pk).exists():
                profile.m_courses.remove(course)

        return redirect('course_detail', pk=pk)
    return render(
        request,
        'courses/course_detail.html',
        {
            'course': course,
            'current_users': current_users,
            'is_enrolled': is_enrolled
        })


@login_required()
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.c_owner = request.user
            course.save()
            return redirect('courses_list')
    else:
        form = CourseForm()

    return render(request, 'courses/add_edit_course.html', {'form': form})


@login_required()
def edit_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)

    if course.c_owner != request.user:
        messages.error(request, 'Ви не можете редагувати цей курс, бо ви його не створювали!')
        return redirect('course_detail', pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/add_edit_course.html', {'form': form})


@login_required()
def delete_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)

    if course.c_owner != request.user:
        messages.error(request, 'Ви не можете видалити цей курс, бо ви його не створювали!')
        return redirect('course_detail', pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('courses_list')

    return render(request, 'courses/course_confirm_delete.html', {'course': course})
