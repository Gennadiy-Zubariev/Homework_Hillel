from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from teachers_app.models import Teacher
from teachers_app.forms import TeacherForm
from mixins.teacher_mixins import (
    TeacherContextMixin,
    TeacherDetailGetObjectsMixin,
    TeacherDeleteGetQuerySetMixin)


class TeacherDetailView(LoginRequiredMixin, TeacherContextMixin, TeacherDetailGetObjectsMixin, DetailView):
    model = Teacher
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'


class AddTeacherView(LoginRequiredMixin, TeacherContextMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/add_edit_teacher.html'

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('courses_list')

    def form_valid(self, form):
        form.instance.t_user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Викладача {form.instance.full_teacher_name} створено')
        return response


class DeleteTeacherView(LoginRequiredMixin, TeacherDeleteGetQuerySetMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('courses_list')
    context_object_name = 'teacher'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Курс видалено!')
        return super().delete(request, *args, **kwargs)
