import datetime
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from groups.models import Group
from core.models import Person

from dateutil.relativedelta import relativedelta

# Create your models here.
from students.validators import adult_validator, AdultValidator


class Student(Person):
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}, {self.group}'

    # @staticmethod
    # def generate_students(count):
    #     faker = Faker()
    #     for _ in range(count):
    #         st = Student(
    #             first_name=faker.first_name(),
    #             last_name=faker.last_name(),
    #             email=faker.email(),
    #             birthdate=faker.date_between(start_date='-65y', end_date='-18y'),
    #         )
    #
    #         st.age = relativedelta(datetime.date.today(), st.birthdate).years
    #         st.save()

# Generating fake data (Student's objects)
# Student.generate(10)
