__author__ = 'mohammad'


from django import template



register = template.Library()

@register.filter
def IntegerToPersian(number):
    if number is None:
        return None
    if number==0:
        return '۰'
    persian_number = ''
    while(number>=1):
        digit = number%10
        persian_number = toPersianDigit(digit)+persian_number
        number = int(number/10)
    return persian_number



@register.filter
def FloatToPersian(number):
    if number is None:
        return None
    if (type(number) is int):
        return IntegerToPersian(number)
    numbers = str(number).split('.')
    integer_number = IntegerToPersian(int(numbers[0]))
    float_number = IntegerToPersian(int(numbers[1]))
    return integer_number+'.'+float_number



def toPersianDigit(digit):
    if digit is None:
        return None
    if digit==1:
        return '۱'
    if digit==2:
        return '۲'
    if digit==3:
        return '۳'
    if digit==4:
        return '۴'
    if digit==5:
        return '۵'
    if digit==6:
        return '۶'
    if digit==7:
        return '۷'
    if digit==8:
        return '۸'
    if digit==9:
        return '۹'
    if digit==0:
        return '۰'





@register.filter()
def roleToPersian(role):
    if role is None:
        return None
    if role == 'kargardan':
        return 'کارگردان'
    if role == 'nevisande':
        return 'نویسنده'
    if role == 'tahiey_konande':
        return 'تهیه کننده'
    if role == 'modir_tolid':
        return 'مدیر تولید'
    if role == 'mojri_tarh':
        return 'مجری طرح'
    if role == 'dastyar_aval_kargardan':
        return 'دستیار اول کارگردان'
    if role == 'barname_riz':
        return 'برنامه ریز'
    if role == 'modir_film_bardari':
        return 'مدیر فیلم برداری'
    if role == 'tadvin':
        return 'تدوین'
    if role == 'tarrah_sahne_va_lebas':
        return 'طراح صحنه و لباس'
    if role == 'tarrah_chehre_pardazi':
        return 'طراح چهره پردازی'
    if role == 'ahangsaz':
        return 'آهنگ ساز'
    if role == 'seda_bardari':
        return 'صدا بردار'
    if role == 'seda_Gozari_va_mix':
        return 'صدا گذار و میکس'
    if role == 'akkas':
        return 'عکاس'
    if role == 'jelvehaye_vije_meydani':
        return 'جلوه های ویژه میدانی'
    if role == 'jelvehaye_vije_basari':
        return 'جلوه های ویژه بصری'
    if role == 'monshi_sahne':
        return 'منشی صحنه'
    if role == 'moshaver_film_name':
        return 'مشاور فیلم نامه'
    if role == 'moshaver_honari':
        return 'مشاور هنری'
    if role == 'moshaver':
        return 'مشاور'



def GenreToPersian(genre):
    if genre is None:
        return None
    if genre == 'action':
        return 'حادثه ای'
    if genre == 'animation':
        return 'انیمیشن'
    if genre == 'biography':
        return 'بیوگرافی'
    if genre == 'comedy':
        return 'کمدی'
    if genre == 'romantic':
        return 'عاشقانه'
    if genre == 'science_fiction':
        return 'علمی تخیلی'
    if genre == 'short':
        return 'کوتاه'
    if genre == 'trailer':
        return 'تریلر'
    if genre == 'fantasy':
        return 'فانتزی'
    if genre == 'historical':
        return 'تاریخی'
    if genre == 'horror':
        return 'ترسناک'
    if genre == 'musical':
        return 'موزیکال'
    if genre == 'criminal':
        return 'جنایی'
    if genre == 'documentary':
        return 'مستند'
    if genre == 'dram':
        return 'درام'
    if genre == 'military':
        return 'جنگی'
    if genre == 'social':
        return 'اجتماعی'

@register.filter
def NewsCategoryToPersian(category):
    if category == "TV":
        return "تلویزیون"
    if category == "iran_cinema":
        return "سینمای ایران"
    if category == "world_cinema":
        return "سینمای جهان"
    if category == "honarmandan":
        return "هنرمندان"