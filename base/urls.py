from django.urls import path
from .views import home, room, create_room, update_room, delete_room, loginPage, logoutUser, registerPage


urlpatterns = [
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('register/',registerPage, name='register'),
    path('', home, name='home'),
    path('room/<str:pk>', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/<str:pk>', update_room, name='update-room'),
    path('delete-room/<str:pk>', delete_room, name='delete-room'),
]
