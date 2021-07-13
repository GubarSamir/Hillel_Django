import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def adult_validator(birthdate, adult_age_limit = 18):

    age = datetime.datetime.now().year - birthdate.year

    if age < adult_age_limit:
        raise ValidationError(f'Age should be greater than {adult_age_limit} y.o.')


class AdultValidator:

    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, birthdate):
        adult_validator(birthdate, self.age_limit)


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format: "
                                     "'+999999999'. Up to 15 digits allowed.")