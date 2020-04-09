from django.contrib import admin
from django.urls import path, include
app_name='report'
urlpatterns = [
    path("", views.consult, name='consult' ),
]