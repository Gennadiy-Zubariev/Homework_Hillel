from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from teachers_app.models import Teacher
from teachers_app.forms import TeacherForm


@login_required
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    courses = teacher.rn_courses.all()

    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher, 'courses': courses})


class AddTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/add_edit_teacher.html'
    success_url = '/courses/'

    def form_valid(self, form):
        messages.success(self.request, f'Викладача {form.instance.full_teacher_name} створено')
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()
