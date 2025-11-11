from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from action_logs_app.models import ActionLog
from mixins.action_log_mixins import ActionLogSuperuserMixin


class ActionLogListView(ActionLogSuperuserMixin, ListView):
    model = ActionLog
    template_name = 'action_logs/logs_list.html'
    context_object_name = 'logs'
    paginate_by = 10
