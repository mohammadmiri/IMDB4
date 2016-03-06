from .models import News, Poll, PollOption, Gallery

from django.contrib import admin


class PollOption(admin.TabularInline):
    model = PollOption
    extra = 1

class PollAdmin(admin.ModelAdmin):
    inlines = [PollOption]


admin.site.register(News)
admin.site.register(Poll, PollAdmin)
admin.site.register(Gallery)

