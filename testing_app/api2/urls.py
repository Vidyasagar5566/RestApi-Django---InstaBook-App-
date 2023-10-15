from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [

    path('test_api2', views.testing_api2.as_view(),name = 'testing_api2'),

#CLUBS/SPORTS/FESTS
    path('allclubs', views.ALLCLUBS_list.as_view(),name = 'ALLCLUBS_list'),
    path('club/likes', views.CLUB_like_list.as_view(),name = 'CLUB_like_list'),
    path('allsports', views.ALLSPORTS_list.as_view(),name = 'ALLSPORTS_list'),
    path('sport/likes', views.SPORT_like_list.as_view(),name = 'SPORT_like_list'),
    path('allfests', views.ALLFESTS_list.as_view(),name = 'ALLFESTS_list'),
    path('fest/likes', views.FEST_like_list.as_view(),name = 'FEST_like_list'),

    path('club_sport_fest/mems', views.CLUB_SPORT_FEST_MEMB.as_view(),name = 'CLUB_SPORT_FEST_MEMB'),

#ACADEMIC_SUBJECTS
    path('all_branches/list1', views.ALL_BRANCHES.as_view(),name = 'ALL_BRANCHES'),
    path('cal_dates_subs/list1', views.ALL_SEM_SUBS.as_view(),name = 'CALENDER_DATE_SUBS'),
    path('cal_sub_years/list1', views.ALL_SUB_YEARS.as_view(),name = 'CALENDER_SUB_YEARS'),
    path('calender_sub_files1', views.ALL_SUB_YEAR_FILES.as_view(),name = 'CALENDER_SUB_FILES'),
    path('timetable/list1', views.TIME_TABLE.as_view(),name = 'TIME_TABLE'),
    path('ratings', views.RATINGS.as_view(),name = 'RATINGS'),

    path('security1', views.SECURITY.as_view(),name = 'SECURITY1'),

#ACADEMICS
    path('sac', views.SAC_list.as_view(),name = 'SAC_list1'),
    path('mess', views.MESS_list.as_view(),name = 'ACADEMIC_list1'),
    path('academic', views.ACADEMIC_list.as_view(),name = 'ACADEMIC_list1'),


#Notifications
    path('send_notifications1', views.SendNotifications.as_view(),name = 'send_notifications1'),
    path('notifications1', views.Notifications.as_view(),name = 'Notifications1'),
    path('edit_notif_settings1', views.EDIT_notif_settings.as_view(),name = 'EDIT_notif_settings1'),
    ]














