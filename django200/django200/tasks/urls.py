
from django.urls import path

from django200.tasks.views import index, get_all_tasks

urlpatterns = (
    path('', index),
    path('all/', get_all_tasks)
)