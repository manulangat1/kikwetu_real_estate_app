from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pkid', 'id', 'user',   'phone_number',  'country', ]
    list_display_links = ['id', 'user']
    list_filter = ['user',   'phone_number', 'country', ]

admin.site.register(Profile, ProfileAdmin)
