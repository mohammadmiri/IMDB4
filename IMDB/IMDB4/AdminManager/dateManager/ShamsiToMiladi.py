
# import datetime.date
from datetime import date


def convert_shamsi_to_miladi(shamsiDate):
    totalDayInShamsi = (shamsiDate['year']-1)*365 + month_convert_to_day(shamsiDate['month']) + shamsiDate['day'] + \
                       count_day_of_leapYear(shamsiDate['year'])
    print(str(totalDayInShamsi))
    totalDayInMiladi = totalDayInShamsi + 226899
    miladiDate = count_year_month_day_according_to_totalDay(totalDayInMiladi)
    return date(miladiDate['year'], miladiDate['month'], miladiDate['day'])


def count_day_of_leapYear(numOfYear):
    return int((numOfYear)/4)

def count_year_month_day_according_to_totalDay(numOfDay):
    numOfYear = int(numOfDay/365)
    numOfLeap = int((numOfYear-1)/4)
    days = numOfDay%365
    while numOfLeap > days:
        days += 365
        numOfYear -= 1
    days -= numOfLeap
    numOfYear += 1
    isLeap = False
    if (numOfYear - 2004)%4 == 0:
        isLeap = True
    print('is leap: '+str(isLeap)+" year: "+str(numOfYear)+" days: "+str(days))
    monthAndDay = count_month_according_to_dayMiladi(days, isLeap)
    dict = {'year':numOfYear, 'month':monthAndDay['month'], 'day':monthAndDay['day']}
    year = dict['year']
    month = dict['month']
    day = dict['day']
    print(""+str(type(year))+" "+str(type(month))+" "+str(type(day)))
    return dict


def count_month_according_to_dayMiladi(numOfDay, isLeap):
    numOfMonth = 1
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if isLeap == True:
        if numOfDay > 29:
            numOfMonth += 1
            numOfDay -= 29
        else: return {'month':numOfMonth, 'day':numOfDay}
    else:
        if numOfDay > 28:
            numOfMonth += 1
            numOfDay -= 28
        else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 30:
        numOfMonth += 1
        numOfDay -= 30
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 30:
        numOfMonth += 1
        numOfDay -= 30
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 30:
        numOfMonth += 1
        numOfDay -= 30
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 31:
        numOfMonth += 1
        numOfDay -= 31
    else: return {'month':numOfMonth, 'day':numOfDay}
    if numOfDay > 30:
        numOfMonth += 1
        numOfDay -= 30
    else: return {'month':numOfMonth, 'day':numOfDay}
    return {'month':numOfMonth, 'day':numOfDay}

def month_convert_to_day(numOfMonth):
    if numOfMonth == 1:
        return 0
    elif numOfMonth == 2:
        return 31
    elif numOfMonth == 3:
        return 31*2
    elif numOfMonth == 4:
        return 31*3
    elif numOfMonth == 5:
        return 31*4
    elif numOfMonth == 6:
        return 31*5
    elif numOfMonth == 7:
        return 31*6
    elif numOfMonth == 8:
        return 31*6 + 30
    elif numOfMonth == 9:
        return 31*6 + 30*2
    elif numOfMonth == 10:
        return 31*6 + 30*3
    elif numOfMonth == 11:
        return 31*6 + 30*4
    elif numOfMonth == 12:
        return 31*6 + 30*5
    return

