from django.urls import path

from .views import StudentListView, StudentUpdateView, StudentCreateView, StudentDeleteView

app_name = 'students'

urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]
