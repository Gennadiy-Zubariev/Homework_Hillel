import factory
from datetime import date, timedelta
from django.contrib.auth import get_user_model
from faker import Faker
from courses_app.models import Courses
from teachers_app.models import Teacher
from members_app.models import Members

User = get_user_model()
fake = Faker()

class MembersUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.LazyAttribute(lambda _: fake.email()[:255])
    password = factory.PostGenerationMethodCall('set_password', fake.password())
    first_name = factory.LazyAttribute(lambda _: fake.first_name()[:50])
    last_name = factory.LazyAttribute(lambda _: fake.last_name()[:30])
    phone_number = factory.LazyAttribute(lambda _: fake.phone_number()[:20])
    is_staff = False
    is_superuser = False

class SuperuserFactory(MembersUserFactory):
    is_staff = True
    is_superuser = True

class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    full_teacher_name = factory.LazyAttribute(lambda _: f'{fake.first_name()} {fake.last_name()}'[:20])
    bio = factory.Faker('text', max_nb_chars=30, locale='uk_UA')
    specialties = factory.Faker(
        'random_element',
        elements=(
            'Python',
            'Django',
            'React',
            'Vue',
            'HTML',
            'CSS',
            'JS',
            "FastAPI",
            "Data Science",
            "Machine Learning",
            "Алгоритми",
            "Бази даних"
        ))

    t_user = factory.SubFactory(MembersUserFactory)

class CoursesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Courses

    title = factory.Faker(
        'random_element',
        elements=(
            'Python',
            'Django',
            'React',
            'Vue',
            'HTML',
            'CSS',
            'JS',
            "FastAPI",
            "Data Science",
            "Machine Learning",
            "Алгоритми",
            "Бази даних"
        ))
    description = factory.Faker('text', max_nb_chars=100, locale='uk_UA')
    program = factory.Faker('text', max_nb_chars=100, locale='uk_UA')
    start_date = factory.Faker(
        'date_between',
        start_date=date.today() + timedelta(days=1),
        end_date=date.today() + timedelta(days=365)
    )
    end_date = factory.LazyAttribute(lambda obj: obj.start_date + timedelta(days=fake.random_int(min=1, max=30)))
    c_owner = factory.SubFactory(MembersUserFactory)


class MembersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Members

    m_user = factory.SubFactory(MembersUserFactory)

    @factory.post_generation
    def m_courses(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for course in extracted:
                self.m_courses.add(course)





