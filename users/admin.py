from django.contrib import admin
from .models import Profile, CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','bio',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('bio',)
