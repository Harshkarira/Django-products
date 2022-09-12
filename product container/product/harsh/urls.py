from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('insert/',views.insert,name="min"),
    path('match/',views.match,name="add"),
    path('edit/<pk>',views.edit, name='edit'),
    path('delete/<pk>',views.delete,name='delete')
    # localhost:8000/blog/home
]