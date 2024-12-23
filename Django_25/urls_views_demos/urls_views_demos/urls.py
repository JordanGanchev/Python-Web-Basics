"""urls_views_demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from urls_views_demos.departments.views import index, index2, department_1_details, department_2_details, \
    departments_details, departments_details_by_name

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('urls_views_demos.core.urls')),
    path("departments/", include('urls_views_demos.departments.urls')),

    # path("employees", include([
    #     path('', include('urls_views_demos.core')),
    #     path("asd/", index),
    #     path("asd2/", department_2_details)
    # ])
    #      ),
)

'''
When creating new Django App
1. Add the Django App in ;INSTALL_APPS'
2. Create 'urls.py' in the Django App
3. Include the Django App`s 'urls.py' in global 'urls.py'
'''

'''
# Diff between 'path' and 'str' in urls:
department/gosh/pesho -> path
department/gosho -> str
'''
