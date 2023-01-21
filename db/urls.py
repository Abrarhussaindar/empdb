from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('emp_details/', views.emp_details, name ="emp details")
]