from django.urls import path

from . import views

urlpatterns = [
    # if we get into this application and we are on the home page, we will go to the views.index page with the name "index"
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path('generate_word/', views.generate_word, name='generate_word'),
]