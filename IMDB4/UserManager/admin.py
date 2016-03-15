from .models import UserIMDB, WatchList

from django.contrib import admin



class WatchListInline(admin.TabularInline):
    model = WatchList
    extra = 1

class UserIMDBAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('-name',)
    inlines = [WatchListInline, ]





admin.site.register(UserIMDB,UserIMDBAdmin)






