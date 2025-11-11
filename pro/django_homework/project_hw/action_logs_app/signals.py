from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from courses_app.models import Courses
from members_app.models import Members
from teachers_app.models import Teacher
from accounts_app.models import MembersUser
from action_logs_app.models import ActionLog


@receiver(post_save, sender=Courses)
def log_course_save(sender, instance, created, **kwargs):
    # Пропускаємо, якщо це проміжне збереження (raw=True при fixtures)
    if kwargs.get('raw', False):
        return

    action = 'create' if created else 'update'
    user = getattr(instance, 'c_owner', None)  # безпечне отримання

    ActionLog.objects.create(
        action_type=action,
        user=user,
        content_object=instance,
        description=f'{"Створено" if created else "Оновлено"} курс "{instance.title}"'
    )


@receiver(post_delete, sender=Courses)
def log_course_delete(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    ActionLog.objects.create(
        action_type='delete',
        user=instance.c_owner,
        content_type=content_type,
        object_id=instance.pk,
        description=f'Видалено курс "{instance.title}" (ID: {instance.pk})'
    )


@receiver(post_save, sender=Teacher)
def log_teacher_save(sender, instance, created, **kwargs):
    ActionLog.objects.create(
        action_type='create',
        user=instance.t_user,
        content_object=instance,
        description=f'{"Створено" if created else "Оновлено"} викладача "{instance.full_teacher_name}"'
    )


@receiver(post_delete, sender=Teacher)
def log_teacher_delete(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(instance)
    ActionLog.objects.create(
        action_type='delete',
        user=instance.t_user,
        content_type=content_type,
        object_id=instance.pk,
        description=f'Видалено викладача "{instance.full_teacher_name}" (ID: {instance.pk})'
    )


@receiver(post_save, sender=MembersUser)
def log_user_save(sender, instance, created, **kwargs):
    if created:
        ActionLog.objects.create(
            action_type='create',
            user=instance,
            content_object=instance,
            description=f'Зареєстровано користувача "{instance.email}"'
        )


@receiver(m2m_changed, sender=Members.m_courses.through)
def log_enrollment(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for course_pk in pk_set:
            try:
                course = Courses.objects.get(pk=course_pk)
                ActionLog.objects.create(
                    action_type='enroll',
                    user=instance.m_user,
                    content_object=course,
                    description=f'Користувач {instance.m_user.email} записався на курс "{course.title}"'
                )
            except Courses.DoesNotExist:
                pass

    elif action == 'post_remove':
        for course_pk in pk_set:
            try:
                course = Courses.objects.get(pk=course_pk)
                ActionLog.objects.create(
                    action_type='unenroll',
                    user=instance.m_user,
                    content_object=course,
                    description=f'Користувач {instance.m_user.email} відписався від курсу "{course.title}"'
                )
            except Courses.DoesNotExist:
                pass
