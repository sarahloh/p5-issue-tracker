from django.urls import path
from tickets import views


urlpatterns = [
    path('', views.get_issues, name='index'),
]
