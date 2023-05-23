from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todos_api, name='todos_api'),
    path('todos/<int:id>', views.todo_api, name='todo_api'),
    path('todos/user/<int:id>', views.user_todos_api, name='user_todos_api')
]
