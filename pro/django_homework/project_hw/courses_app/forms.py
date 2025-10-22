from django import forms
from django.core.exceptions import ValidationError

from courses_app.models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'description', 'program', 'start_date', 'end_date', 'image', ]

        error_messages = {
            'title': {
                'required': 'Це поле обов\'язкове',
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введіть назву курсу', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Введіть опис курсу', 'class': 'form-control'}),
            'program': forms.Textarea(attrs={'placeholder': 'Введіть програму курсу', 'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise ValidationError("Дата завершення не може бути раніше дати початку!")

        if title and start_date and end_date:
            title_lower = title.lower()
            existing_courses = Courses.objects.filter(start_date=start_date, end_date=end_date)

            if self.instance.pk:
                existing_courses = existing_courses.exclude(pk=self.instance.pk)

            for course in existing_courses:
                if course.title.lower() == title_lower:
                    raise ValidationError('Курс з такою назвою та датами початку/кінця вже існує!')

        return cleaned_data
