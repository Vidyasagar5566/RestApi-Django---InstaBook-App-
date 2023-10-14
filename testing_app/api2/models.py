from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings



class AllClubs(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllClubs_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    date_of_join = models.DateTimeField(default=timezone.now)
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)

class Clubs_likes(models.Model):
    club = models.ForeignKey(AllClubs,on_delete=models.CASCADE,related_name='AllClubs_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllClubs_like')
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)


class AllSports(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllSports_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    sport_ground = models.TextField(default="")
    sport_ground_img = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    date_of_join = models.DateTimeField(default=timezone.now)
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)

class Sports_likes(models.Model):
    sport = models.ForeignKey(AllSports,on_delete=models.CASCADE,related_name='AllSports_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllSports_like')
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)


class AllFests(models.Model):
    name = models.CharField(max_length=50,default="")
    logo = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
    title = models.CharField(max_length=50,default="")
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllFests_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    sport_ground = models.TextField(default="")
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    date_of_join = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.name)



class Fests_likes(models.Model):
    fest = models.ForeignKey(AllFests,on_delete=models.CASCADE,related_name='AllFests_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='AllFests_like')
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)





