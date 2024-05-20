from urllib import request

from django.views.generic import CreateView, DetailView

from apps.forms import RegisterFormModel
from apps.models import Profile


class ProfileDetailView(DetailView):
    is_authenticated = True
    queryset = Profile.objects.all()
    template_name = 'detail.html'
    context_object_name = 'profiles'


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterFormModel
    success_url = 'login'
