from django import forms
from teachers_app.models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_teacher_name', 'bio', 'specialties', 'photo']

        widgets = {
            'full_teacher_name': forms.TextInput(attrs={'placeholder': 'Введіть ПІБ викладача', 'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Про викладача', 'class': 'form-control', 'rows': 5}),
            'specialties': forms.TextInput(attrs={'placeholder': 'Викладає такі курси', 'class': 'form-control'})
        }

