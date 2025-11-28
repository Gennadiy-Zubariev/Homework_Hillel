from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from courses_app.models import Courses
from teachers_app.models import Teacher
from members_app.models import Members
from courses_app.forms import CourseForm
from mixins.courses_mixins import (
    OwnerRequiredMixin,
    CourseCreateContextDataMixin,
    CourseUpdateContextDataMixin,
    CourseDetailContextDataMixin
)


class CourseListView(LoginRequiredMixin, ListView):
    model = Courses
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Courses.objects.all().order_by('c_owner').prefetch_related('c_owner')


class CourseDetailView(LoginRequiredMixin, CourseDetailContextDataMixin, DetailView):
    model = Courses
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        return super().get_queryset().select_related('c_owner')

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        user = self.request.user
        action = request.POST.get('action')

        if not user.is_authenticated:
            messages.warning(request, 'Увійдіть у систему, щоб записатися на курс.')
            return redirect('login')

        profile, current = Members.objects.get_or_create(m_user=user)

        if action == 'add':
            if not profile.m_courses.filter(pk=course.pk).exists():
                profile.m_courses.add(course)
                messages.success(request, f'Вас додано до курсу "{course.title}"')
            else:
                messages.info(request, 'Ви вже записані на цей курс.')

        elif action == 'remove':
            if profile.m_courses.filter(pk=course.pk).exists():
                profile.m_courses.remove(course)
                messages.success(request, f'Вас видалено з курсу "{course.title}"')

        return redirect('course_detail', pk=course.pk)


class CourseCreateView(LoginRequiredMixin, CourseCreateContextDataMixin, CreateView):
    model = Courses
    form_class = CourseForm
    template_name = 'courses/add_edit_course.html'
    success_url = reverse_lazy('courses_list')

    def post(self, request, *args, **kwargs):
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
                teacher = Teacher.objects.get(pk=teacher_to_add_id)
                if 'draft_teachers' not in request.session:
                    request.session['draft_teachers'] = []
                if int(teacher_to_add_id) not in request.session['draft_teachers']:
                    request.session['draft_teachers'].append(int(teacher_to_add_id))
                    request.session.modified = True

                    messages.success(request,
                                     f'Додано викладача {teacher.full_teacher_name} (всього: {len(request.session["draft_teachers"])}).')
                else:
                    messages.info(request, f'{teacher.full_teacher_name} вже доданий')
            else:
                messages.warning(request, 'Оберіть викладача')
            return redirect('add_course')

        elif action == 'save':
            form = self.get_form()
            if form.is_valid():
                course = form.save(commit=False)
                course.c_owner = request.user
                course.save()

                draft_teachers_pks = request.session.get('draft_teachers', [])
                for teacher_pk in draft_teachers_pks:
                    teacher = Teacher.objects.get(pk=teacher_pk)
                    if not course.c_teachers.filter(pk=teacher.pk).exists():
                        course.c_teachers.add(teacher)

                if 'draft_teachers' in request.session:
                    del request.session['draft_teachers']
                if 'draft_course_data' in request.session:
                    del request.session['draft_course_data']

                messages.success(request, 'Курс створено!')
                return redirect(self.success_url)
            else:
                messages.error(request, 'Виправте помилки у формі!')
                return self.form_invalid(form)

        elif action == 'cancel':
            if 'draft_course_data' in request.session:
                del request.session['draft_course_data']
            if 'draft_teachers' in request.session:
                del request.session['draft_teachers']
            messages.info(request, 'Чернетку скасовано.')  # Опціонально: сповіщення
            return redirect('courses_list')

        return super().post(request, *args, **kwargs)


class CourseUpdateView(LoginRequiredMixin, OwnerRequiredMixin, CourseUpdateContextDataMixin, UpdateView):
    model = Courses
    form_class = CourseForm
    template_name = 'courses/add_edit_course.html'
    success_url = reverse_lazy('courses_list')

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        session_key = f'edit_draft_teachers_{self.object.pk}'
        action = request.POST.get('action')

        if action == 'add_teacher':
            teacher_to_add_id = request.POST.get('teacher_to_add')
            teacher = Teacher.objects.get(pk=teacher_to_add_id)
            if teacher_to_add_id:
                request.session.setdefault(session_key, [])
                if int(teacher_to_add_id) not in request.session[session_key]:
                    request.session[session_key].append(int(teacher_to_add_id))
                    request.session.modified = True
                    messages.success(request, f'Викладача {teacher.full_teacher_name} додано у чергу.')
                else:
                    messages.info(request, f'{teacher.full_teacher_name} уже є в курсі.')

            return redirect('edit_course', pk=self.object.pk)

        if action == 'remove_teacher':
            teacher_id = request.POST.get('teacher_id')
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            self.object.c_teachers.remove(teacher)
            messages.success(request, f'Викладача {teacher.full_teacher_name} видалено.')
            return redirect('edit_course', pk=self.object.pk)


        elif action == 'save':
            form = self.get_form()
            if form.is_valid():
                course = form.save()

                for teacher_id in request.session.get(session_key, []):
                    teacher = Teacher.objects.get(pk=teacher_id)
                    course.c_teachers.add(teacher)

                request.session.pop(session_key, None)
                messages.success(request, 'Курс оновлено!')
                return redirect(self.get_success_url())

            messages.error(request, 'Форма містить помилки!')
            return self.form_invalid(form)

        elif action == 'cancel':
            if session_key in request.session:
                del request.session[session_key]
            messages.info(request, 'Зміни скасовано.')  # Опціонально: сповіщення
            return redirect('courses_list')

        return super().post(request, *args, **kwargs)


class CourseDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Courses
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('courses_list')
    context_object_name = 'course'

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        course.rn_members.clear()
        messages.success(request, 'Курс видалено!')
        return super().delete(request, *args, **kwargs)
