from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404  # noqa
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from core.views import EditView
from students.forms import StudentCreateForm, StudentUpdateForm, StudentsFilter
from students.models import Student

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields


def hello(request):
    return HttpResponse('Hello')


@use_args(
    {
        "first_name": fields.Str(
            required=False
        ),
        "last_name": fields.Str(
            required=False
        ),
        "birthdate": fields.Date(required=False),
    },
    location="query",
)
def get_students(request, args):
    students = Student.objects.all().select_related('group', 'headed_group')

    # for param_name, param_value in args.items():
    #     if param_value:
    #         students = students.filter(**{param_name: param_value})

    obj_filter = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'students': students,
            'obj_filter': obj_filter,
        }
    )


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        obj_list = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )

        return obj_list


@login_required
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'form': form
        }
    )


# @csrf_exempt
def update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(instance=student, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentUpdateForm(instance=student)

    return render(
        request=request,
        template_name='students/update.html',
        context={
            'form': form
        }
    )


def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/delete.html',
        context={
            'student': student
        }
    )


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
