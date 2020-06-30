from django.contrib import admin
from .models import Profile
from friendship.models import Friend, Follow, Block

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'blood_group', 'status']
	list_filter = ['status']

# @admin.register(Friend)
# class FriendAdmin(admin.ModelAdmin):
# 	list_display = []