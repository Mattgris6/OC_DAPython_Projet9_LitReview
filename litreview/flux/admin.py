from django.contrib import admin

from flux.models import *


class TicketAdmin(admin.ModelAdmin):
    #list display
    list_display = ['title', 'user', 'time_created']
    #list Filter
    list_filter = ['title', 'user', 'time_created']
    # search list
    search_fields = ['title', 'user', 'time_created']


class ReviewAdmin(admin.ModelAdmin):
    #list display
    list_display = ['ticket', 'user', 'headline', 'time_created']
    #list Filter
    list_filter = ['ticket', 'user', 'headline', 'time_created']
    # search list
    search_fields = ['ticket', 'user', 'headline', 'time_created']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)