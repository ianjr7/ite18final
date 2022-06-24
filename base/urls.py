from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('Book/', views.home, name='home'),
    path('about_us/', views.about_us, name='about-us'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk> /', views.deleteRoom, name='delete-room'),
]

