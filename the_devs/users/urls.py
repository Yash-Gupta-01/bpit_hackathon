from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('login/',auth_view.LoginView.as_view(),name='login'),
    path('contact/',views.contact,name='contact')

]