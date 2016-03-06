__author__ = 'mohammad'

from AdminManager.dateManager import ShamsiToMiladi, MiladiToShamsi

from django import template

import datetime


register = template.Library()

@register.filter()
def convert_to_shamsi(value):
    miladi_date = {'year':value.year, 'month':value.month, 'day':value.day}
    shamsi_date = MiladiToShamsi.convert_miladi_to_shamsi(miladi_date)
    return shamsi_date




@register.filter()
def convert_to_miladi(value):
    shamsi_date = {'year':value.year, 'month':value.month, 'day':value.day}
    miladi_date = ShamsiToMiladi.convert_shamsi_to_miladi(shamsi_date)
    return miladi_date





