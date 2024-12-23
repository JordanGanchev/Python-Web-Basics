from django.urls import path

from urls_views_demos.departments.views import departments_details, departments_details_by_name

urlpatterns = (
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),
    path("<int:pk>/", departments_details),
    path("<str:name>/", departments_details_by_name),
)