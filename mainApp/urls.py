from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('new/', views.addTask, name='new-task'),
    path('all/', views.viewTasks, name='all-tasks'),
]