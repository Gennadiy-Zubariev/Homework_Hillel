from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ActionLog(models.Model):
    action_choises = [
        ('create', 'Створення'),
        ('update', 'Оновлення'),
        ('delete', 'Видалення'),
        ('enroll', 'Запис на курс'),
        ('unenroll', 'Відпис від курсу'),
    ]

    action_type = models.CharField(max_length=20, choices=action_choises)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True,
                                     blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    description = models.TextField(blank=True)  # <-- додати це поле


    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

        ordering = ['-timestamp']





