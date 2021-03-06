from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from core.views import EditView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields
from copy import copy


def hello(request):
    return HttpResponse('Hello')


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    success_message = 'Student has create'
    template_name = 'students/create.html'


class StudentListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    model = Student
    template_name = 'students/list.html'

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headed_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_filter'] = self.get_filter()

        params = self.request.GET
        if 'page' in params:
            params = copy(params)
            del params['page']

        context['get_params'] = params.urlencode()

        return context


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