from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('create/',views.create, name='create'),
    path('insert/',views.add, name='add'),
    path('edit/<pk>',views.edit, name='edit'),
    path('update',views.update,name='update'),
    path('delete/<pk>',views.delete,name='delete')
]
