from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
import base64
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
from fcm_django.models import FCMDevice
from django.db.models import Q
from django.utils.timezone import localtime


#        user = request.user
#        data = request.data
#        data = request.query_params

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
                    like = models.Clubs_likes.objects.filter(club = i,username = user)
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
            new_club.name = data['name']
            new_club.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_club.title = data['title']
            new_club.domain = user.domain
            new_club.head = User.objects.get(email = data['email'])
            new_club.team_members = data['team_members']
            new_club.description = data['description']
            new_club.websites = data['websites']
            new_club.save()

        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            club = models.AllClubs.objects.get(id = data['id'])
            club.delete()

        except:
            error = True
        return Response({'error':error})



    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_club = models.AllClubs.objects.get(id = data['id'])
            new_club.name = data['name']
            new_club.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_club.title = data['title']
            new_club.domain = user.domain
            new_club.head = User.objects.get(email = data['email'])
            new_club.team_members = data['team_members']
            new_club.description = data['description']
            new_club.websites = data['websites']
            new_club.save()

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
            club = models.AllClubs.objects.get(id = int(data['AllClubs_id']))
            club_like = models.Clubs_likes()
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
            club = models.AllClubs.objects.get(id = int(data['AllClubs_id']))

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
                    like = models.Sports_likes.objects.filter(sport = i,username = user)
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
            new_sport.name = data['name']
            new_sport.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_sport.title = data['title']
            new_sport.domain = user.domain
            new_sport.head = User.objects.get(email = data['email'])
            new_sport.team_members = data['team_members']
            new_sport.description = data['description']
            new_sport.websites = data['websites']
            new_sport.sport_ground = data['sport_ground']
            new_sport.sport_ground_img = ContentFile(base64.b64decode(data['file1']),data['file_name1'])
            new_sport.img_ratio = data['img_ratio']
            new_sport.save()

        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            sport = models.AllSports.objects.get(id = data['id'])
            sport.delete()

        except:
            error = True
        return Response({'error':error})



    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_club = models.AllSports.objects.get(id = data['id'])
            new_sport.name = data['name']
            new_sport.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_sport.title = data['title']
            new_sport.domain = user.domain
            new_sport.head = User.objects.get(email = data['email'])
            new_sport.team_members = data['team_members']
            new_sport.description = data['description']
            new_sport.websites = data['websites']
            new_sport.sport_ground = data['sport_ground']
            new_sport.sport_ground_img = ContentFile(base64.b64decode(data['file1']),data['file_name1'])
            new_sport.img_ratio = data['img_ratio']
            new_sport.save()

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
            sport = models.AllSports.objects.get(id = int(data['AllSports_id']))
            sport_like = models.Sports_likes()
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
            sport = models.AllSports.objects.get(id = int(data['AllSports_id']))

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
                    like = models.Fests_likes.objects.filter(fest = i,username = user)
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
            new_fest.name = data['name']
            new_fest.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_fest.title = data['title']
            new_fest.domain = user.domain
            new_fest.head = User.objects.get(email = data['email'])
            new_fest.team_members = data['team_members']
            new_fest.description = data['description']
            new_fest.websites = data['websites']
            new_fest.save()

        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            fest = models.AllFests.objects.get(id = data['id'])
            fest.delete()

        except:
            error = True
        return Response({'error':error})



    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data

            new_fest = models.AllFests.objects.get(id = data['id'])
            new_fest.name = data['name']
            new_fest.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            new_fest.title = data['title']
            new_fest.domain = user.domain
            new_fest.head = User.objects.get(email = data['email'])
            new_fest.team_members = data['team_members']
            new_fest.description = data['description']
            new_fest.websites = data['websites']
            new_fest.save()

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
            fest = models.AllFests.objects.get(id = int(data['AllFests_id']))
            fest_like = models.Fests_likes()
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
            fest = models.AllFests.objects.get(id = int(data['AllFests_id']))

            like = models.Fests_likes.objects.get(username = user,fest = fest)
            like.delete()

            fest.like_count -= 1
            fest.save()
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
            serializer = serializers.UserSerializer(team_mem_data, many=True)

            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = User.objects.get(username = data['club_sport'])
            #user = User.objects.get(username = "cricket")
            club_files = user.post_table_username.all()
            serializer = api_serializers.PostTableSerializer(club_files, many=True)
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
                all_sub_names = api_models.BranchSub.objects.filter(sub_id = data['sub_id'])
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
            data = request.data
            sub = api_models.BranchSub()
            sub.username = request.user
            sub.sub_name = data['sub_name']
            sub.domain = user.domain
            sub.sub_id = data['sub_id']
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
            sub_years = sub.CalenderSub.all()
            serializer = serializers.CalenderSubYearsSerializer(sub_years,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            data = request.data
            sub = api_models.BranchSub.objects.get(id = int(data['sub_id']))
            new_year = api_models.BranchSubYears()
            new_year.username = request.user
            new_year.domain = user.domain
            new_year.sub_name = sub
            new_year.year_name = data['year_name']
            new_year.private = data['private']
            new_year.save()
            return Response({'error':error,'id':new_year.id})
        except:
            error = True
        return Response({'error':error,'id':'-1'})


    def put(self,request):
        error = False
        try:
            data = request.data
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
            qns_file  = api_models.BranchSubFiles()
            qns_file.username = request.user
            year = api_models.BranchSubYears.objects.get(id = data['year_id'])
            qns_file.year_id = year
            qns_file.domain = user.domain
            qns_file.description = data['description']
            qns_file.qn_ans_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
            qns_file.file_type = data['file_type']
            qns_file.file_name = data['file_name']
            qns_file.save()
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
            sub = api_models.CalenderSub.objects.get(id = int(data['sub_id']))
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
                sub_name = api_models.CalenderSub.objects.get(id = int(data['sub_id']))
                rating  = api_models.Ratings.objects.get(username = user,sub_name = sub_name)
                sub_name.tot_ratings_val = sub_name.tot_ratings_val - rating.rating + data['rating']
                sub_name.save()
                rating.domain = user.domain
                rating.rating = data['rating']
                rating.save()
                return Response({'error':error,'id':rating.id})
            except:
                rating  = api_models.Ratings()
                rating.username = request.user
                sub_name = api_models.CalenderSub.objects.get(id = int(data['sub_id']))
                sub_name.tot_ratings_val += data['rating']
                sub_name.num_ratings += 1
                sub_name.save()
                rating.sub_name = sub_name
                rating.rating = data['rating']
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






class SAC_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data1 = request.query_params
            data = User.objects.filter(is_admin = True,domain = data1['domain'])
            serializer = serializers.UserSerializer(data, many=True)
            return Response(serializer.data)
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




class SECURITY(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            Report = api_models.Reports()
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



