from django.urls import path
from action_logs_app.views import ActionLogListView

urlpatterns = [
    path('', ActionLogListView.as_view(), name='logs_list'),
]