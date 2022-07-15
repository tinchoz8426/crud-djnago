from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name="Index"),
    path('insert', views.insert, name="Insert"),
    path('delete/<int:task_id>', views.delete, name="Delete"),
    path('update/<int:task_id>', views.update_form, name="UpdateForm"),
    path('update/', views.update, name="Update"),
]