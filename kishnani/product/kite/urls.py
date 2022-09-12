from django.urls import path,include
from . import views

urlpatterns = [
      path('home/',views.home,name="home"),
      path('about/',views.about),
      path('insert/',views.insert,name="min"),
      path('match/',views.match,name="add"),
    # localhost:8000/blog/home
]