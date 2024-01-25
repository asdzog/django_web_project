from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserLogin(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')


class UserLogout(LogoutView):
    model = User
    success_url = reverse_lazy('catalog:home')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        token = default_token_generator.make_token(new_user)
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = '127.0.0.1:8000'
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрировались в магазине "On-line Shop".'
                    'Для подтверждения почтового адреса пройдите по следующей ссылке:\n'
                    f'http://{current_site}{activation_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return redirect('users:confirm_register')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.email_verified = True
            user.save()
            login(request, user)
            return redirect('users:registration_succeeded')
        else:
            return redirect('users:registration_failed')


class EmailConfirmView(TemplateView):
    template_name = 'users/confirm_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Verify code sent'
        return context


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_psw(request):
    new_password = User.objects.make_random_password()
    send_mail(
        subject='Вы успешно сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))


class RegisterFailView(View):
    template_name = 'users/registration_failed.html'


class RegisterSuccessView(TemplateView):
    template_name = 'users/registration_succeeded.html'
