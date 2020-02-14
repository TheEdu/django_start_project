"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50, label="Usuario")
    username.widget.attrs['class'] = 'form-control'
    username.widget.attrs['placeholder'] = 'Usuario'

    password = forms.CharField(max_length=70, widget=forms.PasswordInput(), label="Contraseña")
    password.widget.attrs['class'] = 'form-control'
    password.widget.attrs['placeholder'] = 'Contraseña'

    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput(), label="Confirmar contraseña")
    password_confirmation.widget.attrs['class'] = 'form-control'
    password_confirmation.widget.attrs['placeholder'] = 'Confirmar contraseña'

    first_name = forms.CharField(min_length=2, max_length=50, label="Nombres")
    first_name.widget.attrs['class'] = 'form-control'
    first_name.widget.attrs['placeholder'] = 'Nombres'

    last_name = forms.CharField(min_length=2, max_length=50, label="Apellidos")
    last_name.widget.attrs['class'] = 'form-control'
    last_name.widget.attrs['placeholder'] = 'Apellidos'

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput(), label="Email")
    email.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Email'

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de Usuario ya existe.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
