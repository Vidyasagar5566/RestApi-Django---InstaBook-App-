from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [

    path('test', views.testing.as_view(),name = 'login'),
    path('login2', obtain_auth_token),
    path('register/email_check2', views.Register_EMAIL_check.as_view(),name = 'Register1'),
    path('get_user2', views.GET_user.as_view(),name = 'GET_user1'),
    path('edit_notif_settings1', views.EDIT_notif_settings.as_view(),name = 'EDIT_notif_settings1'),
    path('lost_found/list1', views.LST_list.as_view(),name = 'LST_list1'),
    path('lost_found/comment_list1', views.LST_Comment_list.as_view(),name = 'LST_Comment_list1'),
    path('post/list1', views.POST_list.as_view(),name = 'POST_list1'),
    path('post/comment_list1', views.PST_CMNT_list.as_view(),name = 'PST_CMNT_list1'),
    path('post/like_list1', views.POST_LIKE_list.as_view(),name = 'POST_LIKE_list1'),
    path('event/list1', views.EVENT_list.as_view(),name = 'EVENT_list1'),
    path('event/like_list1', views.EVENT_LIKE_list.as_view(),name = 'EVENT_LIKE_list1'),
    path('alert/list1', views.ALERT_list.as_view(),name = 'ALERT_list1'),
    path('alert/comment_list1', views.ALERT_CMNT_list.as_view(),name = 'ALERT_comment_list1'),
    path('profile/list1', views.PEOFILE_list.as_view(),name = 'PEOFILE_list1'),


    path('cal_events/list1', views.CALENDER_EVENTS_list.as_view(),name = 'CALENDER_EVENTS_list'),

# MESSANGER
    path('messanger1', views.Messanger.as_view(),name = 'Messanger1'),
    path('user_messanger1', views.USER_Messanger.as_view(),name = 'user_messanger1'),

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
