from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from django.contrib.auth import get_user_model

User = get_user_model()


class Teacher(models.Model):
    full_teacher_name = models.CharField(max_length=100, verbose_name='ПІБ викладача')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Про викладача')
    photo = models.ImageField(upload_to='teachers_images', blank=True, null=True)
    specialties = models.CharField(max_length=200, blank=True, verbose_name='Спеціалізація(напрямок)')
    logs = GenericRelation('action_logs_app.ActionLog', related_query_name='teacher')
    t_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='rn_teacher')

    def __str__(self):
        return self.full_teacher_name

    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'
        ordering = ['full_teacher_name']
