from teachers.views import TeachersUpdateView, \
    TeachersListView, TeachersCreateView, TeachersDeleteView
from django.urls import path

app_name = 'teachers'

urlpatterns = [
    path('', TeachersListView.as_view(), name='list'),
    path('create/', TeachersCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TeachersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TeachersDeleteView.as_view(), name='delete'),
]
