import datetime
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonExampleForm(forms.ModelForm):
    uuid = forms.CharField(label='DNI')
    uuid.widget.attrs['class'] = 'form-control'

    firstName = forms.CharField(label='Nombres')
    firstName.widget.attrs['class'] = 'form-control'

    lastName = forms.CharField(label='Apellidos')
    lastName.widget.attrs['class'] = 'form-control'

    gender = forms.ModelChoiceField(label='Género', queryset=GenderExample.objects.all())

    class Meta:
        model = PersonExample
        fields = ('uuid', 'firstName', 'lastName', 'gender')


class GenderExampleForm(forms.ModelForm):
    uuid = forms.CharField(label='Género')
    uuid.widget.attrs['class'] = 'form-control'

    description = forms.CharField(label='Descripción')
    description.widget.attrs['class'] = 'form-control'

    class Meta:
        model = GenderExample
        fields = ('uuid', 'description')