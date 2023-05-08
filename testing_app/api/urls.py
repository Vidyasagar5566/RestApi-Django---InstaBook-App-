from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('', views.testing.as_view(),name = 'login'),
    path('login', obtain_auth_token),
    path('register/email_check', views.Register_EMAIL_check.as_view(),name = 'Register'),
    path('get_user', views.GET_user.as_view(),name = 'GET_user'),
    path('lost_found/list', views.LST_list.as_view(),name = 'LST_list'),
    path('lost_found/comment_list', views.LST_Comment_list.as_view(),name = 'LST_Comment_list'),
    path('post/list', views.POST_list.as_view(),name = 'POST_list'),
    path('post/comment_list', views.PST_CMNT_list.as_view(),name = 'PST_CMNT_list'),
    path('post/like_list', views.POST_LIKE_list.as_view(),name = 'POST_LIKE_list'),
    path('event/list', views.EVENT_list.as_view(),name = 'EVENT_list'),
    path('event/like_list', views.EVENT_LIKE_list.as_view(),name = 'EVENT_LIKE_list'),
    path('alert/list', views.ALERT_list.as_view(),name = 'ALERT_list'),
    path('alert/comment_list', views.ALERT_CMNT_list.as_view(),name = 'ALERT_comment_list'),
    path('club_sport/list', views.CLUB_SPORT_list.as_view(),name = 'CLUB_SPORT_list'),
    path('club_sport/edit', views.CLUB_SPORT_edit.as_view(),name = 'CLUB_SPORT_edit'),
    path('club_sport/like_list', views.CLUB_SPORT_like_list.as_view(),name = 'CLUB_SPORT_like_list'),
    path('club_sport/memb', views.CLUB_SPORT_MEMB.as_view(),name = 'CLUB_SPORT'),
    path('profile/list', views.PEOFILE_list.as_view(),name = 'PEOFILE_list'),
    path('sac/list', views.SAC_list.as_view(),name = 'SAC_list'),
    path('mess/list', views.MESS_list.as_view(),name = 'ACADEMIC_list'),
    path('academic/list', views.ACADEMIC_list.as_view(),name = 'ACADEMIC_list'),
    path('timetable/list', views.TIMETABLE_list.as_view(),name = 'TIMETABLE_list'),

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