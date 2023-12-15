from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
import base64
import datetime
from . import serializers
from . import models
from api import models as api_models
from api import serializers as api_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User = get_user_model()
import random
from firebase_admin.messaging import Message, Notification
from firebase_admin import messaging
from fcm_django.models import FCMDevice
from django.db.models import Q
from django.utils.timezone import localtime
from django.utils import timezone



#        user = request.user
#        data = request.data
#        data = request.query_params



datetime_weight = 0.6
like_weight = 0.2
comment_weight = 0.3

domains = {

'nitt.edu'  : 'Nit Trichy',
'nitk.edu.in' : 'Nit Surathkal',
'nitrkl.ac.in' : 'Nit Rourkela',
'nitw.ac.in': ' Nit Warangal',
'nitc.ac.in'   :'Nit Calicut',
'vnit.ac.in':  'Nit Nagpur',
'nitdgp.ac.in' :  'Nit Durgapur',
'nits.ac.in':    'Nit Silchar',
'mnit.ac.in':   'Nit Jaipur',
'mnnit.ac.in' : 'Nit Allahabad',
'nitkkr.ac.in':   'Nit Kurukshetra',
'nitj.ac.in'  :' Nit Jalandhar',
'svnit.ac.in': ' Nit Surat',
'nitm.ac.in' : 'Nit Meghalaya',
'nitp.ac.in' : 'Nit Patna',
'nitrr.ac.in' : 'Nit Raipur',
'nitsri.ac.in' : 'Nit Srinagar',
'manit.ac.in'  :'Nit Bhopal',
'nita.ac.in'  :'Nit Agarthala',
'nitgoa.ac.in' :  'Nit Goa',
'nitjsr.ac.in' : 'Nit Jamshedpur',
'nitmanipur.ac.in':  'Nit Manipur',
'nith.ac.in'   : 'Nit Hamper',
'nituk.ac.in'  : ' Nit Uttarakhand',
'nitpy.ac.in' : 'Nit Puducherry',
'nitap.ac.in' : 'Nit ArunaChalPradesh',
'nitsikkim.ac.in':  'Nit Sikkim',
'nitdelhi.ac.in' : 'Nit Delhi',
'nitmz.ac.in': 'Nit Mizoram',
'nitnagaland.ac.in' : 'Nit Nagaland',
'nitandhra.ac.in' : 'Nit AndhraPradesh',



##IITS

'iitm.ac.in' : 'IIT Madras',
'iitd.ac.in' : 'IIT Delhi',
'iitb.ac.in' : 'IIT Bombay',
'iitk.ac.in' : 'IIT Kanpur',
'iitr.ac.in' : 'IITR Rookee',
'iitkgp.ac.in' : 'IIT Kharagpur',
'iitg.ac.in' : 'IIT Guwahati',
'iith.ac.in' : 'IIT Hyderabad',
'iitbhu.ac.in' :  'IIT BHU',
'iitism.ac.in'  :  'IIT ISM Dhanbad',
'iiti.ac.in'  : 'IIT Indore',
'iitrpr.ac.in'  : 'IIT Rupar',
'iitmandi.ac.in' :   'IIT Mandi',
'iitgn.ac.in'   :  'IIT Gandhinagar',
'iitj.ac.in'   : 'IIT Jodhpur',
'iitp.ac.in'   :     'IIT Patna',
'iitbbs.ac.in'  :   'IIT Bhubaneswar',
'iittp.ac.in'   :  'IIT Tirupati',
'iitpkd.ac.in'  :  'IIT Palakkad',
'iitjammu.ac.in' :   'IIT Jammu',
'iitdh.ac.in'    : 'IIT Dharwad',
'iitbhilai.ac.in'  :  'IIT Bhilai'

    }







