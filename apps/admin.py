from django.contrib import admin
from django.contrib.auth.models import User

from apps.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
