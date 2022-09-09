from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='exp_index'),
    path('add/', views.add, name='add'),
    path('add/addexpense/', views.addexpense, name='addexpense'),
    path('delete/<int:id>', views.delete, name='delete')
]