from .models import Celebrity
from UserManager.models import PostForCelebrity


from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from datetime import date



class PostOFUserInline(admin.TabularInline):
    model = PostForCelebrity
    extra = 1



class AgeFilter(admin.SimpleListFilter):

    title = _('decade born')
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            ('10s', _('in the 10s')),
            ('20s', _('in the 20s')),
            ('30s', _('in the 30s')),
            ('40s', _('in the 40s')),
            ('50s', _('in the 50s')),
            ('60s', _('in the 60s')),
            ('70s', _('in the 70s')),
            ('80s', _('in the 80s')),
            ('90s', _('in the 90s')),
            ('earlier', _('earlier than 2000'))
        )

    def queryset(self, request, queryset):
        if self.value() == '10s':
            return Celebrity.objects.filter(birthday__gte=date(1910, 1, 1), birthday__lte=date(1919, 1, 1))
        if self.value() == '20s':
            return Celebrity.objects.filter(birthday__gte=date(1920, 1, 1), birthday__lte=date(1929, 1, 1))
        if self.value() == '30s':
            return Celebrity.objects.filter(birthday__gte=date(1930, 1, 1), birthday__lte=date(1939, 1, 1))
        if self.value() == '40s':
            return Celebrity.objects.filter(birthday__gte=date(1940, 1, 1), birthday__lte=date(1949, 1, 1))
        if self.value() == '50s':
            return Celebrity.objects.filter(birthday__gte=date(1950, 1, 1), birthday__lte=date(1959, 1, 1))
        if self.value() == '60s':
            return Celebrity.objects.filter(birthday__gte=date(1960, 1, 1), birthday__lte=date(1969, 1, 1))
        if self.value() == '70s':
            return Celebrity.objects.filter(birthday__gte=date(1970, 1, 1), birthday__lte=date(1979, 1, 1))
        if self.value() == '80s':
            return Celebrity.objects.filter(birthday__gte=date(1980, 1, 1), birthday__lte=date(1989, 1, 1))
        if self.value() == '90s':
            return Celebrity.objects.filter(birthday__gte=date(1990, 1, 1), birthday__lte=date(1999, 1, 1))
        if self.value() == 'earlier':
            return Celebrity.objects.filter(birthday__gte=date(2000, 1, 1))


class CelebrityAdmin(admin.ModelAdmin):
    list_filter = (AgeFilter,)
    ordering = ('name',)
    search_fields = ['name']
    inlines = [PostOFUserInline]









admin.site.register(Celebrity, CelebrityAdmin)

