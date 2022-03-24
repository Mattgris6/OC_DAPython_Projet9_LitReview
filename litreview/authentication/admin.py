from django.contrib import admin

from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = (['username'])
    list_filter = (['username'])
    search_fields = ['username']


admin.site.register(User, UserAdmin)
