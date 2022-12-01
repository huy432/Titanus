from django.contrib import admin

# Register your models here.
from .models import UserProfile
# Register your models here.ư
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(UserProfile, UserProfileAdmin)