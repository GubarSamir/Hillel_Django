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
from copy import copy

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


# class TeachersListView(LoginRequiredMixin, ListView):
#     model = Teacher
#     template_name = 'teachers/list.html'


class TeachersListView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Teacher
    template_name = 'teachers/list.html'

    # def get_filter(self):
    #     return TeachersFilter(
    #         data=self.request.GET,
    #         queryset=self.model.objects.all().select_related('group', 'headed_group')
    #     )

    # def get_queryset(self):
    #     return self.get_filter().qs
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_filter'] = self.get_filter()
    #
    #     params = self.request.GET
    #     if 'page' in params:
    #         params = copy(params)
    #         del params['page']
    #
    #     context['get_params'] = params.urlencode()
    #
    #     return context


class TeachersDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
