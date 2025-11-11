from django.http import Http404
from django.shortcuts import get_object_or_404
from teachers_app.models import Teacher



class TeacherContextMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')

        try:
            teacher = self.get_object() if hasattr(self, 'get_object') else None
            if teacher:
                context['courses'] = teacher.rn_courses.all()
        except (AttributeError, Http404):
            pass

        return context

class TeacherDetailGetObjectsMixin:
    def get_object(self, queryset = None):
        return get_object_or_404(Teacher, pk=self.kwargs['pk'])

class TeacherDeleteGetQuerySetMixin:
    def get_queryset(self):
        return Teacher.objects.all()

