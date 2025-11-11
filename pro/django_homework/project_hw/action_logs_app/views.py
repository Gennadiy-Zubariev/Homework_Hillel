from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from action_logs_app.models import ActionLog

class ActionLogListView(UserPassesTestMixin, ListView):
    model = ActionLog
    template_name = 'action_logs/logs_list.html'
    context_object_name = 'logs'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser
