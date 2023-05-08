from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import uuid


#workon testing


class User(AbstractUser):
    email = models.CharField(default="",max_length=100,unique = True)
    username = models.CharField(default="-",max_length=100,unique = True)
    roll_num = models.CharField(default="",max_length=100)
    is_sac = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phn_num = models.CharField(default="+91 0000 000 000",max_length=100)
    profile_pic = models.ImageField(upload_to = 'pics',default = 'static/img.png')
    bio = models.CharField(max_length = 400,default="@")
    sac_role = models.CharField(default="@",max_length=100)
    admin_role = models.CharField(default="@",max_length=100)
    date_of_birth = models.DateTimeField(default=timezone.now)
    high_post_count = models.IntegerField(default=0)
    high_lst_count = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)




class PostTable(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_table_username')
    title = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    img = models.FileField(upload_to = 'pics',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    profile_pic = models.ImageField(upload_to = 'pics',default = 'static/img.png')
    post_file = models.IntegerField(default = 0) #vedio or audio
    tag = models.CharField(max_length = 20,default="post")   # lost_found,suggestion,problems,trending,memes/jokes,fets/club/sport,events
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(default=timezone.now)
    Admin = models.BooleanField(default = False)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username) + ":" + str(self.post_id)

class post_Likes(models.Model):
    post_id = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='post_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_like_username')
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.post_id)

class post_Comments(models.Model):
    post_id = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='post_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_comment_username')
    Comment = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.post_id)


class Lost_Found(models.Model):
    lst_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='lst_found_username')
    title = models.CharField(max_length=50,default="")
    description = models.TextField(default="")
    img = models.ImageField(upload_to = 'pics',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    comment_count = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username) + ":" + str(self.lst_id)

class LST_Comments(models.Model):
    lst_id = models.UUIDField(default=uuid.uuid4, editable=False)
    lst_cmnt_id = models.ForeignKey(Lost_Found, on_delete=models.CASCADE, related_name='lst_found_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='lst_cmnt_username',default="")
    Comment = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.lst_id)


class Events(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='events_username')
    title = models.CharField(max_length=50,default="")
    description = models.TextField(default="")
    event_img = models.FileField(upload_to = 'pics',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    event_vedio = models.FileField(upload_to = 'pics',default = 'static/img.png')
    vedio_ratio = models.FloatField(default = 1.00)
    event_updates = models.TextField(default="")
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.event_id)


class Event_likes(models.Model):
    event_id = models.ForeignKey(Events,on_delete=models.CASCADE,related_name='event_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='event_like')
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.event_id)

class Alerts(models.Model):
    alert_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='alerts_username')
    title = models.CharField(max_length=50,default="")
    description = models.TextField(default="")
    img = models.FileField(upload_to = 'pics',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    comment_count = models.IntegerField(default=0)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.alert_id)

class ALERT_Comments(models.Model):
    alert_id = models.UUIDField(default=uuid.uuid4, editable=False)
    alert_cmnt_id = models.ForeignKey(Alerts, on_delete=models.CASCADE, related_name='alert_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='alert_cmnt_username',default="")
    Comment = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.alert_id)


class Clubs_Sports(models.Model):
    logo = models.ImageField(upload_to = 'pics',default = 'static/img.png')
    title = models.CharField(max_length=50,default="")
    club_r_sport = models.CharField(max_length=50,default="")
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Club_sports_user')
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Club_sports_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    sport_ground = models.TextField(default="")
    sport_ground_img = models.ImageField(upload_to = 'pics',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    date_of_join = models.DateTimeField(default=timezone.now)
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-like_count','-date_of_join']

    def __str__(self):
        return str(self.username)



class Clubs_Sports_likes(models.Model):
    club_sport = models.ForeignKey(Clubs_Sports,on_delete=models.CASCADE,related_name='club_sport_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='club_sport_like')
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.club_sport)


class Mess_table(models.Model):
    hostel = models.CharField(max_length=50,default="")
    sun = models.TextField(default = '')
    mon = models.TextField(default = '')
    tue = models.TextField(default = '')
    wed = models.TextField(default = '')
    thu = models.TextField(default = '')
    fri = models.TextField(default = '')
    sat = models.TextField(default = '')

    class Meta:
        ordering = ['-hostel']

    def __str__(self):
        return str(self.hostel)


class Academic_table(models.Model):
    academic_name = models.CharField(max_length=50,default="")
    sun = models.TextField(default = '')
    mon = models.TextField(default = '')
    tue = models.TextField(default = '')
    wed = models.TextField(default = '')
    thu = models.TextField(default = '')
    fri = models.TextField(default = '')
    sat = models.TextField(default = '')

    def __str__(self):
        return str(self.academic_name)

class Time_table(models.Model):
    branch_name = models.CharField(max_length=50,default="")
    branch_tb_img = models.ImageField(upload_to = 'pics',default = 'static/img.png')  #
    img_ratio = models.FloatField(default = 1.00)
    sun = models.TextField(default = '')
    mon = models.TextField(default = '')
    tue = models.TextField(default = '')
    wed = models.TextField(default = '')
    thu = models.TextField(default = '')
    fri = models.TextField(default = '')
    sat = models.TextField(default = '')

    def __str__(self):
        return str(self.branch_name)
    
 


























#class Alerts_Comments(models.Model):
#    alert_id = models.ForeignKey(Alerts,on_delete=models.CASCADE,related_name='alert_comment_id')
#    e_mail = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='alert_comments_email')
#    comment = models.CharField(default="",max_length=100)
#    posted_date = models.DateTimeField(default=timezone.now)
    
#    class Meta:
#        ordering = ['-posted_date']
    
#    def __str__(self):
#        return str(self.e_mail) + ":" + str(self.alert_id)
    
    

#class Clubs_Sports_files(models.Model):
#    CS_file_id = models.UUIDField(default=uuid.uuid4, editable=False)
#    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='clubs')
#    club_r_sport_name = models.ForeignKey(Clubs_Sports,on_delete=models.CASCADE, related_name='club')
#    event_date_time = models.DateTimeField(default=timezone.now)
#    title = models.CharField(max_length=50,default = '')
#    description = models.TextField(default = '')
#    image_vedio = models.FileField(upload_to = 'pics',default = 'static/img.png')
    
    
#    class Meta:
#        ordering = ['-posted_date']

#    def __str__(self):
#        return str(self.club_r_sport_name)