from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
import uuid





class SAC_MEMS(models.Model):
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='SAC_MEMS_head')
    logo = models.ImageField(upload_to = 'pg',default = 'static/img.png') #club_sports
    img_ratio = models.FloatField(default = 1.00)
    role = models.CharField(max_length=100,default="")
    description = models.TextField(default = '')
    phone_num = models.CharField(max_length=15,default="")
    email = models.CharField(max_length=50,default="")
    domain = models.TextField(default="@nitc.ac.in")
    star_mark = models.IntegerField(default=0)
    date_of_join = models.DateTimeField(default=datetime.now)

    post_count = models.IntegerField(default=0)
    thread_count = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)


    class Meta:
        ordering = ['-date_of_join']

    def __str__(self):
        return str(self.role)



class AllClubs(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'pg',default = 'static/img.png') #club_sports
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllClubs_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    date_of_join = models.DateTimeField(default=datetime.now)
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    domain = models.TextField(default="@nitc.ac.in")
    star_mark = models.IntegerField(default=0)

    post_count = models.IntegerField(default=0)
    thread_count = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)

class Clubs_likes(models.Model):
    club = models.ForeignKey(AllClubs,on_delete=models.CASCADE,related_name='AllClubs_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllClubs_like')
    posted_date = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)


class AllSports(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'pg',default = 'static/img.png')#club_sports
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllSports_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    sport_ground = models.TextField(default="")
    sport_ground_img = models.ImageField(upload_to = 'pg',default = 'static/img.png')#club_sports
    img_ratio = models.FloatField(default = 1.00)
    date_of_join = models.DateTimeField(default=datetime.now)
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    domain = models.TextField(default="@nitc.ac.in")
    star_mark = models.IntegerField(default=0)

    post_count = models.IntegerField(default=0)
    thread_count = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)

class Sports_likes(models.Model):
    sport = models.ForeignKey(AllSports,on_delete=models.CASCADE,related_name='AllSports_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllSports_like')
    posted_date = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)


class AllFests(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'pg',default = 'static/img.png')#club_sports
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllFests_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    date_of_join = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")
    star_mark = models.IntegerField(default=0)

    post_count = models.IntegerField(default=0)
    thread_count = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)



class Fests_likes(models.Model):
    fest = models.ForeignKey(AllFests,on_delete=models.CASCADE,related_name='AllFests_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllFests_like')
    posted_date = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)





class Notifications(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Notification_username')
    title = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    branch = models.CharField(default="@",max_length=100)
    onlyUsername = models.BooleanField(default=False)
    batch = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    year = models.CharField(default="11111",max_length=100)
    course = models.CharField(default="B.Tech@M.Tech@PG@Phd@MBA@Other@B.Arch",max_length=100)
    img = models.FileField(upload_to = 'pg',default = 'static/img.png')#notif
    img_ratio = models.FloatField(default = 1.00)
    posted_date = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)




class Reports(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='ReportUser',blank=True,null=True)
    description = models.TextField(default="")
    report_belongs = models.CharField(max_length=100,default="student")
    posted_date = models.DateTimeField(default=datetime.now)
    domain = models.TextField(default="@nitc.ac.in")

    def __str__(self):
        return str(self.username)


class DatingUser(models.Model):
    dummyUserUuid =  models.UUIDField(default=uuid.uuid4)
    dummyName = models.CharField(max_length=100,default="student")
    dummyProfile = models.FileField(upload_to = 'pg',default = 'static/img.png')#Dating
    dummyBio = models.TextField(default="")
    dummyDomain = models.TextField(default="@nitc.ac.in")
    connections_count = models.IntegerField(default=0)
    Reactions1_count = models.IntegerField(default=0)
    Reactions2_count = models.IntegerField(default=0)
    is_reaction = models.IntegerField(default=0)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='DatingUser',blank=True,null=True)
    domain = models.TextField(default="@nitc.ac.in")
    numChats = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default = datetime.now())

    algoValue = models.FloatField(default = 1.00)



    class Meta:
        ordering = ['-algoValue']

    def __str__(self):
        return str(self.username)


class DatingUserReactions(models.Model):
    DatingUser = models.ForeignKey(DatingUser,on_delete=models.CASCADE, related_name='DatingUserReactions',blank=True,null=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='DatingUserReactions',blank=True,null=True)
    Reaction = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)














