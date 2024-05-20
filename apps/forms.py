from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterFormModel(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean_password(self):
        return make_password(self.cleaned_data['password'])
