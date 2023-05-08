from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
import base64
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User = get_user_model()
import random


#        user = request.user
#        data = request.data
#        data = request.query_params


class testing(APIView):
    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = User.objects.get(username = "VidyaSagar")
            data = user.post_table_username.all()
            serializer = serializers.PostTableSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})


    def post(self,request):
        error = False
        data = request.data
        user = User.objects.create_user(username=data["username"],password=data["password"])
        Token.objects.create(user=user)
        return Response({'error':error})

    def delete(self,request):
        error = False
        return Response({'error':error})


class Register_EMAIL_check(APIView):
    def get(self,request):
        error = False
        data = request.query_params
        try:
            user = User.objects.get(email = data["email"])
        except:
            email = data['email']
            lst = email.split('_')
            if len(lst) == 1:
                a = email.split('@')[0]
                username = a[0].upper() + a[1:]
                roll_num = "ADMIN"
            else:
                a = lst[0]
                username = a[0].upper() + a[1:]
                roll_num = email.split('_')[1][:9]
            password = email + "1234"
            profile_pic = "static/profile.jpg"
            try:
                user = User.objects.create_user(username=username,password=password,roll_num = roll_num.upper(),profile_pic = profile_pic)
            except:
                x = random.randint(0,10000)
                user = User.objects.create_user(username=username + "_" +  str(x) ,password=password,roll_num = roll_num.upper(),profile_pic = profile_pic)
            user.email = data['email']
            user.save()
        return Response({"error":error})



    def post(self,request):
        error = False
        try:
            data = request.data
            if data['key'] == "@Vidyasag5566":
                user = User.objects.create_user(username=data["username"],password=data["password"])
                Token.objects.create(user=user)
            else:
                error = True
        except:
            error = True
        return Response({'error':error})

