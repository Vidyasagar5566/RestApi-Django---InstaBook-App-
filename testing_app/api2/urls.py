from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [

#CLUBS/SPORTS/FESTS
    path('allclubs/list1', views.ALLCLUBS_list.as_view(),name = 'ALLCLUBS_list'),
    path('club/like_list1', views.CLUB_like_list.as_view(),name = 'CLUB_like_list'),
    path('allsports/list1', views.ALLSPORTS_list.as_view(),name = 'ALLSPORTS_list'),
    path('sport/like_list1', views.SPORT_like_list.as_view(),name = 'SPORT_like_list'),
    path('allfests/list1', views.ALLFESTS_list.as_view(),name = 'ALLFESTS_list'),
    path('fest/like_list1', views.FEST_like_list.as_view(),name = 'FEST_like_list'),

    path('club_sport_fest/memb1', views.CLUB_SPORT_FEST_MEMB.as_view(),name = 'CLUB_SPORT_FEST_MEMB'),

#ACADEMIC_EVENT
    path('all_branches/list1', views.ALL_BRANCHES.as_view(),name = 'ALL_BRANCHES'),
    path('cal_dates_subs/list1', views.ALL_SEM_SUBS.as_view(),name = 'CALENDER_DATE_SUBS'),   #include subjects
    path('cal_sub_years/list1', views.ALL_SUB_YEARS.as_view(),name = 'CALENDER_SUB_YEARS'),
    path('calender_sub_files1', views.ALL_SUB_YEAR_FILES.as_view(),name = 'CALENDER_SUB_FILES'),
    path('timetable/list1', views.TIME_TABLE.as_view(),name = 'TIME_TABLE'),
    path('ratings', views.RATINGS.as_view(),name = 'RATINGS'),

    path('security1', views.SECURITY.as_view(),name = 'SECURITY1'),

    path('sac/list1', views.SAC_list.as_view(),name = 'SAC_list1'),
    path('mess/list1', views.MESS_list.as_view(),name = 'ACADEMIC_list1'),
    path('academic/list1', views.ACADEMIC_list.as_view(),name = 'ACADEMIC_list1'),

    ]