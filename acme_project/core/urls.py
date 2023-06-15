from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.page_not_found.as_view(), name='page_not_found'),
]