from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('alltask/', views.alltask, name = 'alltask'),
    path('tag/', views.tag, name = 'tag'),
    path('incomplete/', views.incomplete, name = 'incomplete'),
    path('update/?P<int:task_id>/', views.update, name="update"),
    path('delete/?P<int:task_id>/', views.delete, name="delete"),
    path('markcomplete/?P<int:task_id>/', views.markcomplete, name="markcomplete"),
]
