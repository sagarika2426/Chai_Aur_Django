from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1_home , name='app1_home'),

]