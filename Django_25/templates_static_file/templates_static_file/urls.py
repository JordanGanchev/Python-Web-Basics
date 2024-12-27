from django.contrib import admin
from django.urls import path, include

from templates_static_file.employees.views import employee_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employees/<pk>", employee_details, name="employee_details"),
    path("", include("templates_static_file.employees.urls")),
]
