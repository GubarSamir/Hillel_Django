import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, forms

from teachers.models import Teacher
import django_filters

class TeachersBaseForm(ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'last_name',
            'first_name',
            'age',
            'email',
            'birthdate',
            'salary',

        ]
        # fields = '__all__'
        widgets = {'birthdate': DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Teacher.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(phone_number + ' is already added')
        else:
            return phone_number

class TeachersCreateForm(TeachersBaseForm):
    pass


class TeachersUpdateForm(TeachersBaseForm):
    class Meta(TeachersBaseForm.Meta):
        fields = [
            'last_name',
            'first_name',
            'age',
            'email',
            'birthdate',
            'salary',
        ]


class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'birthdate': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'salary': ['exact', 'startswith'],
            'age': ['exact', 'startswith'],
            'last_name': ['exact', 'startswith'],
        }
