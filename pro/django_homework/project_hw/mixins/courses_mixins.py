from courses_app.forms import CourseForm
from teachers_app.models import Teacher


class OwnerRequiredMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(c_owner=self.request.user)


class CourseCreateContextDataMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        draft_course_data = request.session.get('draft_course_data', {})
        if draft_course_data:
            context['form'] = CourseForm(initial=draft_course_data)
        else:
            context['form'] = CourseForm()

        draft_teachers_pks = request.session.get('draft_teachers', [])
        draft_teachers = Teacher.objects.filter(pk__in=draft_teachers_pks).order_by('full_teacher_name')

        context['all_teachers'] = Teacher.objects.all().order_by('full_teacher_name')
        context['draft_teachers'] = draft_teachers
        return context


class CourseUpdateContextDataMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        session_key = f'edit_draft_teachers_{pk}'
        context['course'] = self.object
        context['edit_draft_teachers'] = Teacher.objects.filter(
            pk__in=self.request.session.get(session_key, [])).order_by('full_teacher_name')
        context['all_teachers'] = Teacher.objects.all().order_by('full_teacher_name')
        return context


class CourseDetailContextDataMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()

        context['current_users'] = course.rn_members.all()
        user = self.request.user
        if user.is_authenticated:
            context['is_enrolled'] = course.rn_members.filter(m_user=user).exists()
        else:
            context['is_enrolled'] = False

        return context
