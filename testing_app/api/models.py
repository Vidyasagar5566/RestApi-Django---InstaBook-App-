from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from api2 import models as api2_models
#workon testing





class User(AbstractUser):
    email = models.CharField(default="",max_length=100,unique = True)
    username = models.CharField(default="-",max_length=100,unique = True)
    password1 = models.CharField(default="@Vidyasag1234",max_length=100)

    roll_num = models.CharField(default="",max_length=100)
    phn_num = models.CharField(default="+91 000 000 0000",max_length = 17)
    profile_pic = models.ImageField(upload_to = 'uploads',default = 'static/img.png')
    file_type = models.CharField(default="0",max_length=100)
    bio = models.CharField(max_length = 400,default="@")
    skills = models.JSONField(default = {'Programming_Languages': '','Projects':{},'Work_Experience':{},'Education_details':{}})
    course = models.CharField(default="B.TECH",max_length=100)
    branch = models.CharField(default="@",max_length=100)
    batch = models.CharField(default="@",max_length=100)
    year = models.IntegerField(default=0)
    date_of_birth = models.DateTimeField(default=timezone.now)

    is_instabook = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student_admin = models.BooleanField(default=False)

    instabook_role = models.CharField(default="@",max_length=100)
    faculty_role = models.CharField(default="@",max_length=100)
    admin_role = models.CharField(default="@",max_length=100)
    student_admin_role = models.CharField(default="@",max_length=100)

    clz_clubs_head = models.BooleanField(default=False)
    clz_sports_head = models.BooleanField(default=False)
    clz_fests_head = models.BooleanField(default=False)
    clz_sacs_head = models.BooleanField(default=False)
    clz_users_head = models.BooleanField(default=False)

    clz_clubs = models.JSONField(default = {'head':{},'team_member':{}})
    clz_sports = models.JSONField(default = {'head':{},'team_member':{}})
    clz_fests = models.JSONField(default = {'head':{},'team_member':{}})
    clz_sacs = models.JSONField(default = {'head':{},'team_member':{}})


    user_mark = models.CharField(default="St",max_length=100)
    star_mark = models.IntegerField(default=0)

    post_count = models.IntegerField(default=0)
    lst_count = models.IntegerField(default=0)
    notif_seen = models.BooleanField(default=True)
    notif_count = models.IntegerField(default=0)
    notif_ids = models.TextField(default="@")
    notif_settings = models.CharField(default="11111111111111111111111",max_length=100)

    token = models.TextField(default="dfv",max_length=500)
    platform = models.CharField(default="android",max_length=50)
    domain = models.CharField(default="@nitc.ac.in",max_length=100)
    is_details = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)



class PostTable(models.Model):
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
    all_universities = models.BooleanField(default = True)
    domain = models.TextField(default="@nitc.ac.in")


    post_category = models.CharField(default="student",max_length=100,choices = (('student','student'),('club','club'),('sport','sport'),('fest','fest'),('sac','sac')))
    club_post = models.ForeignKey(api2_models.AllClubs,on_delete=models.CASCADE, related_name='post_from_club',blank=True,null=True)
    sport_post = models.ForeignKey(api2_models.AllSports,on_delete=models.CASCADE, related_name='post_from_club',blank=True,null=True)
    fest_post = models.ForeignKey(api2_models.AllFests,on_delete=models.CASCADE, related_name='post_from_club',blank=True,null=True)
    sac_post = models.ForeignKey(api2_models.SAC_MEMS,on_delete=models.CASCADE, related_name='post_from_club',blank=True,null=True)



    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username)

    #def delete(self):
    #    self.filefield.delete(save=False)
    #    super().delete()

class post_Likes(models.Model):
    post_id = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='post_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_like_username')
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.post_id)

class post_Comments(models.Model):
    post_id = models.ForeignKey(PostTable, on_delete=models.CASCADE, related_name='post_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_comment_username')
    Comment = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.post_id)


class Lost_Found(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='lst_found_username')
    title = models.CharField(max_length=50,default="")
    description = models.TextField(default="")
    tag = models.CharField(max_length=50,default="lost/found")
    img = models.ImageField(upload_to = 'lost_found',default = 'static/img.png')
    img_ratio = models.FloatField(default = 1.00)
    comment_count = models.IntegerField(default=0)
    lst_hiders = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
         return str(self.username)

  #  def delete(self, *args, **kwargs):
  #      self.img.delete(save=False)
  #      super().delete(*args, **kwargs)

class LST_Comments(models.Model):
    lst_cmnt_id = models.ForeignKey(Lost_Found, on_delete=models.CASCADE, related_name='lst_found_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='lst_cmnt_username',default="")
    Comment = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.lst_cmnt_id)


class Events(models.Model):
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
    all_universities = models.BooleanField(default = True)
    domain = models.TextField(default="@nitc.ac.in")

    event_category = models.CharField(default="student",max_length=100,choices = (('student','student'),('club','club'),('sport','sport'),('fest','fest'),('sac','sac')))
    club_event = models.ForeignKey(api2_models.AllClubs,on_delete=models.CASCADE, related_name='event_from_club',blank=True,null=True)
    sport_event = models.ForeignKey(api2_models.AllSports,on_delete=models.CASCADE, related_name='event_from_club',blank=True,null=True)
    fest_event = models.ForeignKey(api2_models.AllFests,on_delete=models.CASCADE, related_name='event_from_club',blank=True,null=True)
    sac_event = models.ForeignKey(api2_models.SAC_MEMS,on_delete=models.CASCADE, related_name='event_from_club',blank=True,null=True)





    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)


class Event_likes(models.Model):
    event_id = models.ForeignKey(Events,on_delete=models.CASCADE,related_name='event_like_id')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='event_like')
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.event_id)

