from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
from django.db.models import Q
from django.utils.timezone import localtime


#        user = request.user
#        data = request.data
#        data = request.query_params



class SendNotifications(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def post(self,request):
        data = request.data
        data1 = Message(
            notification=Notification(title= data['title'], body= data['description'],image="https://testing5566.s3.amazonaws.com/pics/scaled_IMG-20230403-WA0019_nBt9IOM.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA33TUEPX6FOZRQ2MY%2F20230523%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20230523T083943Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d41894585e88878f4537f8a450c92a2f869e9b93cdbcf0396dc547574316dc63"),
            )
        users = User.objects.all()
        for i in users:
            if i.notif_settings[data['notiff_sett']] == '1' and i.token != "dfv":
                try:
                    device = FCMDevice()
                    device.registration_id  = i.token
                    device.name = i.username
                    device.type = i.platform
                    device.save()
                    device.send_message(data1)

                except:
                    try:
                        device = FCMDevice.objects.get(registration_id = i.token)
                        device.name = i.username
                        device.type = i.platform
                        device.save()
                        device.send_message(data1)
                    except:
                        a = 10
        return Response({"error":False})

    def put(self,request):
        user = request.user
        data = request.data
        data1 = Message(
            notification=Notification(title = user.email, body= "Gave Announcement : " + data['title'] + " : " + data['description']),
            #topic="Optional topic parameter: Whatever you want",
            )
        users = User.objects.all()
        for i in users:
            if data['notif_year'][user.year - 1] == "1" and (user.branch in data['notif_branchs']):
                i.notif_seen = False
                i.notif_count += 1
                i.save()
                if i.notif_settings[7] == '1' and i.token != "dfv":
                    try:
                        device = FCMDevice()
                        device.registration_id  = i.token
                        device.name = i.username
                        device.save()
                        device.send_message(data1)
                    except:
                        try:
                            device = FCMDevice.objects.get(registration_id = i.token)
                            device.name = i.username
                            device.save()
                            device.send_message(data1)
                        except:
                            a = 10
        return Response({"error":False})



class testing(APIView):
    def get(self,request):
        error = False
        password = ""
        try:
            user = User.objects.get(email = "guest@nitc.ac.in")
            user1 = User.objects.get(email = "testing5566@gmail.com")

            all_files = models.CalenderSubFiles.objects.all()



        except:
            error = True
        return Response({"error":error,"password":password})


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
        password = data['email'] + "1234"
        try:
            user = User.objects.get(email = data["email"])
            #try:
            #    if user.password == user.email + "1234":
            #        x = roll_num  + str(random.randint(100,10000))
            #        user.password1 = x
            #        user.password = x
            #        user.save()
            #        return Response({"error":False,"password":x})
            #    else:
            #        return Response({"error":False,"password":user.password1})
            #except:
            #    a = 0
            password = "@Vidyasag1234"   #data['email'] + "1234"
            return Response({"error":False,"password":user.password1})
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
            profile_pic = "static/profile.jpg"
            password = "@Vidyasag1234"        #email + "1234" #str(random.randint(10000,1000000))
            try:
                user = User.objects.create_user(email = email,username=username,password=password,password1=password,roll_num = roll_num.upper(),profile_pic = profile_pic)
            except:
                x = random.randint(0,10000)
                user = User.objects.create_user(email = email,username=username + "_" +  str(x) ,password=password,password1=password,roll_num = roll_num.upper(),profile_pic = profile_pic)
            return Response({"error":False,"password":password})
        return Response({"error":error,"password":password})



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
        data = request.query_params

        year  = 1
        branch = "ec"
        study = "n"
        years = {'23':1,'22':2,'21':3,'20':4}
        a = user.email
        a = a.split('_')
        if len(a) > 1:
            study = a[1][0]
            branch = a[1][7] + a[1][8]
            try:
                year = years[a[1][1]+a[1][2]]
            except:
                year = 1
        user.year = year
        user.branch = branch.upper()
        try:
            user.token = data['token']
            try:
                user.platform = data['platform']
            except:
                h = 2
        except:
            h = 2
        user.save()

        data = Message(
        notification=Notification(title= user.username + " LOGIN", body= user.username + " was successfully login in to NITC instabook app thak you.",image="https://testing5566.s3.amazonaws.com/pics/scaled_IMG-20230403-WA0019_nBt9IOM.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA33TUEPX6FOZRQ2MY%2F20230523%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20230523T083943Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d41894585e88878f4537f8a450c92a2f869e9b93cdbcf0396dc547574316dc63"),
        #topic="Optional topic parameter: Whatever you want",
        )
        #notifications().notifications(data,1)

        try:
            user1 = User.objects.get(username = "Testing user")
            device = FCMDevice()
            device.registration_id  = user1.token
            device.name = "Testing user"
            #device.save()
            #data = device.send_message(data)
        except:
            try:
                user1 = User.objects.get(username = "Testing user")
                device = FCMDevice.objects.get(registration_id = user1.token)
                device.name = "Testing user"
                #device.save()
                #data = device.send_message(data)
            except:
                h = 0

        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    def delete(self,request):
        error = False
        try:
            user = request.user
            user.file_type = '0'
            user.phn_num = "+91 000 000 0000"
            user.save()
        except:
            error = True
        return Response({'error':error})


class LST_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            try:
                data = request.query_params
                start = int(data['num_list'])
            except:
                start = 0
            user = request.user
            data1 = models.Lost_Found.objects.all()
            data1 = data1[start : 60 + start]
            data = []
            for i in data1:
                if user.email in i.lst_hiders:
                    continue
                data.append(i)
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
            if data['image_ratio'] == '1':
                lst.img = ContentFile(base64.b64decode(data['file']),data['file_name'])
            else:
                lst.img_ratio = 0.0
            lst.title = data['title']
            lst.tag = data['tag']
            lst.description = data['description']
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


    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            lst = models.Lost_Found.objects.get(id = int(data['lst_id']))
            lst.lst_hiders = lst.lst_hiders + user.email + "#"
            lst.save()
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
            data1 = serializer.data
            data1.reverse()
            return Response(data1)
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

            a = '''    data1 = Message(
            notification=Notification(title= user.email, body= " commented on your : " + LST_list.title + " : " + data['comment']),
            #topic="Optional topic parameter: Whatever you want",
            )
            try:
                user1 = LST_list.username
                device = FCMDevice()
                device.registration_id  = user1.token
                device.name = user1.username
                device.save()
                data = device.send_message(data1)
            except:
                try:
                    user1 = LST_list.username
                    device = FCMDevice.objects.get(registration_id = user1.token)
                    device.name = user1.username
                    device.save()
                    data = device.send_message(data1)
                except:
                    h = 0   '''
            return Response({'error':error,'id':new_comment.id,"not":"not sent"})
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
            post_list1 = models.PostTable.objects.all()
            post_list = []
            for i in post_list1:
                #if i.username.username == "Testing user" or i.username.username == "Testing User":
                #    continue
                if user.email in i.post_hiders:
                    continue
                post_list.append(i)
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
            final = serializer.data
            return Response(final)
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
            post.img_ratio = float(int(data['image_ratio']))
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


    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            post = models.PostTable.objects.get(id = int(data['post_id']))
            post.post_hiders = post.post_hiders + user.email + "#"
            post.save()
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
            data1 = serializer.data
            data1.reverse()
            return Response(data1)
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

            a = '''  data1 = Message(
            notification=Notification(title= user.email , body=  " commented on " + post_id.username.username  + " Post" + " : " + data['comment']),
            #topic="Optional topic parameter: Whatever you want",
            )

            try:
                user1 = post_id.username
                device = FCMDevice()
                device.registration_id  = user1.token
                device.name = user1.username
                device.save()
                data = device.send_message(data1)
            except:
                try:
                    user1 = post_id.username
                    device = FCMDevice.objects.get(registration_id = user1.token)
                    device.name = user1.username
                    device.save()
                    data = device.send_message(data1)
                except:
                    h = 0   '''

            return Response({'error':error,'id':post_cmnt.id})
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
            event.img_ratio = float(int(data['image_ratio']))
            event.event_date = data['event_date']
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

            try:
                data = Message(
                notification=Notification(title = event.title + " update ", body= data['event_update'])
                #topic="Optional topic parameter: Whatever you want",
                )
                #notifications().notifications(data,3)
            except:
                a=""
        except:
            error = True
        return Response({'error':error})


class ALERT_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data1 = models.Alerts.objects.all()
            user = request.user
            data = []
            for i in data1:
                if i.username == user:
                    data.append(i)
                    continue
                if user.branch in i.allow_branchs and i.allow_years[user.year -1] == '1':
                    data.append(i)
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
            if data['file_type'] != 0:
                alert.img = ContentFile(base64.b64decode(data['base64file']),data['fileName'])
                alert.img_ratio = float(data['file_type'])
            else:
                alert.img_ratio = 0.0
            alert.title = data['title']
            alert.description = data['description']
            alert.allow_branchs = data['allow_branchs']
            alert.allow_years = data['allow_years']
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
            user = request.user
            #LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            ALERT_list = models.Alerts.objects.get(id = int(data['alert_id']))
            comments1 = ALERT_list.alert_comment.all()
            comments = []
            for i in comments1:
                if i.username == user:
                    comments.append(i)
                    continue
                if user.branch in i.allow_branchs and i.allow_years[user.year -1] == '1':
                    comments.append(i)
            serializer = serializers.Alert_CommentsSerializer(comments,many = True)
            response = serializer.data
 #           response.reverse()
            return Response(response)
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
            if data['file_type'] != 0:
                new_comment.img = ContentFile(base64.b64decode(data['base64file']),data['fileName'])
                new_comment.img_ratio = float(data['file_type'])
            else:
                new_comment.img_ratio = 0.0
            new_comment.allow_branchs = data['allow_branchs']
            new_comment.allow_years = data['allow_years']
            new_comment.save()
            ALERT_list.save()

            return Response({'error':error,'id':new_comment.id})
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
            if data['image_type'] == "file":
                clubs_sports.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            clubs_sports.title = data['title']
            clubs_sports.club_r_sport = data['club_fest']
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
            if data['image_type'] == "file":
                clubs_sports.logo = ContentFile(base64.b64decode(data['file']),data['file_name'])
            clubs_sports.title = data['title']
            clubs_sports.club_r_sport = 'sport'
            clubs_sports.username = user
            clubs_sports.head = User.objects.get(email = data['email'])
            clubs_sports.team_members = data['team_members']
            clubs_sports.description = data['description']
            clubs_sports.websites = data['websites']
            clubs_sports.sport_ground = data['sport_ground']
            if data['image2_type'] == "file":
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

    # User Posts Data
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
            user.username = data['username']
            user.phn_num = data['phone_number']
            if data['file_type'] == '2':
                user.profile_pic = ContentFile(base64.b64decode(data['file']),data['file_name'])
                user.file_type = '1'
            user.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            user = request.user
            user.file_type = '0'
            user.save()
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


# using to get all subjects
class CALENDER_DATE_SUBS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            all_sub_names = models.CalenderSub.objects.filter(sub_id = data['sub_id'])
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
            sub = models.CalenderSub()
            sub.username = request.user
            sub.sub_name = data['sub_name']
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
            sub = models.CalenderSub.objects.get(id = int(data['sub_id']))
            sub.sub_name = data['sub_name']
            sub.save()

        except:
            error = True
        return Response({'error':error})




class CALENDER_SUB_YEARS(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            sub = models.CalenderSub.objects.get(id = int(data['sub_id']))
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
            sub = models.CalenderSub.objects.get(id = int(data['sub_id']))
            new_year = models.CalenderSubYears()
            new_year.username = request.user
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
            year = models.CalenderSubYears.objects.get(id = int(data['year_id']))
            year.year_name = data['year_name']
            year.private = data['private']
            year.save()

        except:
            error = True
        return Response({'error':error})






class CALENDER_SUB_FILES(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            data = request.query_params
            year = models.CalenderSubYears.objects.get(id = int(data['year_id']))
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
            qns_file  = models.CalenderSubFiles()
            qns_file.username = request.user
            year = models.CalenderSubYears.objects.get(id = data['year_id'])
            qns_file.year_id = year
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
            file = models.CalenderSubFiles.objects.get(id = int(data['id']))
            file.delete()
        except:
            error = True
        return Response({'error':error})

    def put(self,request):
        error = False
        try:
            data = request.data
            qns_file  = models.CalenderSubFiles.objects.get(id = int(data['id']))
            user = User.objects.get(email = data['file_email'])
            qns_file.username = user
            year = models.CalenderSubYears.objects.get(id = data['year_id'])
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
            sub = models.CalenderSub.objects.get(id = int(data['sub_id']))
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
                sub_name = models.CalenderSub.objects.get(id = int(data['sub_id']))
                rating  = models.Ratings.objects.get(username = user,sub_name = sub_name)
                sub_name.tot_ratings_val = sub_name.tot_ratings_val - rating.rating + data['rating']
                sub_name.save()
                rating.rating = data['rating']
                rating.save()
                return Response({'error':error,'id':rating.id})
            except:
                rating  = models.Ratings()
                rating.username = request.user
                sub_name = models.CalenderSub.objects.get(id = int(data['sub_id']))
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
            rating = models.Ratings.objects.get(id = int(data['id']))
            sub_name = rating.sub_name
            sub_name.tot_ratings_val -= rating.rating
            sub_name.num_ratings -= 1
            sub_name.save()
            rating.delete()
        except:
            error = True
        return Response({'error':error})


class CALENDER_EVENTS_list(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    #TO GET ALL EVENTS_DATES
    def patch(self,request):
        error = False
        try:
            user = request.user
            dates = {}
            #activities = models.Events.objects.all()
            #for i in activities:
            #    a = i.event_date
                #if str(a)[:10] not in dates:
            #    dates[str(a) +'&&'+ i.title] = ""
            cal_events =  models.CalenderEvents.objects.filter(username = user) | models.CalenderEvents.objects.filter(cal_event_type = "all")
            for i in cal_events:
                if i.cal_event_type == "self":
                    #if str(i.event_date)[:10] not in dates:
                    dates[str(i.event_date) +'&&'+ i.title ] = ""
                elif (i.year[user.year - 1] == '1') and (user.branch in i.branch):
                    #if str(i.event_date)[:10] not in dates:
                    dates[str(i.event_date) +'&&'+ i.title] = ""
            final_dates = list(dates.keys())
            final_dates.sort()
            return Response(final_dates)
        except:
            error = True
        return Response({'error':error})

    # TO GET INDUVIDUAL DATE EVENTS
    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            calender_date_events_self = models.CalenderEvents.objects.filter(username = user,cal_event_type = "self")
            calender_date_events_all = models.CalenderEvents.objects.filter(cal_event_type = "all")
            calender_date_events = []
            for i in calender_date_events_self:
                a = str(i.event_date)
                if a[:10] == data['calender_date']:
                    calender_date_events.append(i)
            for i in calender_date_events_all:
                a = str(i.event_date)
                if a[0:10] == data['calender_date'] and i.year[user.year - 1] == '1' and user.branch in i.branch:
                    calender_date_events.append(i)
            activities_all = models.Events.objects.all()
            date_activities = []
            for i in activities_all:
                a = str(i.event_date)[0:10]
                if a == data['calender_date']:
                    date_activities.append(i)
            event_serializer = serializers.EventsSerializer(date_activities,many = True)
            calender_date_serializer = serializers.CALENDER_EVENTSerializer(calender_date_events,many = True)

            return Response([event_serializer.data,calender_date_serializer.data])

        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            calander_event = models.CalenderEvents()
            calander_event.username = user
            calander_event.cal_event_type = data["cal_event_type"]
            calander_event.title = data['title']
            calander_event.description = data['description']
            if data['file_type'] != '0':
                calander_event.calender_date_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
            calander_event.file_type = data['file_type']
            calander_event.branch = data['branch']
            calander_event.year = data['year']
            calander_event.event_date = data['event_date']
            calander_event.save()
            return Response({'error':error,'id':calander_event.id})
        except:
            error = True
        return Response({'error':error,'id':0})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            message = models.CalenderEvents.objects.get(id = int(data['calender_event_id']))
            message.delete()
        except:
            error = True
        return Response({'error':error})

    def put(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            calander_event = models.CalenderEvents.objects.get(id = int(data['id']))
            calander_event.username = user
            calander_event.cal_event_type = data["cal_event_type"]
            calander_event.title = data['title']
            calander_event.description = data['description']
            if data['file_type'] != '0':
                calander_event.calender_date_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
            calander_event.file_type = data['file_type']
            calander_event.branch = data['branch']
            calander_event.year = data['year']
            calander_event.event_date = data['event_date']
            calander_event.save()
            return Response({'error':error,'id':calander_event.id,'date':calander_event.event_date})
        except:
            error = True
        return Response({'error':error,'id':0})


class TIME_TABLE(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            timetable = models.Time_table.objects.all()
            serializer = serializers.Time_tableSerializer(timetable,many = True)
            #return Response([serializer.data,[]])


            user = request.user
            dates = {}
            activities = models.Events.objects.all()
            for i in activities:
                a = i.event_date
                if str(a)[:10] not in dates:
                    dates[str(a)[:10]] = ""
            cal_events =  models.CalenderEvents.objects.filter(username = user) | models.CalenderEvents.objects.filter(cal_event_type = "all")
            for i in cal_events:
                if i.cal_event_type == "self":
                    if str(i.event_date)[:10] not in dates:
                        dates[str(i.event_date)[:10]] = ""
                elif (i.year[user.year - 1] == '1') and (user.branch in i.branch):
                    if str(i.event_date)[:10] not in dates:
                        dates[str(i.event_date)[:10]] = ""
            final_dates = list(dates.keys())
            final_dates.sort()
            return Response([serializer.data,final_dates])
        except:
            error = True
        return Response({'error':error})


    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
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

#data["_lights"] set notif for edit true or false;
#data['notif_id'] in i.notif_ids
            year = data['branch_name'][2]
            branch = data['branch_name'][0:2]
            class_slots = data['class_slot_division'].split('&')
            data1 = Message(
            notification=Notification(title = class_slots[0] + "Timetable Update", body= "Faculty: " + class_slots[2] +"Class status: " + class_slots[4]),
            #topic="Optional topic parameter: Whatever you want",
            )
            if data["_lights"] == "true":
                notif = models.Notifications()
                notif.username = user
                notif.title = class_slots[0] + "Timetable Update"
                notif.description = "Faculty: " + class_slots[2] +"Class status: " + class_slots[4]
                notif.branch = data['notif_id']
                notif.save()

            users = User.objects.all()
            for i in users:
                if (data['notif_id'] in i.notif_ids) and data["_lights"] == "true":
                    i.notif_seen = False
                    i.notif_count += 1
                    i.save()
                    if i.notif_settings[1] == '1' and i.token != "dfv":
                        try:
                            device = FCMDevice()
                            device.registration_id  = i.token
                            device.name = i.username
                            device.save()
                            device.send_message(data)
                        except:
                            try:
                                device = FCMDevice.objects.get(registration_id = i.token)
                                device.name = i.username
                                device.save()
                                device.send_message(data)
                            except:
                                a = 10

        except:
            error = True
        return Response({'error':error})





## EDIT NOTIFICATIONS AND NOTIFICATION SEEN

class EDIT_notif_settings(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]
    def post(self,request):
        error = False
        try:
            user = request.user
            data = request.data
            notif = data['notif_settings']
            index = data['index']
            settings = user.notif_settings
            user.notif_settings = settings[:int(index)] + notif + settings[int(index)+1:]
            user.save()
        except:
            error = True
        return Response({'error':error})

    def delete(self,request):
        error = False
        try:
            user = request.user
            user.notif_seen = True
            user.notif_count = 0
            user.save()
        except:
            error = True
        return Response({'error':error})

## EDIT NOTIFICATION IDS FOR TIME TABLES(BRANCHES AND ELECTIVES)

    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            user.notif_ids = data['notif_ids']
            user.save()
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
            data1 = models.Notifications.objects.all()
            data = []
            for i in data1:
                if i.username == user:
                    data.append(i)
                    continue
                if user.branch in i.allow_branchs and i.allow_years[user.year -1] == '1':
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
            notif.title = data['title']
            notif.description = data['description']
            notif.branch = data['notif_branchs']
            notif.year = data['notif_year']
            notif.save()

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


class Messanger(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            required = {}
            user_messages = models.Messanger.objects.filter(Q(message_sender=user) | Q(message_receiver=user))
            for i in user_messages:
                if i.message_sender == user:
                    if i.message_receiver in required:
                        continue
                    else:
                        required[i.message_receiver] = i
                else:
                    if i.message_sender in required:
                        continue
                    else:
                        required[i.message_sender] = i
            last_user_messages = required.keys()
            final_Response = []
            for j in last_user_messages:
                user_messages = models.Messanger.objects.filter((Q(message_sender=user) & Q(message_receiver=j)) | (Q(message_sender=j) & Q(message_receiver=user)))
                serializer = serializers.MessangerSerializer(user_messages,many = True)
                response = serializer.data
                response.reverse()
                final_Response.append(response)
            lens = data['exist_messages_list'].split(',')
            try:
                if data['exist_messages_list'] == "load":
                    return Response(final_Response)

                if len(final_Response) == len(lens):
                    for i in range(len(lens)):
                        if int(lens[i]) == len(final_Response[i]):
                            continue
                        else:
                            break
                    else:
                        return Response([])
            except:
                b = 0
            return Response(final_Response)
        except:
            error = True
        return Response({'error':error})

    def post(self,request):
        error = False
        try:
            data = request.data
            user = request.user
            recevier = User.objects.get(email = data['email'])
            message = models.Messanger()
            message.message_sender = user
            message.message_receiver = recevier
            message.message_body = data['message_body']
            message.messag_file_type = data['messag_file_type']
            if data['messag_file_type'] != '0':
                message.message_file = ContentFile(base64.b64decode(data['file']),data['file_name'])
                message.message_body_file = 'file'
            else:
                message.message_body_file = 'body'
            message.message_replyto = data['message_replyto']
            message.save()

            data1 = Message(
            notification=Notification(title = user.email, body= " sends a message : " + data['message_body']),
            #topic="Optional topic parameter: Whatever you want",
            )

            if recevier.notif_settings[8] == '1' and recevier.token != "dfv":
                try:
                    device = FCMDevice()
                    device.registration_id  = recevier.token
                    device.name = recevier.username
                    device.save()
                    device.send_message(data1)
                except:
                    try:
                        device = FCMDevice.objects.get(registration_id = recevier.token)
                        device.name = recevier.username
                        device.save()
                        device.send_message(data1)
                    except:
                        a = 10
            return Response({'error':error,'id':message.id})
        except:
            error = True
        return Response({'error':error,'id':''})

    def delete(self,request):
        error = False
        try:
            data = request.query_params
            message = models.Messanger.objects.get(id = int(data['message_id']))
            message.delete()
        except:
            error = True
        return Response({'error':error})


class USER_Messanger(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication,]

## NAME MATCH USERS

    def get(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            users_list = User.objects.filter(email__startswith = data['username_match']) | User.objects.filter(username__startswith = data['username_match']) | User.objects.filter(roll_num__startswith = data['username_match'])
            serializer = serializers.SmallUserSerializer(users_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({'error':error})

## USER TO USER MESSAGES

    def delete(self,request):
        error = False
        try:
            user = request.user
            data = request.query_params
            chatting_user = User.objects.get(email = data['chattinguser_email'])
            seen_messages = models.Messanger.objects.filter((Q(message_sender=chatting_user) & Q(message_receiver=user)))
            for i in seen_messages:
                i.message_seen = True
                i.save()
            user_messages = models.Messanger.objects.filter((Q(message_sender=user) & Q(message_receiver=chatting_user)) | (Q(message_sender=chatting_user) & Q(message_receiver=user)))
            serializer = serializers.MessangerSerializer(user_messages,many = True)
            response = serializer.data
            response.reverse()
            try:
                if data['ind_message_lenth'] == "load":
                    return Response(response)
                if int(data['ind_message_lenth']) == len(user_messages):
                    if (response[-1]['message_seen'] == True) and (data['last_msg_seen'] == 'false'):
                        return Response(response)
                    else:
                        return Response([])
                else:
                    return Response([])
            except:
                b = 0
            return Response(response)
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
            report = models.Reports.objects.get(id = int(data['report_id']))
            report.delete()
        except:
            error = True
        return Response({'error':error})































