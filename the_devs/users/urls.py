from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from ratelimit import limits

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', limits(calls=50, period=86400)(auth_view.LoginView.as_view(template_name='users/login.html')), name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    #path('become-volunteer/', views.become_volunteer, name='become_volunteer'),  # Add this line
]