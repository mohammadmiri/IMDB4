__author__ = 'mohammad'

from AdminManager.dateManager import ShamsiToMiladi, MiladiToShamsi
from AdminManager.templatetags import toPersian

from django import template

import datetime



register = template.Library()

@register.filter()
def convert_to_shamsi(value):
    if value is None:
        return None
    miladi_date = {'year':value.year, 'month':value.month, 'day':value.day}
    shamsi_date = MiladiToShamsi.convert_miladi_to_shamsi(miladi_date)
    return shamsi_date



@register.filter()
def convert_to_miladi(value):
    if value is None:
        return None
    shamsi_date = {'year':value.year, 'month':value.month, 'day':value.day}
    miladi_date = ShamsiToMiladi.convert_shamsi_to_miladi(shamsi_date)
    return miladi_date


@register.filter()
def get_month(date):
    if date is None:
        return None
    return date['month']

@register.filter()
def get_year(date):
    if date is None:
        return None
    return date['year']

@register.filter()
def get_day(date):
    if date is None:
        return None
    return date['day']


@register.filter()
def get_diff_date(date):
    if date is None:
        return None
    diff_day = get_diff_day(datetime.datetime.now() , date)
    if diff_day == 0:
        diff_hour = datetime.datetime.now().hour - date.hour
        if diff_hour < 0:
            return toPersian.IntegerToPersian(diff_hour+24)+' ساعت '
        if diff_hour > 0:
            return toPersian.IntegerToPersian(diff_hour)+' ساعت '
        if diff_hour == 0:
            diff_minute = datetime.datetime.now().minute - date.minute
            if diff_minute < 0:
                return toPersian.IntegerToPersian(diff_minute+60)+' دقیقه '
            else:
                return toPersian.IntegerToPersian(diff_minute)+'دقیقه '
    else:
        return toPersian.IntegerToPersian(diff_day) + ' روز '


# date1 should be earlier than date2
def get_diff_day(date1:datetime.datetime, date2:datetime.datetime):
    days = 30*(date1.month - date2.month)
    days += (date1.day - date2.day)
    return days

