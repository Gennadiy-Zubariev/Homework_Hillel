from django.urls import reverse_lazy
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

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('courses_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.t_user = self.request.user
        instance.save()
        messages.success(self.request, f'Викладача {form.instance.full_teacher_name} створено')
        return super().form_valid(form)


