from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView, ListView, CreateView

from core.views import EditView
from teachers.forms import TeachersCreateForm, TeachersUpdateForm, TeachersFilter
from teachers.models import Teacher


from webargs.djangoparser import use_kwargs, use_args
from webargs import fields


class TeachersCreateView(SuccessMessageMixin, CreateView):
    model = Teacher
    form_class = TeachersCreateForm
    success_url = reverse_lazy('teachers:list')
    success_message = 'Teacher has create'
    template_name = 'teachers/create.html'


class UpdateTeachersView(EditView):
    model = Teacher
    form_class = TeachersUpdateForm
    success_url = 'teachers:list'
    template_name = 'teachers/update.html'


class TeachersUpdateView(UpdateView):
    model = Teacher
    form_class = TeachersUpdateForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class TeachersListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teachers/list.html'


class TeachersDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
