from django.contrib.admin import action
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from courses_app.models import Courses
from members_app.models import Members
from courses_app.forms import CourseForm
from teachers_app.models import Teacher


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
            'is_enrolled': is_enrolled,
        })


@login_required()
def add_course(request):
    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'add_teacher':
            form_data = {
                'title': request.POST.get('title', ''),
                'description': request.POST.get('description', ''),
                'program': request.POST.get('program', ''),
                'start_date': request.POST.get('start_date', ''),
                'end_date': request.POST.get('end_date', ''),
            }
            request.session['draft_course_data'] = form_data

            teacher_to_add_id = request.POST.get('teacher_to_add')
            if teacher_to_add_id:
                try:
                    teacher = Teacher.objects.get(pk=teacher_to_add_id)
                    if 'draft_teachers' not in request.session:
                        request.session['draft_teachers'] = []
                    if int(teacher_to_add_id) not in request.session['draft_teachers']:
                        request.session['draft_teachers'].append(int(teacher_to_add_id))
                        request.session.modified = True
                        messages.success(request,
                                         f'Додано викладача: {teacher.full_teacher_name} (всього: {len(request.session["draft_teachers"])}).')
                    else:
                        messages.info(request, f'{teacher.full_teacher_name} вже доданий')
                except Teacher.DoesNotExist:
                    messages.error(request, 'Викладача не знайдено')
            else:
                messages.warning(request, 'Виберіть викладача')
            return redirect('add_course')

        if action == 'save':
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = form.save(commit=False)
                course.c_owner = request.user
                course.save()

                draft_teachers_pks = request.session.get('draft_teachers', [])
                added_count = 0
                for teacher_pk in draft_teachers_pks:
                    try:
                        teacher = Teacher.objects.get(pk=teacher_pk)
                        if not course.c_teachers.filter(pk=teacher.pk).exists():
                            course.c_teachers.add(teacher)
                            added_count += 1
                    except Teacher.DoesNotExist:
                        pass

                if added_count > 0:
                    messages.success(request, f'Додано {added_count} викладача(ів).')

                if 'draft_teachers' in request.session:
                    del request.session['draft_teachers']
                if 'draft_course_data' in request.session:
                    del request.session['draft_course_data']

                messages.success(request, 'Курс створено!')
                return redirect('courses_list')
            else:
                messages.error(request, 'Виправте помилки у формі!')
    else:
        draft_data = request.session.get('draft_course_data', {})
        form = CourseForm(initial=draft_data) if draft_data else CourseForm()
    draft_teachers_pks = request.session.get('draft_teachers', [])
    draft_teachers = Teacher.objects.filter(pk__in=draft_teachers_pks).order_by('full_teacher_name')

    return render(request, 'courses/add_edit_course.html', {
        'form': form,
        'draft_teachers': draft_teachers
    })


@login_required()
def edit_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)

    if course.c_owner != request.user:
        messages.error(request, 'Ви не можете редагувати цей курс, бо ви його не створювали!')
        return redirect('course_detail', pk=pk)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'remove_teacher':
            teacher_id = request.POST.get('teacher_id')
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            course.c_teachers.remove(teacher)
            messages.success(request, f'Викладача {teacher.full_teacher_name} видалено з курсу.')
            return redirect('edit_course', pk=pk)

        elif action == 'add_teacher':
            teacher_to_add_id = request.POST.get('teacher_to_add')
            if teacher_to_add_id:
                try:
                    teacher = Teacher.objects.get(pk=teacher_to_add_id)
                    if 'edit_draft_teachers' not in request.session:
                        request.session['edit_draft_teachers'] = []
                    if int(teacher_to_add_id) not in request.session['edit_draft_teachers']:
                        request.session['edit_draft_teachers'].append(int(teacher_to_add_id))
                        request.session.modified = True
                        # if not course.c_teachers.filter(pk=teacher_to_add_id).exists():
                        #     course.c_teachers.add(teacher)
                        messages.success(request, f'Викладача {teacher.full_teacher_name} додано до курсу.')
                    else:
                        messages.info(request, f'{teacher.full_teacher_name} уже є в курсі.')
                except Teacher.DoesNotExist:
                    messages.error(request, 'Викладача не знайдено.')
            else:
                messages.warning(request, 'Виберіть викладача перед додаванням.')
            return redirect('edit_course', pk=pk)

        elif action == 'save':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()

                edit_draft_teachers_pks = request.session.get('edit_draft_teachers', [])
                for teacher_pk in edit_draft_teachers_pks:
                    try:
                        teacher = Teacher.objects.get(pk=teacher_pk)
                        if not course.c_teachers.filter(pk=teacher.pk).exists():
                            course.c_teachers.add(teacher)
                    except Teacher.DoesNotExist:
                        pass

                if 'edit_draft_teachers' in request.session:
                    del request.session['edit_draft_teachers']
                    request.session.modified = True
                if 'edit_course_data' in request.session:
                    del request.session['edit_course_data']
                    request.session.modified = True

                messages.success(request, 'Курс оновлено!')
                return redirect('course_detail', pk=pk)
            else:
                messages.error(request, 'Форма містить помилки!')
    else:

        form = CourseForm(instance=course)

    edit_draft_teachers_pks = request.session.get('edit_draft_teachers', [])
    edit_draft_teachers = Teacher.objects.filter(pk__in=edit_draft_teachers_pks).order_by('full_teacher_name')

    return render(request, 'courses/add_edit_course.html', {
        'form': form,
        'course': course,
        'edit_draft_teachers': edit_draft_teachers,
    })


@login_required()
def delete_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)

    if course.c_owner != request.user:
        messages.error(request, 'Ви не можете видалити цей курс, бо ви його не створювали!')
        return redirect('course_detail', pk=pk)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Курс видалено!')
        return redirect('courses_list')

    return render(request, 'courses/course_confirm_delete.html', {'course': course})
