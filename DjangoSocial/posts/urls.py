from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
   
   path('createpost/',create_post,name="createpost"),
   path('likes/<int:post_id>/',post_like,name="post_like"),
   path('comment/<int:post_id>/', add_comment, name='add_comment'),
]