class Alerts(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='alerts_username')
    title = models.CharField(max_length=50,default="")
    description = models.TextField(default="")
    img = models.FileField(upload_to = 'alerts',default = 'static/img.png')
    img_ratio = models.FloatField(default = 0.0)
    comment_count = models.IntegerField(default=0)
    allow_branchs = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    allow_years = models.CharField(default="1111",max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)
    all_universities = models.BooleanField(default = True)
    domain = models.TextField(default="@nitc.ac.in")


    thread_category = models.CharField(default="student",max_length=100,choices = (('student','student'),('club','club'),('sport','sport'),('fest','fest'),('sac','sac')))
    club_thread = models.ForeignKey(api2_models.AllClubs,on_delete=models.CASCADE, related_name='thread_from_club',blank=True,null=True)
    sport_thread = models.ForeignKey(api2_models.AllSports,on_delete=models.CASCADE, related_name='thread_from_club',blank=True,null=True)
    fest_thread = models.ForeignKey(api2_models.AllFests,on_delete=models.CASCADE, related_name='thread_from_club',blank=True,null=True)
    sac_thread = models.ForeignKey(api2_models.SAC_MEMS,on_delete=models.CASCADE, related_name='thread_from_club',blank=True,null=True)





    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)

class ALERT_Comments(models.Model):
    alert_cmnt_id = models.ForeignKey(Alerts, on_delete=models.CASCADE, related_name='alert_comment')
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='alert_cmnt_username',default="")
    Comment = models.TextField(default="")
    img = models.FileField(upload_to = 'alerts',default = 'static/img.png')
    img_ratio = models.FloatField(default = 0.0)
    allow_branchs = models.CharField(default="CS@EC@EE@ME@CE@CH@BT@AR@MT@EP@PE",max_length=100)
    allow_years = models.CharField(default="1111",max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username) + ":" + str(self.alert_cmnt_id)



class UniBranches(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='UniBranches_user')
    course = models.CharField(default="B.Tech",max_length=100,choices = (('B.Tech','B.Tech'),('M.Tech','M.Tech'),('PG','PG'),('Phd','Phd'),('MBA','MBA')))
    branch_name = models.CharField(default="CS",max_length=100)
    semisters = models.TextField(default="")
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")
    priority = models.CharField(default="CS",max_length=100)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return str(self.branch_name)




class BranchSub(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSub_user')
    sub_name = models.CharField(max_length=100,default="@")
    sub_id = models.CharField(max_length=100,default="@")
    all_years = models.TextField(default="@")
    num_years = models.IntegerField(default=0)
    description = models.TextField(default="@")
    posted_date = models.DateTimeField(default=timezone.now)
    tot_ratings_val = models.IntegerField(default=0)
    num_ratings = models.IntegerField(default=0)
    course = models.CharField(default="B.Tech",max_length=100,choices = (('B.Tech','B.Tech'),('M.Tech','M.Tech'),('PG','PG'),('Phd','Phd'),('MBA','MBA')))
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-sub_name']

    def __str__(self):
        return str(self.sub_name)


class BranchSubYears(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSubYears_user')
    sub_name = models.ForeignKey(BranchSub,on_delete=models.CASCADE, related_name='CalenderSub')
    year_name = models.CharField(max_length=100,default="@")
    private = models.BooleanField(default=False)
    num_files = models.IntegerField(default=0)
    description = models.TextField(default="@")
    posted_date = models.DateTimeField(default=timezone.now)
    course = models.CharField(default="B.Tech",max_length=100,choices = (('B.Tech','B.Tech'),('M.Tech','M.Tech'),('PG','PG'),('Phd','Phd'),('MBA','MBA')))
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-year_name']

    def __str__(self):
        return str(self.sub_name)


class BranchSubFiles(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='CalenderSubFiles_user')
    year_id = models.ForeignKey(BranchSubYears, on_delete=models.CASCADE, related_name='CalenderSubYears')
    description = models.TextField(default="@")
    qn_ans_file = models.FileField(upload_to = 'QnsAns',default = 'static/img.png')
    file_type = models.CharField(default="@",max_length=100)
    file_name = models.CharField(default="@",max_length=100)
    year = models.CharField(default="@",max_length=100)
    posted_date = models.DateTimeField(default=timezone.now)
    course = models.CharField(default="B.Tech",max_length=100,choices = (('B.Tech','B.Tech'),('M.Tech','M.Tech'),('PG','PG'),('Phd','Phd'),('MBA','MBA')))
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-file_name']

    def __str__(self):
        return str(self.year_id)


class Ratings(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='Ratings_user')
    sub_name = models.ForeignKey(BranchSub,on_delete=models.CASCADE, related_name='CalenderSub_ratings')
    description = models.TextField(default="@")
    rating = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    posted_date = models.DateTimeField(default=timezone.now)
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.username)




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
    domain = models.TextField(default="@nitc.ac.in")

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
    domain = models.TextField(default="@nitc.ac.in")

    class Meta:
        ordering = ['-message_date']

    def __str__(self):
        return str(self.message_sender)







class Mess_table(models.Model):
    hostel = models.CharField(max_length=50,default="")
    domain = models.TextField(default="@nitc.ac.in")
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
    domain = models.TextField(default="@nitc.ac.in")
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
    domain = models.TextField(default="@nitc.ac.in")
    sun = models.TextField(default = '')
    mon = models.TextField(default = '')
    tue = models.TextField(default = '')
    wed = models.TextField(default = '')
    thu = models.TextField(default = '')
    fri = models.TextField(default = '')
    sat = models.TextField(default = '')

    def __str__(self):
        return str(self.branch_name)

