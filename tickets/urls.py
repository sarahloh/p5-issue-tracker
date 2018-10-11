from django.urls import path
from tickets import views


urlpatterns = [
    path('', views.all_tickets, name='index'),
]
