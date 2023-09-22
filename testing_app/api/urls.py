from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
 #   path('', views.testing.as_view(),name = 'login'),
 #   path('login', obtain_auth_token),
 #   path('register/email_check', views.Register_EMAIL_check.as_view(),name = 'Register'),
 #   path('get_user', views.GET_user.as_view(),name = 'GET_user'),
 #   path('lost_found/list', views.LST_list.as_view(),name = 'LST_list'),
 #   path('lost_found/comment_list', views.LST_Comment_list.as_view(),name = 'LST_Comment_list'),
 #   path('post/list', views.POST_list.as_view(),name = 'POST_list'),
 #   path('post/comment_list', views.PST_CMNT_list.as_view(),name = 'PST_CMNT_list'),
 #   path('post/like_list', views.POST_LIKE_list.as_view(),name = 'POST_LIKE_list'),
 #   path('event/list', views.EVENT_list.as_view(),name = 'EVENT_list'),
 #   path('event/like_list', views.EVENT_LIKE_list.as_view(),name = 'EVENT_LIKE_list'),
 #   path('alert/list', views.ALERT_list.as_view(),name = 'ALERT_list'),
 #   path('alert/comment_list', views.ALERT_CMNT_list.as_view(),name = 'ALERT_comment_list'),
 #   path('club_sport/list', views.CLUB_SPORT_list.as_view(),name = 'CLUB_SPORT_list'),
 #   path('club_sport/edit', views.CLUB_SPORT_edit.as_view(),name = 'CLUB_SPORT_edit'),
 #   path('club_sport/like_list', views.CLUB_SPORT_like_list.as_view(),name = 'CLUB_SPORT_like_list'),
 #   path('club_sport/memb', views.CLUB_SPORT_MEMB.as_view(),name = 'CLUB_SPORT'),
 #   path('profile/list', views.PEOFILE_list.as_view(),name = 'PEOFILE_list'),
 #   path('sac/list', views.SAC_list.as_view(),name = 'SAC_list'),
 #   path('mess/list', views.MESS_list.as_view(),name = 'ACADEMIC_list'),
 #   path('academic/list', views.ACADEMIC_list.as_view(),name = 'ACADEMIC_list'),
 #   path('timetable/list', views.TIMETABLE_list.as_view(),name = 'TIMETABLE_list'),
 #   path('notifications', views.Notifications.as_view(),name = 'Notifications'),
 #  path('edit_notif_settings', views.EDIT_notif_settings.as_view(),name = 'EDIT_notif_settings'),


    path('test', views.testing.as_view(),name = 'login'),
    path('login2', obtain_auth_token),
    path('register/email_check2', views.Register_EMAIL_check.as_view(),name = 'Register1'),
    path('get_user2', views.GET_user.as_view(),name = 'GET_user1'),
    path('lost_found/list1', views.LST_list.as_view(),name = 'LST_list1'),
    path('lost_found/comment_list1', views.LST_Comment_list.as_view(),name = 'LST_Comment_list1'),
    path('post/list1', views.POST_list.as_view(),name = 'POST_list1'),
    path('post/comment_list1', views.PST_CMNT_list.as_view(),name = 'PST_CMNT_list1'),
    path('post/like_list1', views.POST_LIKE_list.as_view(),name = 'POST_LIKE_list1'),
    path('event/list1', views.EVENT_list.as_view(),name = 'EVENT_list1'),
    path('event/like_list1', views.EVENT_LIKE_list.as_view(),name = 'EVENT_LIKE_list1'),
    path('alert/list1', views.ALERT_list.as_view(),name = 'ALERT_list1'),
    path('alert/comment_list1', views.ALERT_CMNT_list.as_view(),name = 'ALERT_comment_list1'),
    path('club_sport/list1', views.CLUB_SPORT_list.as_view(),name = 'CLUB_SPORT_list1'),
    path('club_sport/edit1', views.CLUB_SPORT_edit.as_view(),name = 'CLUB_SPORT_edit1'),
    path('club_sport/like_list1', views.CLUB_SPORT_like_list.as_view(),name = 'CLUB_SPORT_like_list1'),
    path('club_sport/memb1', views.CLUB_SPORT_MEMB.as_view(),name = 'CLUB_SPORT1'),
    path('profile/list1', views.PEOFILE_list.as_view(),name = 'PEOFILE_list1'),
    path('sac/list1', views.SAC_list.as_view(),name = 'SAC_list1'),
    path('mess/list1', views.MESS_list.as_view(),name = 'ACADEMIC_list1'),
    path('academic/list1', views.ACADEMIC_list.as_view(),name = 'ACADEMIC_list1'),
    path('notifications1', views.Notifications.as_view(),name = 'Notifications1'),
    path('edit_notif_settings1', views.EDIT_notif_settings.as_view(),name = 'EDIT_notif_settings1'),

# MESSANGER  && NOTIFICATIONS
    path('send_notifications1', views.SendNotifications.as_view(),name = 'send_notifications1'),
    path('messanger1', views.Messanger.as_view(),name = 'Messanger1'),
    path('user_messanger1', views.USER_Messanger.as_view(),name = 'user_messanger1'),
#CALENDER_EVENT
    path('cal_dates_subs/list1', views.CALENDER_DATE_SUBS.as_view(),name = 'CALENDER_DATE_SUBS'),   #include subjects
    path('cal_sub_years/list1', views.CALENDER_SUB_YEARS.as_view(),name = 'CALENDER_SUB_YEARS'),
    path('calender_sub_files1', views.CALENDER_SUB_FILES.as_view(),name = 'CALENDER_SUB_FILES'),
    path('cal_events/list1', views.CALENDER_EVENTS_list.as_view(),name = 'CALENDER_EVENTS_list'),
    path('timetable/list1', views.TIME_TABLE.as_view(),name = 'TIME_TABLE'),
    path('ratings', views.RATINGS.as_view(),name = 'RATINGS'),

   path('security1', views.SECURITY.as_view(),name = 'SECURITY1'),


    ]































#final queryParameters = {
#  'param1': 'one',
#  'param2': 'two',
#};
#final uri =
#    Uri.https('www.myurl.com', '/api/v1/test', queryParameters);
#final response = await http.get(uri, headers: {
#  HttpHeaders.authorizationHeader: 'Token $token',
#  HttpHeaders.contentTypeHeader: 'application/json',
#});
