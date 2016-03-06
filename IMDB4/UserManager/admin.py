from .models import  UserIMDB

from django.contrib import admin






class UserIMDBAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('-name',)





admin.site.register(UserIMDB,UserIMDBAdmin)






