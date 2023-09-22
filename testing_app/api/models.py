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
    password1 = models.CharField(default="@Vidyasag1234",max_length=100)
    roll_num = models.CharField(default="",max_length=100)
    is_sac = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    phn_num = models.CharField(default="+91 000 000 0000",max_length = 17)
    profile_pic = models.ImageField(upload_to = 'uploads',default = 'static/img.png')
    file_type = models.CharField(default="0",max_length=100)
    bio = models.CharField(max_length = 400,default="@")
    sac_role = models.CharField(default="@",max_length=100)
    admin_role = models.CharField(default="@",max_length=100)
    faculty_role = models.CharField(default="@",max_length=100)
    date_of_birth = models.DateTimeField(default=timezone.now)
    high_post_count = models.IntegerField(default=0)
    high_lst_count = models.IntegerField(default=0)
    branch = models.CharField(default="@",max_length=100)
    batch = models.CharField(default="@",max_length=100)
    year = models.IntegerField(default=0)
    token = models.TextField(default="dfv",max_length=500)
    platform = models.CharField(default="android",max_length=50)
    notif_settings = models.CharField(default="111111111",max_length=100)
    notif_seen = models.BooleanField(default=True)
    notif_count = models.IntegerField(default=0)
    notif_ids = models.TextField(default="@")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)


class Notifications(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Notification_username')
    title = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    branch = models.CharField(default="@",max_length=100)
    batch = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    year = models.CharField(default="1111",max_length=100)
    img = models.FileField(upload_to = 'notif',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)

class Messanger(models.Model):
    message_sender = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='message_sender')
    message_receiver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='message_receiver')
    message_body = models.TextField(default="")
    message_file = models.FileField(upload_to = 'messanger',default = 'static/img.png')
    messag_file_type = models.CharField(default="@",max_length=100)
    message_body_file = models.CharField(default="@",max_length=100)
    message_replyto = models.TextField(default="@")
    message_seen = models.BooleanField(default=False)
    message_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-message_date']

    def __str__(self):
        return str(self.message_sender)

class CalenderEvents(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderEvent_user')
    cal_event_type = models.CharField(max_length=100,default="self")
    title = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    calender_date_file = models.FileField(upload_to = 'cal_events',default = 'static/img.png')
    file_type = models.CharField(default="@",max_length=100)
    branch = models.CharField(default="@",max_length=100)
    year = models.CharField(default="@",max_length=100)
    event_date = models.DateTimeField(default=timezone.now)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)



class CalenderSub(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSub_user')
    sub_name = models.CharField(max_length=100,default="@")
    sub_id = models.CharField(max_length=100,default="@")
    all_years = models.TextField(default="@")
    num_years = models.IntegerField(default=0)
    description = models.TextField(default="@")
    posted_date = models.DateTimeField(default=timezone.now)
    tot_ratings_val = models.IntegerField(default=0)
    num_ratings = models.IntegerField(default=0)

    class Meta:
        ordering = ['-sub_name']

    def __str__(self):
        return str(self.sub_name)


class CalenderSubYears(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSubYears_user')
    sub_name = models.ForeignKey(CalenderSub,on_delete=models.CASCADE, related_name='CalenderSub')
    year_name = models.CharField(max_length=100,default="@")
    private = models.BooleanField(default=False)
    num_files = models.IntegerField(default=0)
    description = models.TextField(default="@")
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-year_name']

    def __str__(self):
        return str(self.sub_name)


class CalenderSubFiles(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSubFiles_user')
    year_id = models.ForeignKey(CalenderSubYears, on_delete=models.CASCADE, related_name='CalenderSubYears')
    description = models.TextField(default="@")
    qn_ans_file = models.FileField(upload_to = 'QnsAns',default = 'static/img.png')
    file_type = models.CharField(default="@",max_length=100)
    file_name = models.CharField(default="@",max_length=100)
    year = models.CharField(default="@",max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-file_name']

    def __str__(self):
        return str(self.year_id)


class Ratings(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Ratings_user')
    sub_name = models.ForeignKey(CalenderSub,on_delete=models.CASCADE, related_name='CalenderSub_ratings')
    description = models.TextField(default="@")
    rating = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)




class Reports(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='ReportUser')
    description = models.TextField(default="")
    report_belongs = models.CharField(max_length=100,default="student")
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.username)



class PostTable(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_table_username')
    title = models.CharField(max_length=100,default="")
    description = models.TextField(default="")
    img = models.FileField(upload_to = 'posts',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    post_file = models.IntegerField(default = 0) #vedio or audio
    tag = models.CharField(max_length = 20,default="post")   # lost_found,suggestion,problems,trending,memes/jokes,fets/club/sport,events
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    post_hiders = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(default=timezone.now)
    Admin = models.BooleanField(default = False)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username) + ":" + str(self.post_id)

    #def delete(self):
    #    self.filefield.delete(save=False)
    #    super().delete()

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
    tag = models.CharField(max_length=50,default="lost/found")
    img = models.ImageField(upload_to = 'lost_found',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    comment_count = models.IntegerField(default=0)
    lst_hiders = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username) + ":" + str(self.lst_id)

  #  def delete(self, *args, **kwargs):
  #      self.img.delete(save=False)
  #      super().delete(*args, **kwargs)

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
    event_img = models.FileField(upload_to = 'events',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    event_vedio = models.FileField(upload_to = 'pics',default = 'static/img.png')
    vedio_ratio = models.FloatField(default = 1.00)
    event_updates = models.TextField(default="updates")
    is_like = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)
    event_date = models.DateTimeField(default="2023-06-30T08:23:17Z")
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
    img = models.FileField(upload_to = 'alerts',default = 'static/img.png')
    img_ratio = models.FloatField(default = 0.0)
    comment_count = models.IntegerField(default=0)
    allow_branchs = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    allow_years = models.CharField(default="1111",max_length=100)
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
    img = models.FileField(upload_to = 'alerts',default = 'static/img.png')
    img_ratio = models.FloatField(default = 0.0)
    allow_branchs = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    allow_years = models.CharField(default="1111",max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.alert_id)


class Clubs_Sports(models.Model):
    logo = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
    title = models.CharField(max_length=50,default="")
    club_r_sport = models.CharField(max_length=50,default="")
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Club_sports_user')
    head = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Club_sports_head')
    team_members = models.TextField(default="")
    description = models.TextField(default = '')
    websites = models.CharField(max_length=100,default = '')
    sport_ground = models.TextField(default="")
    sport_ground_img = models.ImageField(upload_to = 'club_sports',default = 'static/img.png')
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
    branch_tb_img = models.ImageField(upload_to = 'time_table',default = 'static/img.png')  #
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