def team_members_transfer(old_team_mem,new_team_mem,id,category,name):
    old_team_mem_set = set(old_team_mem.split('#'))
    new_team_mem_set = set(new_team_mem.split('#'))
    common_people = old_team_mem_set.intersection(new_team_mem_set)
    old_team_mem = old_team_mem_set - common_people
    new_team_mem = new_team_mem_set - common_people

    #removing club from this old people
    for i in old_team_mem:
        try:
            user = User.objects.get(email = i)
            if category == 'club':
                del[user.clz_clubs['team_member'][str(id)]]
            elif category == 'sport':
                del[user.clz_sports['team_member'][str(id)]]
            elif category == 'fest':
                del[user.clz_fests['team_member'][str(id)]]
            elif category == 'sac':
                del[user.clz_sacs['team_member'][str(id)]]
            user.save()
        except:
            continue

    #adding club to this new people
    for i in new_team_mem:
        try:
            user = User.objects.get(email = i)
            if category == 'club':
                user.clz_clubs['team_member'][str(id)] = name
            elif category == 'sport':
                user.clz_sports['team_member'][str(id)] = name
            elif category == 'fest':
                user.clz_fests['team_member'][str(id)] = name
            elif category == 'sac':
                user.clz_sacs['team_member'][str(id)] = name
            user.save()
        except:
            continue






class testing_api2(APIView):
    def get(self,request):
        error = False
        password = ""
        try:

            # user = User.objects.get(email = "shiva@gmail.com")
            # users = User.objects.all()


            data = models.DatingUser.objects.all()
            serializer = serializers.DatingUserSerializer(data,many = True)
            return Response(serializer.data)


        except:
            error = True
        return Response({"error":error,"password":a})



def bulk_notifications(fcm_tokens,title,description):
    div = len(fcm_tokens)//100
    for i in range(div+1):
        message = messaging.MulticastMessage(
                    notification=messaging.Notification(
                    title=title,
                    body=description
                    ),
                    tokens=fcm_tokens[i*100:(i+1)*100],
                    data={"key1": "value1", "key2": "value2"},
                    )
        # messaging.send_multicast(message)


class SendNotifications(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]


# 1 lst_buy, 2 posts, 3 posts_admin, 4 events, 5 threads, 6 comments, 7 announcements, 8 messanger


    def post(self,request):
        data = request.data
        user = request.user
        filter_notifications = []
        if data['notiff_sett'] == 1:
            filter_notifications = api_models.FilterNotifications.objects.filter(lst_buy = True,domain = user.domain)
        elif data['notiff_sett'] == 2:
            filter_notifications = api_models.FilterNotifications.objects.filter(posts = True,domain = user.domain)
        elif data['notiff_sett'] == 3:
            filter_notifications = api_models.FilterNotifications.objects.filter(posts_admin = True,domain = user.domain)
        elif data['notiff_sett'] == 4:
            filter_notifications = api_models.FilterNotifications.objects.filter(events = True,domain = user.domain)
        elif data['notiff_sett'] == 5:
            filter_notifications = api_models.FilterNotifications.objects.filter(threads = True,domain = user.domain)
        elif data['notiff_sett'] == 6:
            filter_notifications = api_models.FilterNotifications.objects.filter(comments = True,domain = user.domain)

        fcm_tokens = []
        for i in filter_notifications:
            fcm_tokens.append(i.fcm_token)
        bulk_notifications(fcm_tokens,data['title'],data['description'])
        return Response({"error":False,'tokens':len(fcm_tokens)})


#for announcements
    def put(self,request):
        user = request.user
        data = request.data
        users = User.objects.filter(domain = user.domain)
        fcm_tokens = []
        for i in users:
            if data['notif_year'][i.year - 1] == "1" and (i.branch in data['notif_branchs']) and (i.course in data['notif_courses']):
                i.notif_seen = False
                i.notif_count += 1
                i.save()
                try:

                    filter_notif = api_models.FilterNotifications.objects.get(username = i)
                    if filter_notif.announcements == True:
                        fcm_tokens.append(filter_notif.fcm_token)
                except:
                    a = 0
        bulk_notifications(fcm_tokens,user.email,"Gave Announcement : " + " : " + data['description'])
        return Response({"error":False,"tokens":len(fcm_tokens)})







