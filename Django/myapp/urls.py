from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),   
    path('list/', views.list, name="list"),
    #delete con email
    path('delete/<str:id>', views.delete, name="delete"),
    path('get/<str:id>', views.get, name="get"),
    path('update/<str:id>', views.update, name="update")
]

