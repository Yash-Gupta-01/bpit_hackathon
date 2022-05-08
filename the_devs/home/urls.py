from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    path('',views.index,name='index'),
    path('all-volunteers/',views.volunteers,name='volunteers'),
    path('become-volunteer/',views.become_volunteer,name='become_volunteer'),
    path('search/',views.search,name='search'),

]