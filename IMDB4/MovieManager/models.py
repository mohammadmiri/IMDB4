# -*- coding: utf-8 -*-

from CelebrityManager.models import Celebrity
from UserManager.models import UserIMDB,  User

from django.db import models
from django.db.models import Avg
from ckeditor.fields import RichTextField


class Genre(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name



class KeyWord(models.Model):
    word = models.CharField(max_length=80)

    def __str__(self):
        return self.word



class Movie(models.Model):
    poster = models.ImageField(upload_to='posters', null=True, blank=True, verbose_name='پوستر', )
    name = models.TextField( null=True, blank=True, verbose_name='نام', )
    year = models.CharField(max_length=10, null=True, blank=True, verbose_name='سال تولید', )
    duration = models.IntegerField(null=True, blank=True, verbose_name='مدت زمان', )
    rate = models.FloatField(null=True, blank=True, verbose_name='امتیاز', )
    numUserRated = models.IntegerField(null=True, blank=True, verbose_name='تعداد امتیاز دهندگان', )
    summary = RichTextField(null=True, blank=True, verbose_name='خلاصه فیلم', )
    sale = models.CharField(max_length=80, null=True, blank=True, verbose_name='فروش', )
    dialogue = models.TextField(null=True, blank=True,verbose_name='دیالوگ', )
    genre = models.ManyToManyField(Genre, blank=True, verbose_name='ژانر', )
    keywords = models.ManyToManyField(KeyWord,blank=True, verbose_name='کلمات کلیدی', )

    avamel = models.ManyToManyField(Celebrity, through="Avamel", related_name="movie_avamel", verbose_name='عوامل', )
    actors = models.ManyToManyField(Celebrity, through="Act", related_name="movie_actors", verbose_name='بازیگران', )
    posts = models.ManyToManyField(User, through='Post', verbose_name='پست ها', )
    awards = models.ManyToManyField(Celebrity, through='Award', verbose_name='جوایز', )

    def __str__(self):
        return self.name

    # this function set the rate number
    def set_rate_value(self):
        self.rate = RateUserForMovie.objects.filter(movie=self).aggregate(Avg('rate'))['rate_avg']

    # this function return actors with their alias names
    # return dictionary movie_actors : key -> actor , value -> act.name
    def get_actors(self):
        movie_actors={}
        actors = self.actors.all()
        acts = self.act_set.all()
        for actor in actors:
            for act in acts:
                if act.celebrity == actor:
                    movie_actors[actor] = act.alias
        return movie_actors

    #is for test and should be moved to celebrity model
    @staticmethod
    def get_movie_act(cele):
        movie_actors = {}
        movies = cele.movie_actors.all()
        acts = Act.objects.filter(celebrity=cele)
        for movie in movies:
            for act in acts:
                if act.movie == movie:
                    movie_actors[movie] = act
        return movie_actors



# images of Movie
class Movie_Celebrity_Image(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name='نام',)
    description = models.TextField(null=True, blank=True, verbose_name='توضیح',)
    movies = models.ManyToManyField(Movie, verbose_name='فیلم ها', related_name='images', blank=True)
    celebrities = models.ManyToManyField(Celebrity, verbose_name='بازیگر', related_name='images', blank=True)
    image = models.ImageField(upload_to='MovieImages', verbose_name='عکس', null=True, blank=True,)
    GALLERY_CHOISE = (
        (0,'هیچ کدام'),
        (1,'گالری ۱'),
        (2,'گالری ۲'),
        (3,'گالری ۳'),
        (4,'گالری ۴'),
    )
    galleryNumber = models.IntegerField(default=0, choices=GALLERY_CHOISE, verbose_name='گالری')
    in_homePage = models.BooleanField(default=False, verbose_name='در صفحه اصلی نشان داده شود',)



# this class should be used to determine type of movie (e.g. video-film)
class TypeOfMovie(models.Model):
    movie = models.OneToOneField(Movie, verbose_name='فیلم', related_name='type')
    type = models.TextField(null=True, blank=True, verbose_name='نوع فیلم', )



# this class should be used to represent the status of movie (e.g. pish_tolid)
class StatusOfMovie(models.Model):
    movie = models.OneToOneField(Movie, verbose_name='فیلم', related_name='status')
    StatusChoice = (
        ('pish_tolid', 'پیش تولید'),
        ('film_bardari', 'فیلم برداری'),
        ('pas_tolid', 'پس تولید'),
    )
    status = models.CharField(max_length=50, blank=True, null=True, verbose_name='وضعیت', choices=StatusChoice)



# Teaser of Movie
class Teaser(models.Model):
    movie = models.OneToOneField(Movie, related_name="teaser", null=True, blank=True, verbose_name='فیلم', )
    image = models.ImageField(upload_to='Teaser/Images', null=True, blank=True, verbose_name='عکس', )
    video_link = models.TextField(null=True, blank=True, verbose_name='لینک ویدیو', )
    date_uploaded = models.DateField(null=True, blank=True, verbose_name='تاریخ اپلود', )

    def __str__(self):
        return "teaser '{}' for movie '{}' ".format(
            self.name.__str__(), self.movie.__str__()
        )



# this class contains all property of ManyToMany relationship between awards of Movies and Celebrities
class Award(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='فیلم', )
    celebrity = models.ForeignKey(Celebrity, verbose_name='بازیگر', )
    category = models.TextField(null=True, blank=True, verbose_name='نوع جایزه', )
    FestivalChoices = (
        (0,'جشنواره فجر'),
        (1,'جشن خانه سینما'),
        (2,'جشن منتقدان سینما'),
    )
    festival = models.IntegerField(choices=FestivalChoices, null=True, blank=True, verbose_name='جشنواره', )
    date = models.DateField(null=True, blank=True, verbose_name='تاریخ', )
    type = models.CharField(max_length=150, null=True, blank=True,verbose_name='نوع بخش', )
    GIVEN_CHOICES = (
        (0,'برنده شده'),
        (1,'نامزد شده'),
        (2, 'دیپلم افتخار')
    )
    candidate_type = models.IntegerField(null=True, blank=True, choices=GIVEN_CHOICES, verbose_name='برنده یا نامزد',)

    @staticmethod
    def get_festival_award_count(cele, festival, candidate_type):
        Award.objects.filter(celebrity=cele, festival=festival, candidate_type=candidate_type).count()

    @staticmethod
    def get_award_count(cele, candidate_type):
        Award.objects.filter(celebrity=cele, candidate_type=candidate_type)




# this class contains all property of ManyToMany relationship between Movies and Posts of users
class Post(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='پست', )
    user = models.ForeignKey(User, verbose_name='کاربر', )
    content = models.TextField(blank=True, verbose_name='متن', )
    date = models.DateField( verbose_name='تاریخ', )
    show_it = models.BooleanField(default=False, verbose_name='نشان داده شود', )

    def __str__(self):
        return "user '{}' posted for movie '{}'".format(
            self.user.__str__(), self.movie.__str__()
        )



# this class contains all property of ManyToMany relationship between Movies and Celebrities as actors
class Act(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='فیلم', )
    celebrity = models.ForeignKey(Celebrity, verbose_name='بازیگر', )
    alias = models.CharField(max_length=100, verbose_name='نقش در فیلم', )
    asli_ast = models.BooleanField(default=False, verbose_name='جز بازیگران اصلی است', )

    def __str__(self):
        return "person '{}' acts in movie '{}' as '{}'".format(
            self.celebrity.__str__(), self.movie.__str__(), self.alias.__str__()
        )



# this class contains all property of ManyToMany relationship between Movies and Celebrities as Avamels
class Avamel(models.Model):

    ROLE_CHOICE = (
        ('kargardan', 'کارگردان'),
        ('nevisande', 'نویسنده'),
        ('tahiey_konande', 'تهیه کننده'),
        ('modir_tolid', 'مدیر تولید'),
        ('mojri_tarh', 'مدیر طرح'),
        ('dastyar_aval_kargardan', 'دستیار اول کارگردان'),
        ('barname_riz', 'برنامه ریز'),
        ('modir_film_bardari', 'مدیر فیلم برداری'),
        ('tadvin', 'تدوین'),
        ('tarrah_sahne_va_lebas', 'طراح صحنه و لباس'),
        ('tarrah_chehre_pardazi', 'طراح چهره پردازی'),
        ('ahangsaz', 'آهنگساز'),
        ('seda_bardari', 'صدا بردار'),
        ('seda_Gozari_va_mix', 'صدا گذار'),
        ('akkas', 'عکاس'),
        ('jelvehaye_vije_meydani', 'جلوه های ویژه'),
        ('jelvehaye_vije_basari', 'جلوه های بصری'),
        ('monshi_sahne', 'منشی صحنه'),
        ('moshaver_film_name', 'مشاور فیلم نامه'),
        ('moshaver_honari', 'مشاور هنری'),
        ('moshaver', 'مشاور'),
    )

    movie = models.ForeignKey(Movie, related_query_name="agent", null=True, blank=True, verbose_name='فیلم')
    celebrity = models.ForeignKey(Celebrity, related_query_name="agent", null=True, blank=True, verbose_name='بازیگر')
    role = models.CharField(max_length=40, null=True, blank=True, choices=ROLE_CHOICE, verbose_name='کار اجرایی')

    def __str__(self):
        return "person '{}' in movie '{}' as '{}'".format(
            self.cele.__str__(), self.movie.__str__(), self.ROLE_CHOICE[self.role][1]
        )


# this class contains all property of ManyToMany relationship between Movies and Users
class User_Review(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='فیلم', )
    userPro = models.ForeignKey(UserIMDB, null=True, verbose_name='کاربر', )
    content = models.TextField(verbose_name='متن', )
    show_it = models.BooleanField(default=False, verbose_name='نشان داده بشود', )
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "user '{}' criticize movie '{}'".format(
            self.userPro.__str__(), self.movie.__str__()
        )


# this class contains all criticisms of all critics about this film
class Reviewer_Review(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='فیلم')
    content = models.TextField(null=True, blank=True, verbose_name='متن', )
    nameOfCritic = models.CharField(max_length=80, null=True, blank=True, verbose_name='نام منتقد')
    like = models.FloatField(null=True, blank=True, )
    show_it = models.BooleanField(default=False, verbose_name='نشان داده شود', )

    def __str__(self):
        return "critic '{}' criticize movie '{}'".format(
            self.nameOfCritic.__str__(), self.movie.__str__()
        )


# this class should be used to represent the rate of each user to each film
class RateUserForMovie(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='فیلم', )
    user = models.ForeignKey(User, verbose_name='کاربر', )
    rate = models.IntegerField(verbose_name='امتیاز', )

    def __str__(self):
        return "user '{}' rated '{}' to movie '{}'".format(
            self.user.__str__(), self.rate.__str__(), self.movie.__str__()
        )






