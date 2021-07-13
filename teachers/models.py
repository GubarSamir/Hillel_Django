from django.db import models

from core.models import Person

from random import randint


class Teacher(Person):
    salary = models.PositiveIntegerField(default=1500)

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(1000, 3000)
        obj.save()


# Generating fake data (Teacher's objects)
# Teacher.generate(10)