#CLUBS
class ALLCLUBS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            if data['domain'] == 'All':
                all_clubs = models.AllClubs.objects.all()
            else:
                all_clubs = models.AllClubs.objects.filter(domain = data['domain'])
            for i in all_clubs:
                try:
                    like = models.Clubs_likes.objects.get(club = i,username = user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.AllClubsSerializer(all_clubs,many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_club = models.AllClubs()
            new_club.name = data['club_name']
            new_club.domain = user.domain
            club_head = User.objects.get(email = data['email'])
            new_club.head = club_head
            new_club.save()
            club_head.clz_clubs['head'][str(new_club.id)] = data['club_name']
            club_head.save()

        except:
            error = True
        return Response({'error':error})


    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_club = models.AllClubs.objects.get(id = data['id'])
            old_team_mem = new_club.team_members
            new_club.name = data['name']
            if data['image_type'] == 'file':
                new_club.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_club.title = data['title']
            new_club.domain = user.domain
            new_club.head = user
            new_club.team_members = data['team_members']
            new_club.description = data['description']
            new_club.websites = data['websites']
            new_club.save()
            if old_team_mem != data['team_members']:
                team_members_transfer(old_team_mem,data['team_members'],data['id'],'club',data['name'])

        except:
            error = True
        return Response({'error':error})



    def patch(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_club = models.AllClubs.objects.get(id = int(data['id']))
            new_head = User.objects.get(email = data['new_head_email'])
            new_club.head = new_head
            del[user.clz_clubs['head'][str(data['id'])]]
            new_head.clz_clubs['head'][str(data['id'])] = new_club.name
            user.save()
            new_head.save()
            new_club.save()

        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        try:
            user = request.user
            data = request.data

            new_club = models.AllClubs.objects.get(id = int(data['id']))
            new_club_head = new_club.head
            del[new_club_head.clz_clubs['head'][str(data['id'])]]
            new_club_head.save()
            for i in new_club.team_members.split('#'):
                club_user = User.objects.get(email = i)
                del[club_user.clz_clubs['team_member'][str(data['id'])]]
                club_user.save()

        except:
            error = True
        return Response({'error':error})





class CLUB_like_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            club = models.AllClubs.objects.get(id = int(data['club_id']))
            club_like = models.Clubs_likes()
            club_like.club = club
            club_like.username = user
            club_like.domain = user.domain
            club_like.save()
            club.like_count += 1
            club.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            club = models.AllClubs.objects.get(id = int(data['club_id']))
            like = models.Clubs_likes.objects.get(username = user,club = club)
            like.delete()

            club.like_count -= 1
            club.save()
        except:
            error = True
        return Response({'error':error})




# SPORTS
class ALLSPORTS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user

            if data['domain'] == 'All':
                all_sports = models.AllSports.objects.all()
            else:
                all_sports = models.AllSports.objects.filter(domain = data['domain'])
            for i in all_sports:
                try:
                    like = models.Sports_likes.objects.get(sport = i,username = user)
                    i.is_like = True
                except:
                    i.is_like = False

            serializer = serializers.AllSportsSerializer(all_sports,many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_sport = models.AllSports()
            new_sport.name = data['sport_name']
            new_sport.domain = user.domain
            sport_head = User.objects.get(email = data['email'])
            new_sport.head = sport_head
            new_sport.save()
            sport_head.clz_sports['head'][str(new_sport.id)] = data['sport_name']
            sport_head.save()

        except:
            error = True
        return Response({'error':error})



    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_sport = models.AllSports.objects.get(id = data['id'])
            old_team_mem = new_sport.team_members
            new_sport.name = data['name']
            if data['image_type'] == 'file':
                new_sport.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_sport.title = data['title']
            new_sport.domain = user.domain
            new_sport.head = user
            new_sport.team_members = data['team_members']
            new_sport.description = data['description']
            new_sport.websites = data['websites']
            new_sport.sport_ground = data['sport_ground']
            if data['image2_type'] == 'file':
                new_sport.sport_ground_img = ContentFile(base64.b64decode(data['file1']),data['file_name1'])
            new_sport.save()
            if old_team_mem != data['team_members']:
                team_members_transfer(old_team_mem,data['team_members'],data['id'],'sport',data['name'])

        except:
            error = True
        return Response({'error':error})


    def patch(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_sport = models.AllSports.objects.get(id = data['id'])
            new_head = User.objects.get(email = data['new_head_email'])
            new_sport.head = new_head
            new_sport.save()
            del[user.clz_sports['head'][str(data['id'])]]
            user.save()
            new_head.clz_sports['head'][str(data['id'])] = new_sport.name
            new_head.save()

        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        try:
            user = request.user
            data = request.data

            new_sport = models.AllSports.objects.get(id = int(data['id']))
            new_sport_head = new_sport.head
            del[new_sport_head.clz_sports['head'][str(data['id'])]]
            new_sport_head.save()
            for i in new_sport.team_members.split('#'):
                sport_user = User.objects.get(email = i)
                del[sport_user.clz_sports['team_member'][str(data['id'])]]
                clz_sports.save()

        except:
            error = True
        return Response({'error':error})



class SPORT_like_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            sport = models.AllSports.objects.get(id = int(data['sport_id']))
            sport_like = models.Sports_likes()
            sport_like.sport = sport
            sport_like.username = user
            sport_like.domain = user.domain
            sport_like.save()
            sport.like_count += 1
            sport.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            sport = models.AllSports.objects.get(id = int(data['sport_id']))

            like = models.Sports_likes.objects.get(username = user,sport = sport)
            like.delete()

            sport.like_count -= 1
            sport.save()
        except:
            error = True
        return Response({'error':error})






#FESTS
class ALLFESTS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            if data['domain'] == 'All':
                all_fests = models.AllFests.objects.all()
            else:
                all_fests = models.AllFests.objects.filter(domain = data['domain'])
            for i in all_fests:
                try:
                    like = models.Fests_likes.objects.get(fest = i,username = user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.AllFestsSerializer(all_fests,many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_fest = models.AllFests()
            new_fest.name = data['fest_name']
            new_fest.domain = user.domain
            fest_head = User.objects.get(email = data['email'])
            new_fest.head = fest_head
            new_fest.save()
            fest_head.clz_fests['head'][str(new_fest.id)] = data['fest_name']
            fest_head.save()

        except:
            error = True
        return Response({'error':error})




    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_fest = models.AllFests.objects.get(id = data['id'])
            old_team_mem = new_fest.team_members
            new_fest.name = data['name']
            if data['image_type'] == 'file':
                new_fest.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_fest.title = data['title']
            new_fest.domain = user.domain
            new_fest.head = user
            new_fest.team_members = data['team_members']
            new_fest.description = data['description']
            new_fest.websites = data['websites']
            new_fest.save()
            if old_team_mem != data['team_members']:
                team_members_transfer(old_team_mem,data['team_members'],data['id'],'fest',data['name'])

        except:
            error = True
        return Response({'error':error})


    def patch(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_fest = models.AllFests.objects.get(id = data['id'])
            new_head = User.objects.get(email = data['new_head_email'])
            new_fest.head = new_head
            new_fest.save()
            del[user.clz_fests['head'][str(data['id'])]]
            user.save()
            new_head.clz_fests['head'][str(data['id'])] = new_fest.name
            new_head.save()

        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        try:
            user = request.user
            data = request.data

            new_fest = models.AllFests.objects.get(id = int(data['id']))
            new_fest_head = new_fest.head
            del[new_fest_head.clz_fests['head'][str(data['id'])]]
            new_fest_head.save()
            for i in new_fest.team_members.split('#'):
                fest_user = User.objects.get(email = i)
                del[fest_user.clz_fests['team_member'][str(data['id'])]]
                fest_user.save()

        except:
            error = True
        return Response({'error':error})




class FEST_like_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            fest = models.AllFests.objects.get(id = int(data['fest_id']))
            fest_like = models.Fests_likes()
            fest_like.fest = fest
            fest_like.username = user
            fest_like.domain = user.domain
            fest_like.save()
            fest.like_count += 1
            fest.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            fest = models.AllFests.objects.get(id = int(data['fest_id']))

            like = models.Fests_likes.objects.get(username = user,fest = fest)
            like.delete()

            fest.like_count -= 1
            fest.save()
        except:
            error = True
        return Response({'error':error})




class SAC_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            if data['domain'] == "All":
                sac = models.SAC_MEMS.objects.all()
            else:
                sac = models.SAC_MEMS.objects.filter(domain = data['domain'])
            serializer = serializers.SAC_MEMSSerializer(sac,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            sac = models.SAC_MEMS()
            sac.role = data['role']
            sac.domain = user.domain
            sac_head = User.objects.get(email = data['email'])
            sac.head = sac_head
            sac.save()
            sac_head.clz_sacs['head'][str(sac.id)] = data['role']
            sac_head.save()

        except:
            error = True
        return Response({'error':error})


    def put(self,request):
        error = False
        try:
            data = request.data
            user = request.user

            sac = models.SAC_MEMS.objects.get(id = data['id'])
            if data['image_type'] == 'file':
                sac.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            sac.role =  data['role']
            sac.email = data['email']
            sac.phone_num = data['phone_num']
            sac.description = data['description']
            sac.save()

        except:
            error = True
        return Response({'error':error})



    def patch(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            sac = models.SAC_MEMS.objects.get(id = data['id'])
            new_head = User.objects.get(email = data['new_head_email'])
            sac.head = new_head
            sac.save()
            del[user.clz_sacs['head'][str(data['id'])]]
            user.save()
            new_head.clz_sacs['head'][str(data['id'])] = sac.role
            new_head.save()

        except:
            error = True
        return Response({'error':error})



    def delete(self,request):
        try:
            user = request.user
            data = request.data

            new_sac = models.SAC_MEMS.objects.get(id = int(data['id']))
            new_sac_head = new_sac.head
            del[new_sac_head.clz_sacs['head'][str(data['id'])]]
            new_sac_head.save()

        except:
            error = True
        return Response({'error':error})


# TEAM MEMBERS

class CLUB_SPORT_FEST_MEMB(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            team_mem = data["team_mem"].split('#')
            team_mem_data = []
            for i in team_mem:
                try:
                    user = User.objects.get(email = i)
                    team_mem_data.append(user)
                except:
                    continue
            serializer = serializers.SmallUserSerializer(team_mem_data, many=True)

            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})





class ALL_BRANCHES(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            all_branches = api_models.UniBranches.objects.filter(domain = data['domain'],course = data['course'])
            serializer = serializers.UniBranchesSerializer(all_branches,many = True)
            ans = serializer.data
            ans.reverse()
            return Response(ans)
        except:
            error = True
        return Response({'error':error})


# using to get all subjects
class ALL_SEM_SUBS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            if data['sub_id'] == 'CPC':
                if data['domain'] == "All":
                    all_sub_names = api_models.BranchSub.objects.filter(sub_id = data['sub_id'],domain = "@nitc.ac.in")
                else:
                    all_sub_names = api_models.BranchSub.objects.filter(sub_id = data['sub_id'],domain = data['domain'])
            else:
                all_sub_names = api_models.BranchSub.objects.filter(sub_id = data['sub_id'],domain = data['domain'],course = data['course'])
            serializer = serializers.CalenderSubSerializer(all_sub_names,many = True)
            res = serializer.data
            res.reverse()
            return Response(res)
        except:
            error = True
        return Response({'error':error})

    #POSTING NEW SUBJECT
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            sub = api_models.BranchSub()
            sub.username = user
            sub.sub_name = data['sub_name']
            sub.domain = user.domain
            sub.sub_id = data['sub_id']
            if data['sub_id'] == "CPC":
                sub.InternCompany = data["InternCompany"]
                sub.PlacementCompany = data['PlacementCompany']
            sub.save()
            return Response({'error':error,'id':sub.id})
        except:
            error = True
        return Response({'error':error,'id':"-1"})

    #EDITING SUBJECT
    def put(self,request):
        error = False
        try:
            data = request.data
            sub = api_models.BranchSub.objects.get(id = int(data['sub_id']))
            sub.sub_name = data['sub_name']
            if sub.sub_id == "CPC":
                sub.InternCompany = data["InternCompany"]
                sub.PlacementCompany = data['PlacementCompany']
            sub.save()

        except:
            error = True
        return Response({'error':error})




class ALL_SUB_YEARS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            sub = api_models.BranchSub.objects.get(id = int(data['sub_id']))

            if sub.sub_id == "CPC" and data['inter_placement'] == "Intern":
                sub_years = sub.CalenderSub.filter(InternCompany = True)
            else:
                sub_years = sub.CalenderSub.filter(InternCompany = False)

            serializer = serializers.CalenderSubYearsSerializer(sub_years,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            sub = api_models.BranchSub.objects.get(id = int(data['sub_id']))
            new_year = api_models.BranchSubYears()
            new_year.username = user
            new_year.domain = user.domain
            new_year.sub_name = sub
            new_year.year_name = data['year_name']
            new_year.private = data['private']
            if sub.sub_id == "CPC" and data['inter_placement'] == "Intern":
                new_year.InternCompany = True
            new_year.save()
            sub.num_years += 1
            sub.save()
            return Response({'error':error,'id':new_year.id})
        except:
            error = True
        return Response({'error':error,'id':'-1'})


    def put(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            year = api_models.BranchSubYears.objects.get(id = int(data['year_id']))
            year.year_name = data['year_name']
            year.private = data['private']
            year.save()

        except:
            error = True
        return Response({'error':error})




class ALL_SUB_YEAR_FILES(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            year = api_models.BranchSubYears.objects.get(id = int(data['year_id']))
            all_files = year.CalenderSubYears.all()
            serializer = serializers.CalenderSubFilesSerializer(all_files,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            qns_file  = api_models.BranchSubFiles()
            qns_file.username = user
            year = api_models.BranchSubYears.objects.get(id = data['year_id'])
            qns_file.year_id = year
            qns_file.domain = user.domain
            qns_file.description = data['description']
            qns_file.qn_ans_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
            qns_file.file_type = data['file_type']
            qns_file.file_name = data['file_name']
            qns_file.save()
            year.num_files += 1
            return Response({'error':error,'id':qns_file.id})
        except:
            error = True
        return Response({'error':error,'id':0})


    def delete(self,request):
        error = False
        try:
            data = request.data
            file = api_models.BranchSubFiles.objects.get(id = int(data['id']))
            file.delete()
        except:
            error = True
        return Response({'error':error})

    def put(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            qns_file  = api_models.BranchSubFiles.objects.get(id = int(data['id']))
            user = User.objects.get(email = data['file_email'])
            qns_file.username = user
            year = api_models.BranchSubYears.objects.get(id = data['year_id'])
            qns_file.year_id = year
            qns_file.description = data['description']
            qns_file.qn_ans_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
            qns_file.file_type = data['file_type']
            qns_file.file_name = data['file_name']
            qns_file.save()
            return Response({'error':error,'id':int(data['id'])})
        except:
            error = True
        return Response({'error':error,'id':0})


class RATINGS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            sub = api_models.BranchSub.objects.get(id = int(data['sub_id']))
            all_ratings = sub.CalenderSub_ratings.all()
            serializer = serializers.RatingsSerializer(all_ratings,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            try:
                sub_name = api_models.BranchSub.objects.get(id = int(data['sub_id']))
                rating  = api_models.Ratings.objects.get(username = user,sub_name = sub_name)
                sub_name.tot_ratings_val = sub_name.tot_ratings_val - rating.rating + data['rating']
                sub_name.save()
                rating.domain = user.domain
                rating.rating = data['rating']
                rating.description = data['review']
                rating.save()
                return Response({'error':error,'id':rating.id})
            except:
                rating  = api_models.Ratings()
                rating.username = request.user
                sub_name = api_models.BranchSub.objects.get(id = int(data['sub_id']))
                sub_name.tot_ratings_val += data['rating']
                sub_name.num_ratings += 1
                sub_name.save()
                rating.sub_name = sub_name
                rating.rating = data['rating']
                rating.description = data['review']
                rating.save()
                return Response({'error':error,'id':rating.id})
        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error = False
        try:
            data = request.data
            rating = api_models.Ratings.objects.get(id = int(data['id']))
            sub_name = rating.sub_name
            sub_name.tot_ratings_val -= rating.rating
            sub_name.num_ratings -= 1
            sub_name.save()
            rating.delete()
        except:
            error = True
        return Response({'error':error})





class MESS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            mess = api_models.Mess_table.objects.filter(domain = data['domain'])
            serializer = serializers.Mess_tableSerializer(mess,many = True)
            data = list(serializer.data)
            data.reverse()
            return Response(data)
        except:
            error = True
        return Response({'error':error})





class ACADEMIC_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            academic = api_models.Academic_table.objects.filter(domain = data['domain'])
            serializer = serializers.Academic_tableSerializer(academic,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            if data['id'] == 0:
                academic = api_models.Academic_table()
            else:
                academic = api_models.Academic_table.objects.get(id = int(data['id']))
            academic.academic_name = data['academic_name']
            academic.sun = data['sun']
            academic.mon = data['mon']
            academic.tue = data['tues']
            academic.wed = data['wed']
            academic.thu = data['thu']
            academic.fri = data['fri']
            academic.sat = data['sat']
            academic.domain = user.domain
            academic.save()
        except:
            error = True
        return Response({'error':error})




class SECURITY(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            Report = models.Reports()
            Report.username = user
            Report.report_belongs = data['report_belongs']
            Report.description = data['description']
            Report.domain = user.domain
            Report.save()

            data = Message(
                   notification=Notification(title= user.username + " Reported on " + data['report_belongs'] , body = data['description']),
                   )
            user1 = User.objects.get(email = "buddala_b190838ec@nitc.ac.in")
            try:
                device = FCMDevice()
                device.registration_id  = user1.token
                device.name = "Testing user"
                device.save()
                data = device.send_message(data)
            except:
                try:
                    device = FCMDevice.objects.get(registration_id = user1.token)
                    device.name = "Testing user"
                    device.save()
                    data = device.send_message(data)
                except:
                    h = 0
            return Response({'error':error,'id':Report.id})
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            report = api_models.Reports.objects.get(id = int(data['report_id']))
            report.delete()
        except:
            error = True
        return Response({'error':error})



class Notifications(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            user.notif_seen = True
            user.notif_count = 0
            user.save()
            data1 = models.Notifications.objects.filter(domain = user.domain)
            data = []
            for i in data1:
                if i.username == user:
                    data.append(i)
                    continue
                if user.branch in i.batch and i.year[user.year -1] == '1' and user.course in i.course and i.onlyUsername == False:
                    data.append(i)
            serializer = serializers.NotificationsSerializer(data,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            notif = models.Notifications()
            notif.username = user
            notif.domain = user.domain
            notif.title = data['title']
            notif.description = data['description']
            notif.batch = data['notif_branchs']
            notif.year = data['notif_year']
            notif.course = data['notif_courses']
            notif.save()
            user.notif_seen = False
            user.notif_count += 1
            user.save()

        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            notification = models.Notifications.objects.get(id = int(data['notification_id']))
            notification.delete()
        except:
            error = True
        return Response({'error':error})




class DATING_USER(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            data = models.DatingUser.objects.all()[:30]

            for i in data:
                try:
                    dating_user_reaction = models.DatingUserReactions.objects.get(username  = user,DatingUser = i)
                    i.is_reaction = dating_user_reaction.Reaction
                except:
                    i.is_reaction = 0

            serializer = serializers.DatingUserSerializer(data,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            try:
                datingUser = models.DatingUser.objects.get(username = user)
            except:
                datingUser = models.DatingUser()
            datingUser.username = user
            datingUser.dummyName = data['dummyName']
            datingUser.dummyProfile = ContentFile(base64.b64decode(data['file']),data['file_name'])
            datingUser.dummyBio = data['dummyBio']
            datingUser.dummyDomain = data['dummyDomain']
            datingUser.domain = user.domain
            datingUser.posted_date = timezone.now()
            datingUser.save()
            user.dating_profile = True
            user.save()

            datingUser.algoValue = (  datetime_weight * int(datingUser.posted_date.timestamp()) +
                                      like_weight * (datingUser.Reactions1_count + datingUser.Reactions2_count) +
                                      comment_weight * (datingUser.numChats) )

            datingUser.save()

        except:
            error = True
        return Response({'error':error})

    def patch(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            datingUser = models.DatingUser.objects.get(username = User.objects.get(email = data['dating_user_email']))
            datingUser.numChats += 1
            datingUser.algoValue = (  datetime_weight * int(datingUser.posted_date.timestamp()) +
                                      like_weight * (datingUser.Reactions1_count + datingUser.Reactions2_count) +
                                      comment_weight * (datingUser.numChats) )
            datingUser.save()
            datingUser = models.DatingUser.objects.get(username = user)
            datingUser.numChats += 1
            datingUser.algoValue = (  datetime_weight * int(datingUser.posted_date.timestamp()) +
                                      like_weight * (datingUser.Reactions1_count + datingUser.Reactions2_count) +
                                      comment_weight * (datingUser.numChats) )
            datingUser.save()


        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            datingUser = models.DatingUser.objects.get(username = user)
            datingUser.delete()
            user.dating_profile = False
            user.save()
        except:
            error = True
        return Response({'error':error})


    #FOR GETTING UUIDS TO PROFILES
    def put(self,request):
        error = False
        try:
            data = request.data
            datedUuids = data['datedUuids'].split('#')

            usersProfiles = []
            for i in datedUuids:
                usersProfiles.append(models.DatingUser.objects.get(username = User.objects.get(user_uuid = i)))
            serializer = serializers.DatingUserSerializer(usersProfiles,many = True)
            return Response(serializer.data)

        except:
            error = True
        return Response({'error':error})




class DATING_USER_REACTIONS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            dating_user = models.DatingUser.objects.get(username = User.objects.get(email = data['dating_user_email']))
            try:
                dating_user_reaction = models.DatingUserReactions.objects.get(username  = user,DatingUser = dating_user)
                if data['Reaction'] == 1:
                    dating_user.Reactions1_count += 1
                    dating_user.Reactions2_count -= 1
                elif data['Reaction'] == 2:
                    dating_user.Reactions2_count += 1
                    dating_user.Reactions1_count -= 1

            except:
                dating_user_reaction = models.DatingUserReactions()
                dating_user_reaction.DatingUser = dating_user
                dating_user_reaction.username = user
                if data['Reaction'] == 1:
                    dating_user.Reactions1_count += 1
                elif data['Reaction'] == 2:
                    dating_user.Reactions2_count += 1

            dating_user_reaction.Reaction = data['Reaction']
            dating_user_reaction.save()
            dating_user.save()


            dating_user.algoValue = (  datetime_weight * int(dating_user.posted_date.timestamp()) +
                                      like_weight * (dating_user.Reactions1_count + dating_user.Reactions2_count) +
                                      comment_weight * (dating_user.numChats) )
            dating_user.save()

        except:
            error = True
        return Response({'error':error})


















class TIME_TABLE(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
#         try:
#             timetable = api_models.Time_table.objects.all()
#             serializer = api_serializers.Time_tableSerializer(timetable,many = True)
#             #return Response([serializer.data,[]])


#             user = request.user
#             dates = {}
#             activities = models.Events.objects.all()
#             for i in activities:
#                 a = i.event_date
#                 if str(a)[:10] not in dates:
#                     dates[str(a)[:10]] = ""
#             cal_events =  models.CalenderEvents.objects.filter(username = user) | models.CalenderEvents.objects.filter(cal_event_type = "all")
#             for i in cal_events:
#                 if i.cal_event_type == "self":
#                     if str(i.event_date)[:10] not in dates:
#                         dates[str(i.event_date)[:10]] = ""
#                 elif (i.year[user.year - 1] == '1') and (user.branch in i.branch):
#                     if str(i.event_date)[:10] not in dates:
#                         dates[str(i.event_date)[:10]] = ""
#             final_dates = list(dates.keys())
#             final_dates.sort()
#             return Response([serializer.data,final_dates])
#         except:
#             error = True
#         return Response({'error':error})


#     def post(self,request):
#         error = False
#         try:
#             data = request.data
#             user = request.user
#             timetable = models.Time_table.objects.get(branch_name = data['branch_name'])
#             if data['day'] == "SUN":
#                 timetable.sun = data['day_timetable']
#             elif data['day'] == "MON":
#                 timetable.mon = data['day_timetable']
#             elif data['day'] == "TUE":
#                 timetable.tue = data['day_timetable']
#             elif data['day'] == "WED":
#                 timetable.wed = data['day_timetable']
#             elif data['day'] == "THU":
#                 timetable.thu = data['day_timetable']
#             elif data['day'] == "FRI":
#                 timetable.fri = data['day_timetable']
#             elif data['day'] == "SAT":
#                 timetable.sat = data['day_timetable']
#             timetable.save()

# #data["_lights"] set notif for edit true or false;
# #data['notif_id'] in i.notif_ids
#             year = data['branch_name'][2]
#             branch = data['branch_name'][0:2]
#             class_slots = data['class_slot_division'].split('&')
#             data1 = Message(
#             notification=Notification(title = class_slots[0] + "Timetable Update", body= "Faculty: " + class_slots[2] +"Class status: " + class_slots[4]),
#             #topic="Optional topic parameter: Whatever you want",
#             )
#             if data["_lights"] == "true":
#                 notif = models.Notifications()
#                 notif.username = user
#                 notif.title = class_slots[0] + "Timetable Update"
#                 notif.description = "Faculty: " + class_slots[2] +"Class status: " + class_slots[4]
#                 notif.branch = data['notif_id']
#                 notif.save()

#             users = User.objects.all()
#             for i in users:
#                 if (data['notif_id'] in i.notif_ids) and data["_lights"] == "true":
#                     i.notif_seen = False
#                     i.notif_count += 1
#                     i.save()
#                     if i.notif_settings[1] == '1' and i.token != "dfv":
#                         try:
#                             device = FCMDevice()
#                             device.registration_id  = i.token
#                             device.name = i.username
#                             device.save()
#                             device.send_message(data)
#                         except:
#                             try:
#                                 device = FCMDevice.objects.get(registration_id = i.token)
#                                 device.name = i.username
#                                 device.save()
#                                 device.send_message(data)
#                             except:
#                                 a = 10

#         except:
#             error = True
#         return Response({'error':error})



