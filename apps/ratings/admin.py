from django.contrib import admin
from .models import Rating
# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater',  'agent',   'rating',  'comment', ]
    # list_display_links = ['id', 'user']
    # list_filter = ['user',   'rating', 'comment', ]

admin.site.register(Rating, RatingAdmin)