from django.urls import path

from animalsframe.common.views import index

urlpatterns = (
    path('', index, name='index'),
)