from django.urls import path, re_path
from tickets import views


urlpatterns = [
    path('', views.all_tickets, name='index'),
    re_path(r'^(?P<pk>\d+)/$', views.get_ticket, name='get_ticket'),
    path('new/', views.create_or_edit_ticket, name='new_ticket'),
    re_path(r'^(?P<pk>\d+)/edit/$', views.create_or_edit_ticket, name='edit_ticket'),
]
