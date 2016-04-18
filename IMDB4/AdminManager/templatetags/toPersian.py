__author__ = 'mohammad'


from django import template



register = template.Library()

@register.filter
def IntegerToPersian(number):
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
    if (type(number) is int):
        return IntegerToPersian(number)
    numbers = str(number).split('.')
    integer_number = IntegerToPersian(int(numbers[0]))
    float_number = IntegerToPersian(int(numbers[1]))
    return integer_number+'.'+float_number



def toPersianDigit(digit):
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
    if role == 'movie_kargardan':
        return 'کارگردان'
    if role == 'movie_nevisande':
        return 'نویسنده'
    if role == 'movie_tahiey_konande':
        return 'تهیه کننده'
    if role == 'movie_modir_tolid':
        return 'مدیر تولید'
    if role == 'movie_mojri_tarh':
        return 'مجری طرح'
    if role == 'movie_Dastyar_aval_kargardan':
        return 'دستیار اول کارگردان'
    if role == 'movie_barname_riz':
        return 'برنامه ریز'
    if role == 'movie_modir_film_bardari':
        return 'مدیر فیلم برداری'
    if role == 'movie_tadvin':
        return 'تدوین'
    if role == 'movie_tarrah_sahne_va_lebas':
        return 'طراح صحنه و لباس'
    if role == 'movie_tarrah_chehre_pardazi':
        return 'طراح چهره پردازی'
    if role == 'movie_ahangsaz':
        return 'آهنگ ساز'
    if role == 'movie_seda_bardari':
        return 'صدا بردار'
    if role == 'movie_Seda_Gozari_va_mix':
        return 'صدا گذار و میکس'
    if role == 'movie_akkas':
        return 'عکاس'
    if role == 'movie_jelvehaye_vije_meydani':
        return 'جلوه های ویژه میدانی'
    if role == 'movie_jelvehaye_vije_basari':
        return 'جلوه های ویژه بصری'
    if role == 'movie_monshi_sahne':
        return 'منشی صحنه'
    if role == 'movie_moshaver_film_name':
        return 'مشاور فیلم نامه'
    if role == 'movie_moshaver_honari':
        return 'مشاور هنری'
    if role == 'movie_moshaver':
        return 'مشاور'



def GenreToPersian(genre:str):
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
