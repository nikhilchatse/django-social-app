from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('/',home,name="home"),
    path('profile/',user_profile, name="profile"),
    path('edit/<int:id>',edit_profile, name="edit"),
    path('delete/<int:id>',delete_post, name="delete"),
]