

from django.forms import widgets
from django import template

register=template.Library()






@register.filter()
def klass(instance):
    if(type(instance) is widgets.CheckboxInput):
        return True
    else:
        return False






