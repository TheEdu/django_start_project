"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(
        min_length=4,
        max_length=50,
        label="Usuario"
    )
    username.widget.attrs['class'] = 'form-control'

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(),
        label="Contraseña"
    )
    password.widget.attrs['class'] = 'form-control'

    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(),
        label="Confirmar contraseña"
    )
    password_confirmation.widget.attrs['class'] = 'form-control'

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Nombres"
    )
    first_name.widget.attrs['class'] = 'form-control'

    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        label="Apellidos"
    )
    last_name.widget.attrs['class'] = 'form-control'

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(),
        label="Email"
    )
    email.widget.attrs['class'] = 'form-control'

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)