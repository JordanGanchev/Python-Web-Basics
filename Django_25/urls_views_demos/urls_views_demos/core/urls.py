from django.urls import path
from urls_views_demos.core.views import index


urlpatterns = (
    path('', index),
)