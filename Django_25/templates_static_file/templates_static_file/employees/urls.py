from django.urls import path

from templates_static_file.employees.views import index, employee_details

urlpatterns = (
    path("", index, name='index'),
    path("employees/<pk>", employee_details, name="employee_details"),
)