from django.urls import path
from . import views

urlpatterns = [
    path('', views.listTask, name='list'),
    path('update/<str:pk>', views.updateTask, name='update'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
]
