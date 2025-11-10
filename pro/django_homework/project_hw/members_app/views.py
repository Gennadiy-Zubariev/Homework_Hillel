from django.views.generic import CreateView, TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat.errors import messages
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from members_app.forms import RegistrationForm
from courses_app.models import Courses
from members_app.models import Members

from django.contrib.auth import get_user_model

User = get_user_model()


class MemberRegistrationView(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('courses_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Реєстрація успішна! Ласкаво просимо.')
        return super().form_valid(form)


class MemberProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'members/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile, created = Members.objects.get_or_create(m_user=self.request.user)
        context['profile'] = profile
        context['current'] = profile.m_courses.all()
        return context


class UnenrollCourseView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        course = get_object_or_404(Courses, pk=self.kwargs['course_id'])
        profile, created = Members.objects.get_or_create(m_user=self.request.user)
        if profile.m_courses.filter(pk=course.pk).exists():
            profile.m_courses.remove(course)
            messages.success(self.request, f'Ви відписалися від курсу "{course.title}".')
        return reverse_lazy('profile')


class MemberLogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse_lazy('courses_list')
