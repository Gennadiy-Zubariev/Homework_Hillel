from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from members_app.models import Members


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'birth_date')
        password_validators = []

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Members.objects.get_or_create(user=user, defaults={
                'full_name': self.cleaned_data.get('full_name', ''),
                'birth_date': self.cleaned_data.get('birth_date')
            })
        return user
