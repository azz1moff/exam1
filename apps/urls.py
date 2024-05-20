from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import path

from apps.views import ProfileDetailView, RegisterView


def send_mail_view(request):
    subject = 'Welcome to My Site'
    message = f'Thank u for creating an account!{request.user.id}'
    recipient_list = [request.user.email]
    send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
    return HttpResponse('Successfully sent email!')


urlpatterns = [
    path('profile/<pk>', ProfileDetailView.as_view(), name='detail_page'),
    path('send', send_mail_view,name='send_page'),
    path('login', LoginView.as_view(
        template_name='login.html',
        next_page='send_page',
        redirect_authenticated_user=True,
    ), name='detail_page'),
    path('register', RegisterView.as_view(), name='register_page'),
]
