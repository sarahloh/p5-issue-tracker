from django.urls import path, include
from accounts import views
from accounts import url_reset

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('register/', views.registration, name="registration"),
    path('profile/', views.user_profile, name="profile"),
    path('password_reset/', include(url_reset)),
]
