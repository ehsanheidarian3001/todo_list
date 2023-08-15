from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed/<int:todo_id>', views.completed, name='completed'),
    path('deletecompleted/', views.delete_completed, name='deletecompleted'),
    path('deleteall/', views.delete_all, name='deleteall'),
]
