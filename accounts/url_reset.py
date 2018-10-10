from django.urls import path, re_path, reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.PasswordResetView.as_view(success_url= reverse_lazy('password_reset_done')), name='password_reset'),
    path('done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path('(?P<uidb64>[0-9A-Za-z]+)-(?P<token>).+/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('post_reset_confirm')), name='password_reset_confirm'),
    path('complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete')
]
