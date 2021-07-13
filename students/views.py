from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from core.views import EditView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields


def hello(request):
    return HttpResponse('Hello')


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        obj_list = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

        return obj_list


class UpdateStudentView(EditView):
    model = Student
    form_class = StudentUpdateForm
    success_url = 'students:list'
    template_name = 'students/update.html'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'