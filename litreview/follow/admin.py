from django.contrib import admin

from follow.models import UserFollows


class UserFollowsAdmin(admin.ModelAdmin):
    # list display
    list_display = ['user', 'followed_user']
    # list Filter
    list_filter = ['user', 'followed_user']
    # search list
    search_fields = ['user', 'followed_user']


admin.site.register(UserFollows, UserFollowsAdmin)
