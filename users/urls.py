from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (RegisterView, ProfileView, generate_new_psw,
                         UserConfirmEmailView, EmailConfirmView, RegisterFailView, RegisterSuccessView)

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('generate_new_psw/', generate_new_psw, name='generate_new_psw'),
    path('confirm_register/', EmailConfirmView.as_view(), name='confirm_register'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('registration_failed/', RegisterFailView.as_view(), name='registration_failed'),
    path('registration_succeeded/', RegisterSuccessView.as_view(), name='registration_succeeded'),
]
