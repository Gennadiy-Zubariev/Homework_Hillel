from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
from members_app.models import Members


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Ім'я")
    last_name = forms.CharField(max_length=50, required=False, label="Прізвище")
    phone_number = forms.CharField(max_length=30, required=True, label="Номер телефону")
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}),
                                    label="Дата народження")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth')
        password_validators = []

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        if commit:
            user.save()
            Members.objects.get_or_create(m_user=user)
        return user
