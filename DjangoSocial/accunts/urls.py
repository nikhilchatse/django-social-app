from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('resetpass/',views.reset_pass,name="resetpass"),
    #forget pass path
    path('forgetPass',views.forgetPass,name='forgetPass'),
    path('forgetreset/<int:id>',views.resetforget,name='forgetreset'),
]