class GET_user(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        user = request.user
#        user = User.objects.get(username = "VidyaSagar")
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def delete(self,request):
        error = False
        user = request.user
        user.high_lst_count = 0
        user.save()
        return Response({'error':error})


class LST_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = models.Lost_Found.objects.all()
            serializer = serializers.Lost_FoundSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            lst = models.Lost_Found()
            lst.username = user
            lst.title = data['title']
            lst.description = data['description']
            lst.img = ContentFile(base64.b64decode(data['file']),data['file_name'])
            lst.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            lst = models.Lost_Found.objects.get(id = int(data['lst_id']))
            lst.delete()
        except:
            error = True
        return Response({'error':error})


class LST_Comment_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            #LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            LST_list = models.Lost_Found.objects.get(id = int(data['lst_id']))
            comments = LST_list.lst_found_comment.all()
            serializer = serializers.LST_CommentsSerializer(comments,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            LST_list = models.Lost_Found.objects.get(id = int(data['lst_id']))
            new_comment = models.LST_Comments()
            new_comment.lst_cmnt_id = LST_list
            new_comment.Comment = data['comment']
            new_comment.username = user
            new_comment.save()
            LST_list.comment_count += 1
            LST_list.save()
        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error =  False
        try:
            data = request.query_params
            comment_list = models.LST_Comments.objects.get(id = int(data['lst_cmnt_id']))  # id is primary key of comments
            comment_list.delete()
            lst = models.Lost_Found.objects.get(id = int(data['lst_id']))
            lst.comment_count -= 1
            lst.save()
        except:
            error = True
        return Response({'error':error})

class POST_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            #user = User.objects.get(username = "srinivas")
            user = request.user
            post_list = models.PostTable.objects.all()
            for i in post_list:
                try:
                    like = models.post_Likes.objects.filter(post_id = i,username = user)
                    if len(like) >= 1:
                        i.is_like = True
                    elif len(like) > 1:
                        for i in range(len(like)-1):
                            i.delete()
                except:
                    i.is_like = False
            serializer = serializers.PostTableSerializer(post_list,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            post = models.PostTable()
            post.username = user
            post.description = data['description']
            post.img = ContentFile(base64.b64decode(data['file']),data['file_name'])
            post.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            post = models.PostTable.objects.get(id = int(data['post_id']))
            post.delete()
        except:
            error = True
        return Response({'error':error})


class PST_CMNT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            #post = models.PostTable.objects.get(id = "1")
            post = models.PostTable.objects.get(id = int(data['post_id']))
            pst_comments = post.post_comment.all()
            serializer = serializers.post_CommentsSerializer(pst_comments,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            post_cmnt = models.post_Comments()
            post_id = models.PostTable.objects.get(id = int(data['post_id']))
            post_cmnt.post_id = post_id
            post_cmnt.username = user
            post_cmnt.Comment = data['comment']
            post_cmnt.save()
            post_id.comment_count += 1
            post_id.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            post_cmnt = models.post_Comments.objects.get(id = int(data['cmnt_id']))
            post_cmnt.delete()
            post = models.PostTable.objects.get(id = int(data['post_id']))
            post.comment_count -= 1
            post.save()
        except:
            error = True
        return Response({'error':error})

class POST_LIKE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            post = models.PostTable.objects.get(id = int(data['post_id']))
            post_like = models.post_Likes()
            post_like.username = user
            post_like.post_id = post
            post_like.save()
            post.like_count += 1
            post.save()

        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            post = models.PostTable.objects.get(id = int(data['post_id']))
            try:
                like = models.post_Likes.objects.get(post_id = post,username = user)
                like.delete()
            except:
                like = models.post_Likes.objects.filter(post_id = post,username = user)
                for i in like:
                    i.delete()
            post.like_count -= 1
            post.save()
        except:
            error = True
        return Response({'error':error})


class EVENT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            #user = User.objects.get(id = "1")
            event_list = models.Events.objects.all()
            for i in event_list:
                try:
                    like = models.Event_likes.objects.filter(event_id = i,username = user)
                    if len(like) >= 1:
                        i.is_like = True
                    elif len(like) > 1:
                        for i in range(len(like)-1):
                            i.delete()
                except:
                    i.is_like = False
            serializer = serializers.EventsSerializer(event_list,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            event = models.Events()
            event.username = user
            event.title = data['title']
            event.description = data['description']
            event.event_img = ContentFile(base64.b64decode(data['file']),data['file_name'])
            event.save()

        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            event = models.Events.objects.get(id = int(data['event_id']))
            event.delete()
        except:
            error = True
        return Response({'error':error})

class EVENT_LIKE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            event = models.Events.objects.get(id = int(data['event_id']))
            event_like = models.Event_likes()
            event_like.username = user
            event_like.event_id = event
            event_like.save()
            event.like_count += 1
            event.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            event = models.Events.objects.get(id = int(data['event_id']))
            try:
                like = models.Event_likes.objects.get(username = user,event_id = event)
                like.delete()
            except:
                like = models.Event_likes.objects.filter(username = user,event_id = event)
                for i in like:
                    i.delete()
            event.like_count -= 1
            event.save()
        except:
            error = True
        return Response({'error':error})


    ## EVENT_UPDATE USING EVENT LIKE URL

    def get(self,request):
        error = False
        try:
            data = request.query_params
            event = models.Events.objects.get(id = int(data['event_id']))
            event.event_updates = data['event_update'] + "`" + event.event_updates
            event.save()
        except:
            error = True
        return Response({'error':error})


class ALERT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = models.Alerts.objects.all()
            serializer = serializers.AlertsSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            alert = models.Alerts()
            alert.username = user
            alert.title = data['title']
            alert.description = data['description']
            alert.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            alert = models.Alerts.objects.get(id = int(data['alert_id']))
            alert.delete()
        except:
            error = True
        return Response({'error':error})


class ALERT_CMNT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            #LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            ALERT_list = models.Alerts.objects.get(id = int(data['alert_id']))
            comments = ALERT_list.alert_comment.all()
            serializer = serializers.Alert_CommentsSerializer(comments,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error":error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            ALERT_list = models.Alerts.objects.get(id = int(data['alert_id']))
            ALERT_list.comment_count += 1
            new_comment = models.ALERT_Comments()
            new_comment.alert_cmnt_id  = ALERT_list
            new_comment.Comment = data['comment']
            new_comment.username = user
            new_comment.save()
            ALERT_list.save()
        except:
            error = True
        return Response({'error':error})


    def delete(self,request):
        error =  False
        try:
            data = request.query_params
            comment_list = models.ALERT_Comments.objects.get(id = int(data['alert_cmnt_id']))  # id is primary key of comments
            comment_list.delete()
            alert = models.Alerts.objects.get(id = int(data['alert_id']))
            alert.comment_count -= 1
            alert.save()
        except:
            error = True
        return Response({'error':error})



class CLUB_SPORT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    def get(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            #clubs_sports = models.Clubs_Sports.objects.filter(club_r_sport = 'sport')
            clubs_sports = models.Clubs_Sports.objects.filter(club_r_sport = data['club_sport'])
            for i in clubs_sports:
                try:
                    like = models.Clubs_Sports_likes.objects.filter(club_sport = i,username = user)
                    if len(like) >= 1:
                        i.is_like = True
                    elif len(like) > 1:
                        for i in range(len(like)-1):
                            i.delete()
                except:
                    i.is_like = False
            serializer = serializers.Clubs_SportsSerializer(clubs_sports,many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})
# edding only club

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            try:
                clubs_sports = models.Clubs_Sports.objects.get(username = user)
            except:
                clubs_sports = models.Clubs_Sports()
            clubs_sports.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            clubs_sports.title = data['title']
            clubs_sports.club_r_sport = 'club'
            clubs_sports.username = user
            clubs_sports.head = User.objects.get(email = data['email'])
            clubs_sports.team_members = data['team_members']
            clubs_sports.description = data['description']
            clubs_sports.websites = data['websites']
            clubs_sports.save()
        except:
            error = True
        return Response({'error':error})


# edditing only sport

class CLUB_SPORT_edit(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            clubs_sports = models.Clubs_Sports.objects.get(username = user)
            serializer = serializers.Clubs_SportsSerializer(clubs_sports,many=True)
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
                clubs_sports = models.Clubs_Sports.objects.get(username = user)
            except:
                clubs_sports = models.Clubs_Sports()
            clubs_sports.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            clubs_sports.title = data['title']
            clubs_sports.club_r_sport = 'sport'
            clubs_sports.username = user
            clubs_sports.head = User.objects.get(email = data['email'])
            clubs_sports.team_members = data['team_members']
            clubs_sports.description = data['description']
            clubs_sports.websites = data['websites']
            clubs_sports.sport_ground = data['sport_ground']
            clubs_sports.sport_ground_img = ContentFile(base64.b64decode(data['file1']),data['file_name1'])
            clubs_sports.save()
        except:
            error = True
        return Response({'error':error})



class CLUB_SPORT_like_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            club_sport = models.Clubs_Sports.objects.get(id = int(data['club_sport_id']))
            club_sport_like = models.Clubs_Sports_likes()
            club_sport_like.username = user
            club_sport_like.club_sport  = club_sport
            club_sport_like.save()
            club_sport.like_count += 1
            club_sport.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user
            club_sport = models.Clubs_Sports.objects.get(id = int(data['club_sport_id']))
            try:
                like = models.Clubs_Sports_likes.objects.get(username = user,club_sport = club_sport)
                like.delete()
            except:
                like = models.Clubs_Sports_likes.objects.filter(username = user,club_sport = club_sport)
                for i in like:
                    i.delete()
            club_sport.like_count -= 1
            club_sport.save()
        except:
            error = True
        return Response({'error':error})





class CLUB_SPORT_MEMB(APIView):

    def get(self,request):
        error = False
        try:
            data = request.query_params
            club_mem = data["team_mem"].split('#')
            club_mem_data = []
            for i in club_mem:
                try:
                    user = User.objects.get(email = i)
                    club_mem_data.append(user)
                except:
                    continue
            #user = User.objects.get(username = data['club_name'])
            #user = User.objects.get(username = "cricket")
            #club_files = user.post_table_username.all()
            serializer = serializers.UserSerializer(club_mem_data, many=True)

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
            serializer = serializers.PostTableSerializer(club_files, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


class PEOFILE_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            #user = request.user
            data = request.query_params
            user = User.objects.get(username = data['username'])
            post_list = user.post_table_username.all()
            for i in post_list:
                try:
                    like = models.post_Likes.objects.get(post_id = i,username = request.user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.PostTableSerializer(post_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

    # UPDATE PROFILE WITH IMAGE
    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            update_user = User.objects.get(username = user.username)
            update_user.username = data['username']
            update_user.phn_num = data['phone_number']
            update_user.profile_pic = ContentFile(base64.b64decode(data['file']),data['file_name'])
            update_user.high_lst_count = 1
            update_user.save()
        except:
            error = True
        return Response({'error':error})

    # NOT DELETE UPDATE PROFILE WITHOUT IMAGE

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            user = request.user

            user_id = Token.objects.get(key=request.auth.key).user_id
            User.objects.filter(id=user_id).update(username=data['username'],phn_num = data['phone_number'])


#            update_user = User.objects.get(username = user.username)
#            update_user.username = data['username']
#            update_user.phn_num = data['phone_number']
#            update_user.save()
        except:
            error = True
        return Response({'error':error})





class SAC_list(APIView):

    def get(self,request):
        error = False
        try:
            data = User.objects.filter(is_sac = True)
            serializer = serializers.UserSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})




class MESS_list(APIView):

    def get(self,requesr):
        error = False
        try:
            mess = models.Mess_table.objects.all()
            serializer = serializers.Mess_tableSerializer(mess,many = True)
            data = list(serializer.data)
            data.reverse()
            return Response(data)
        except:
            error = True
        return Response({'error':error})





class ACADEMIC_list(APIView):

    def get(self,requesr):
        error = False
        try:
            academic = models.Academic_table.objects.all()
            serializer = serializers.Academic_tableSerializer(academic,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


class TIMETABLE_list(APIView):

    def get(self,requesr):
        error = False
        try:
            timetable = models.Time_table.objects.all()
            serializer = serializers.Time_tableSerializer(timetable,many = True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            data = request.data
            timetable = models.Time_table.objects.get(branch_name = data['branch_name'])
            if data['day'] == "SUN":
                timetable.sun = data['day_timetable']
            elif data['day'] == "MON":
                timetable.mon = data['day_timetable']
            elif data['day'] == "TUE":
                timetable.tue = data['day_timetable']
            elif data['day'] == "WED":
                timetable.wed = data['day_timetable']
            elif data['day'] == "THU":
                timetable.thu = data['day_timetable']
            elif data['day'] == "FRI":
                timetable.fri = data['day_timetable']
            elif data['day'] == "SAT":
                timetable.sat = data['day_timetable']
            timetable.save()
        except:
            error = True
        return Response({'error':error})








    
