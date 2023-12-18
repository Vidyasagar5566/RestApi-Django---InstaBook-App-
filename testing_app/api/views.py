from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
import base64
from . import serializers
from . import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
import random
import uuid
from firebase_admin.messaging import Message, Notification
from firebase_admin import messaging
from fcm_django.models import FCMDevice
from django.db.models import Q
from django.utils.timezone import localtime
from api2 import models as api2_models
from api2 import serializers as api2_serializers
from api2 import views as api2_views


#        user = request.user
#        data = request.data
#        data = request.query_params


datetime_weight = 0.6
like_weight = 0.2
comment_weight = 0.3

domains = {
    "nitt.": "@nitt.edu",
    "nitk.": "@nitk.edu.in",
    "nitrkl.": "@nitrkl.ac.in",
    "nitw.": "@nitw.ac.in",
    "nitc.": "@nitc.ac.in",
    "vnit.": "@vnit.ac.in",
    "nitdgp.": "@nitdgp.ac.in",
    "nits.": "@nits.ac.in",
    "mnit.": "@mnit.ac.in",
    "mnnit.": "@mnnit.ac.in",
    "nitkkr.": "@nitkkr.ac.in",
    "nitj.": "@nitj.ac.in",
    "svnit.": "@svnit.ac.in",
    "nitm.": "@nitm.ac.in",
    "nitp.": "@nitp.ac.in",
    "nitrr.": "@nitrr.ac.in",
    "nitsri.": "@nitsri.ac.in",
    "manit.": "@manit.ac.in",
    "nita.": "@nita.ac.in",
    "nitgoa.": "@nitgoa.ac.in",
    "nitjsr.": "@nitjsr.ac.in",
    "nitmanipur.": "@nitmanipur.ac.in",
    "nith.": "@nith.ac.in",
    "nituk.": "@nituk.ac.in",
    "nitpy.": "@nitpy.ac.in",
    "nitap.": "@nitap.ac.in",
    "nitsikkim.": "@nitsikkim.ac.in",
    "nitdelhi.": "@nitdelhi.ac.in",
    "nitmz.": "@nitmz.ac.in",
    "nitnagaland.": "@nitnagaland.ac.in",
    "nitandhra.": "@nitandhra.ac.in",
    "iitm.": "@iitm.ac.in",
    "iitd.": "@iitd.ac.in",
    "iitb.": "@iitb.ac.in",
    "iitk.": "@iitk.ac.in",
    "iitr.": "@iitr.ac.in",
    "iitkgp.": "@iitkgp.ac.in",
    "iitg.": "@iitg.ac.in",
    "iith.": "@iith.ac.in",
    "iitbhu.": "@iitbhu.ac.in",
    "iitism.": "@iitism.ac.in",
    "iiti.": "@iiti.ac.in",
    "iitrpr.": "@iitrpr.ac.in",
    "iitmandi.": "@iitmandi.ac.in",
    "iitgn.": "@iitgn.ac.in",
    "iitj.": "@iitj.ac.in",
    "iitp.": "@iitp.ac.in",
    "iitbbs.": "@iitbbs.ac.in",
    "iittp.": "@iittp.ac.in",
    "iitpkd.": "@iitpkd.ac.in",
    "iitjammu.": "@iitjammu.ac.in",
    "iitdh.": "@iitdh.ac.in",
    "iitbhilai.": "@iitbhilai.ac.in",
}


domains1 = {
    "nitt.edu": "Nit Trichy",
    "nitk.edu.in": "Nit Surathkal",
    "nitrkl.ac.in": "Nit Rourkela",
    "nitw.ac.in": "Nit Warangal",
    "nitc.ac.in": "Nit Calicut",
    "vnit.ac.in": "Nit Nagpur",
    "nitdgp.ac.in": "Nit Durgapur",
    "nits.ac.in": "Nit Silchar",
    "mnit.ac.in": "Nit Jaipur",
    "mnnit.ac.in": "Nit Allahabad",
    "nitkkr.ac.in": "Nit Kurukshetra",
    "nitj.ac.in": "Nit Jalandhar",
    "svnit.ac.in": "Nit Surat",
    "nitm.ac.in": "Nit Meghalaya",
    "nitp.ac.in": "Nit Patna",
    "nitrr.ac.in": "Nit Raipur",
    "nitsri.ac.in": "Nit Srinagar",
    "manit.ac.in": "Nit Bhopal",
    "nita.ac.in": "Nit Agarthala",
    "nitgoa.ac.in": "Nit Goa",
    "nitjsr.ac.in": "Nit Jamshedpur",
    "nitmanipur.ac.in": "Nit Manipur",
    "nith.ac.in": "Nit Hamipur",
    "nituk.ac.in": "Nit Uttarakhand",
    "nitpy.ac.in": "Nit Puducherry",
    "nitap.ac.in": "Nit ArunaChalPradesh",
    "nitsikkim.ac.in": "Nit Sikkim",
    "nitdelhi.ac.in": "Nit Delhi",
    "nitmz.ac.in": "Nit Mizoram",
    "nitnagaland.ac.in": "Nit Nagaland",
    "nitandhra.ac.in": "Nit AndhraPradesh",
    ##IITS
    "iitm.ac.in": "IIT Madras",
    "iitd.ac.in": "IIT Delhi",
    "iitb.ac.in": "IIT Bombay",
    "iitk.ac.in": "IIT Kanpur",
    "iitr.ac.in": "IITR Rookee",
    "iitkgp.ac.in": "IIT Kharagpur",
    "iitg.ac.in": "IIT Guwahati",
    "iith.ac.in": "IIT Hyderabad",
    "iitbhu.ac.in": "IIT BHU",
    "iitism.ac.in": "IIT ISM Dhanbad",
    "iiti.ac.in": "IIT Indore",
    "iitrpr.ac.in": "IIT Rupar",
    "iitmandi.ac.in": "IIT Mandi",
    "iitgn.ac.in": "IIT Gandhinagar",
    "iitj.ac.in": "IIT Jodhpur",
    "iitp.ac.in": "IIT Patna",
    "iitbbs.ac.in": "IIT Bhubaneswar",
    "iittp.ac.in": "IIT Tirupati",
    "iitpkd.ac.in": "IIT Palakkad",
    "iitjammu.ac.in": "IIT Jammu",
    "iitdh.ac.in": "IIT Dharwad",
    "iitbhilai.ac.in": "IIT Bhilai",
}


class testing(APIView):
    def get(self, request):
        error = False
        password = ""
        try:
            users = User.objects.all()
            # for i in users:
            #     if i.platform == "android":
            #         i.update_mark = "instabook4"
            #         i.save()

        except:
            error = True
        return Response({"error": error, "password": password})


class Register_EMAIL_check(APIView):
    # USER LOGIN CHECK OF ACCOUNT AND CREATION
    def get(self, request):
        error = False
        data = request.query_params
        password = data["email"] + "1234"
        try:
            user = User.objects.get(email=data["email"])
            return Response({"error": False, "password": user.password1})
        except:
            email = data["email"]
            check_email = email.split("@")
            username = email.split("@")[0]

            for i in domains:
                if i in check_email[1]:
                    password = username + str(random.randint(100, 1000000))
                    try:
                        user = User.objects.create_user(
                            email=email,
                            username=username,
                            password=password,
                            password1=password,
                            domain=domains[i],
                        )
                        try:
                            notif_filter = models.FilterNotifications()
                            notif_filter.username = user
                            notif_filter.domain = user.domain
                            notif_filter.save()
                        except:
                            a = 0
                    except:
                        x = random.randint(0, 10000)
                        user = User.objects.create_user(
                            email=email,
                            username=username + "_" + str(x),
                            password=password,
                            password1=password,
                            domain=domains[i],
                        )
                        try:
                            notif_filter = models.FilterNotifications()
                            notif_filter.username = user
                            notif_filter.domain = user.domain
                            notif_filter.save()
                        except:
                            a = 0
                    return Response({"error": False, "password": user.password1})
            else:
                return Response({"error": True, "password": "email_desnt match"})
        return Response({"error": True, "password": password})

    # USER REGISTER FIRST TIME
    def post(self, request):
        error = False
        try:
            data = request.data
            user = User.objects.get(email=data["email"])
            user.username = data["username"]
            user.branch = data["branch"]
            user.course = data["course"]
            user.year = data["year"]
            user.is_details = True
            user.save()
        except:
            error = True
        return Response({"error": error})

    # USER MARK UPDATE
    def put(self, request):
        error = False
        try:
            data = request.data
            user = User.objects.get(email=data["email"])
            user.user_mark = data["user_mark"]
            user.star_mark = data["star_mark"]
            user.is_admin = data["is_admin"]
            user.is_student_admin = data["is_student_admin"]
            user.save()
        except:
            error = True
        return Response({"error": error})


class GET_token(APIView):
    def post(self, request):
        error = False
        try:
            data = request.data
            user = User.objects.get(
                email=data["username"]
            )  # authenticate(email=data['username'], password=data['password'])
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})
        except:
            error = True
        return Response({"error": error})


class GET_user(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        user = request.user
        data = request.query_params
        try:
            user.token = data["token"]
            user.platform = data["platform"]
            notif_filter = models.FilterNotifications.objects.get(username=user)
            notif_filter.fcm_token = data["token"]
            notif_filter.save()
        except:
            h = 2
        if data["platform"] == "android":
            user.update_mark = "instabook4"
        else:
            user.update_mark = "instabook4"
        user.save()

        if data["email"] != "":
            user = User.objects.get(email=data["email"])

        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


## EDIT NOTIFICATIONS AND NOTIFICATION SEEN


class EDIT_notif_settings(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            user = request.user
            notif_sett = models.FilterNotifications.objects.get(username=user)
            serializer = serializers.FilterNotificationsSerializer(
                [notif_sett], many=True
            )
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            notif_sett = models.FilterNotifications.objects.get(username=user)
            notif_sett.lst_buy = data["lst_buy"]
            notif_sett.posts = data["posts"]
            notif_sett.posts_admin = data["posts_admin"]
            notif_sett.events = data["events"]
            notif_sett.threads = data["threads"]
            notif_sett.comments = data["comments"]
            notif_sett.announcements = data["announcements"]
            notif_sett.messanger = data["messanger"]
            notif_sett.save()
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            user = request.user
            user.notif_seen = True
            user.notif_count = 0
            user.save()
        except:
            error = True
        return Response({"error": error})


class LST_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            start = int(data["num_list"])

            user = request.user
            data1 = []

            if data["email"] == "":
                if data["category"] == "All":
                    if data["tag"] == "All":
                        data1 = models.Lost_Found.objects.filter(
                            domain=data["domain"], tag="lost"
                        ) | models.Lost_Found.objects.filter(
                            domain=data["domain"], tag="found"
                        )
                    else:
                        data1 = models.Lost_Found.objects.filter(
                            domain=data["domain"], tag=data["tag"]
                        )
                else:
                    if data["tag"] == "All":
                        data1 = models.Lost_Found.objects.filter(
                            domain=data["domain"], tag="lost", category=data["category"]
                        ) | models.Lost_Found.objects.filter(
                            domain=data["domain"],
                            tag="found",
                            category=data["category"],
                        )
                    else:
                        data1 = models.Lost_Found.objects.filter(
                            domain=data["domain"],
                            tag=data["tag"],
                            category=data["category"],
                        )

            else:
                profile_user = User.objects.get(email=data["email"])
                if data["category"] == "All":
                    if data["tag"] == "All":
                        data1 = models.Lost_Found.objects.filter(
                            username=profile_user, tag="lost"
                        ) | models.Lost_Found.objects.filter(
                            username=profile_user, tag="found"
                        )
                    else:
                        data1 = models.Lost_Found.objects.filter(
                            username=profile_user, tag=data["tag"]
                        )
                else:
                    if data["tag"] == "All":
                        data1 = models.Lost_Found.objects.filter(
                            username=profile_user, tag="lost", category=data["category"]
                        ) | models.Lost_Found.objects.filter(
                            username=profile_user,
                            tag="found",
                            category=data["category"],
                        )
                    else:
                        data1 = models.Lost_Found.objects.filter(
                            username=profile_user,
                            tag=data["tag"],
                            category=data["category"],
                        )

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
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            lst = models.Lost_Found()
            lst.username = user
            if data["image_ratio"] == "1":
                lst.img = ContentFile(base64.b64decode(data["file"]), data["file_name"])
            else:
                lst.img_ratio = 0.0
            lst.domain = user.domain
            lst.title = data["title"]
            lst.tag = data["tag"]
            lst.category = data["category"]
            lst.description = data["description"]
            lst.domain = user.domain
            lst.save()
            if data["tag"] == "lost" or data["tag"] == "found":
                user.lst_count += 1
            else:
                user.buy_count += 1
            user.save()

        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            lst = models.Lost_Found.objects.get(id=int(data["lst_id"]))
            lst.delete()
            user.lst_count -= 1
            user.save()

        except:
            error = True
        return Response({"error": error})

    def put(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            lst = models.Lost_Found.objects.get(id=int(data["lst_id"]))
            lst.lst_hiders = lst.lst_hiders + user.email + "#"
            lst.save()
        except:
            error = True
        return Response({"error": error})


class LST_Comment_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            # LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            LST_list = models.Lost_Found.objects.get(id=int(data["lst_id"]))
            comments = LST_list.lst_found_comment.all()
            serializer = serializers.LST_CommentsSerializer(comments, many=True)
            data1 = serializer.data
            data1.reverse()
            return Response(data1)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            LST_list = models.Lost_Found.objects.get(id=int(data["lst_id"]))
            new_comment = models.LST_Comments()
            new_comment.lst_cmnt_id = LST_list
            new_comment.domain = user.domain
            new_comment.Comment = data["comment"]
            new_comment.username = user
            new_comment.save()
            new_comment.domain = user.domain
            LST_list.comment_count += 1
            LST_list.save()

            api2_views.bulk_notifications(
                [LST_list.username.token],
                user.email,
                ": Requested " + data["comment"] + " for Your: " + LST_list.title,
            )

            notif = api2_models.Notifications()
            notif.username = LST_list.username
            notif.domain = LST_list.username.domain
            notif.title = user.email + " : send a request for " + LST_list.title
            notif.description = data["comment"]
            notif.onlyUsername = True
            notif.save()

            lstUser = LST_list.username
            lstUser.notif_seen = False
            lstUser.notif_count += 1
            lstUser.save()

            return Response({"error": error, "id": new_comment.id, "not": "not sent"})
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            comment_list = models.LST_Comments.objects.get(
                id=int(data["lst_cmnt_id"])
            )  # id is primary key of comments
            comment_list.delete()
            lst = models.Lost_Found.objects.get(id=int(data["lst_id"]))
            lst.comment_count -= 1
            lst.save()
        except:
            error = True
        return Response({"error": error})


class BS_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            start = int(data["num_list"])

            user = request.user
            data1 = []

            if data["email"] == "":
                if data["category"] == "All":
                    if data["tag"] == "All":
                        data1 = models.Buy_Sell.objects.filter(
                            domain=data["domain"], tag="buy"
                        ) | models.Buy_Sell.objects.filter(
                            domain=data["domain"], tag="sell"
                        )
                    else:
                        data1 = models.Buy_Sell.objects.filter(
                            domain=data["domain"], tag=data["tag"]
                        )
                else:
                    if data["tag"] == "All":
                        data1 = models.Buy_Sell.objects.filter(
                            domain=data["domain"], tag="buy", category=data["category"]
                        ) | models.Buy_Sell.objects.filter(
                            domain=data["domain"], tag="sell", category=data["category"]
                        )
                    else:
                        data1 = models.Buy_Sell.objects.filter(
                            domain=data["domain"],
                            tag=data["tag"],
                            category=data["category"],
                        )

            else:
                profile_user = User.objects.get(email=data["email"])
                if data["category"] == "All":
                    if data["tag"] == "All":
                        data1 = models.Buy_Sell.objects.filter(
                            username=profile_user, tag="buy"
                        ) | models.Buy_Sell.objects.filter(
                            username=profile_user, tag="sell"
                        )
                    else:
                        data1 = models.Buy_Sell.objects.filter(
                            username=profile_user, tag=data["tag"]
                        )
                else:
                    if data["tag"] == "All":
                        data1 = models.Buy_Sell.objects.filter(
                            username=profile_user, tag="buy", category=data["category"]
                        ) | models.Buy_Sell.objects.filter(
                            username=profile_user, tag="sell", category=data["category"]
                        )
                    else:
                        data1 = models.Buy_Sell.objects.filter(
                            username=profile_user,
                            tag=data["tag"],
                            category=data["category"],
                        )
            data1 = data1[start : 60 + start]
            data = []
            for i in data1:
                if user.email in i.lst_hiders:
                    continue
                data.append(i)
            serializer = serializers.Buy_SellSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            lst = models.Buy_Sell()
            lst.username = user
            if data["image_ratio"] == "1":
                lst.img = ContentFile(base64.b64decode(data["file"]), data["file_name"])
            else:
                lst.img_ratio = 0.0
            lst.domain = user.domain
            lst.title = data["title"]
            lst.tag = data["tag"]
            lst.category = data["category"]
            lst.description = data["description"]
            lst.domain = user.domain
            lst.save()
            if data["tag"] == "lost" or data["tag"] == "found":
                user.lst_count += 1
            else:
                user.buy_count += 1
            user.save()

        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            lst = models.Buy_Sell.objects.get(id=int(data["lst_id"]))
            lst.delete()
            user.buy_count -= 1
            user.save()

        except:
            error = True
        return Response({"error": error})

    def put(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            lst = models.Buy_Sell.objects.get(id=int(data["lst_id"]))
            lst.lst_hiders = lst.lst_hiders + user.email + "#"
            lst.save()
        except:
            error = True
        return Response({"error": error})


class BS_Comment_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            # LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            BS_list = models.Buy_Sell.objects.get(id=int(data["lst_id"]))
            comments = BS_list.buy_sell_comment.all()
            serializer = serializers.BS_CommentsSerializer(comments, many=True)
            data1 = serializer.data
            data1.reverse()
            return Response(data1)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            LST_list = models.Buy_Sell.objects.get(id=int(data["lst_id"]))
            new_comment = models.BS_Comments()
            new_comment.bs_cmnt_id = LST_list
            new_comment.domain = user.domain
            new_comment.Comment = data["comment"]
            new_comment.username = user
            new_comment.save()
            new_comment.domain = user.domain
            LST_list.comment_count += 1
            LST_list.save()

            api2_views.bulk_notifications(
                [LST_list.username.token],
                user.email,
                ": Requested " + data["comment"] + " for Your: " + LST_list.title,
            )

            notif = api2_models.Notifications()
            notif.username = LST_list.username
            notif.domain = LST_list.username.domain
            notif.title = user.email + " : send a request for " + LST_list.title
            notif.description = data["comment"]
            notif.onlyUsername = True
            notif.save()

            lstUser = LST_list.username
            lstUser.notif_seen = False
            lstUser.notif_count += 1
            lstUser.save()

            return Response({"error": error, "id": new_comment.id, "not": "not sent"})
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            comment_list = models.BS_Comments.objects.get(
                id=int(data["lst_cmnt_id"])
            )  # id is primary key of comments
            comment_list.delete()
            lst = models.Buy_Sell.objects.get(id=int(data["lst_id"]))
            lst.comment_count -= 1
            lst.save()
        except:
            error = True
        return Response({"error": error})


class POST_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            start = int(data["num_list"])
            user = request.user
            post_list1 = []
            try:
                if data["admin_posts"] == "true":
                    post_list2 = models.PostTable.objects.filter(domain=user.domain)
                    for i in post_list2:
                        if i.username.is_admin == True:
                            post_list1.append(i)
                elif data["domain"] == "All":
                    post_list1 = models.PostTable.objects.filter(
                        all_universities=True
                    ) | models.PostTable.objects.filter(
                        all_universities=False, domain=user.domain
                    )
                else:
                    if user.domain == data["domain"]:
                        post_list1 = models.PostTable.objects.filter(
                            domain=data["domain"]
                        )
                    else:
                        post_list1 = models.PostTable.objects.filter(
                            domain=data["domain"], all_universities=True
                        )
            except:
                if data["domain"] == "All":
                    post_list1 = models.PostTable.objects.filter(all_universities=True)
                else:
                    if user.domain == data["domain"]:
                        post_list1 = models.PostTable.objects.filter(
                            domain=data["domain"]
                        )
                    else:
                        post_list1 = models.PostTable.objects.filter(
                            domain=data["domain"], all_universities=True
                        )
            post_list1 = post_list1[start : 10 + start]
            post_list = []
            for i in post_list1:
                if user.email in i.post_hiders:
                    continue
                post_list.append(i)
            for i in post_list:
                try:
                    like = models.post_Likes.objects.filter(post_id=i, username=user)
                    if len(like) >= 1:
                        i.is_like = True
                    elif len(like) > 1:
                        for i in range(len(like) - 1):
                            i.delete()
                except:
                    i.is_like = False
            serializer = serializers.PostTableSerializer(post_list, many=True)
            final = serializer.data
            return Response(final)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            post = models.PostTable()
            post.username = user
            post.domain = user.domain
            post.description = data["description"]
            if data["image_ratio"] != "0":
                post.img = ContentFile(
                    base64.b64decode(data["file"]), data["file_name"]
                )
            post.img_ratio = float(int(data["image_ratio"]))
            post.all_universities = data["is_all_university"]

            if data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                club.post_count += 1
                club.save()
                post.club = club
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                sport.post_count += 1
                sport.save()
                post.sport = sport
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                fest.post_count += 1
                fest.save()
                post.fest = fest
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                fest.post_count += 1
                fest.save()
                post.sac = sac
            else:
                user.post_count += 1
                user.save()
            post.category = data["category"]
            post.domain = user.domain

            post.algoValue = (
                datetime_weight * int(post.posted_date.timestamp())
                + like_weight * (post.like_count)
                + comment_weight * (post.comment_count)
            )

            post.save()
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            user.post_count -= 1
            post.delete()
            user.save()
        except:
            error = True
        return Response({"error": error})

    def put(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            post.post_hiders = post.post_hiders + user.email + "#"
            post.save()
        except:
            error = True
        return Response({"error": error})


class PST_CMNT_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            # post = models.PostTable.objects.get(id = "1")
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            pst_comments = post.post_comment.all()
            serializer = serializers.post_CommentsSerializer(pst_comments, many=True)
            data1 = serializer.data
            data1.reverse()
            return Response(data1)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            post_cmnt = models.post_Comments()
            post_id = models.PostTable.objects.get(id=int(data["post_id"]))
            post_cmnt.post_id = post_id
            post_cmnt.username = user
            post_cmnt.domain = user.domain
            post_cmnt.Comment = data["comment"]
            post_cmnt.save()
            post_id.comment_count += 1
            post_id.algoValue = (
                datetime_weight * int(post_id.posted_date.timestamp())
                + like_weight * (post_id.like_count)
                + comment_weight * (post_id.comment_count)
            )
            post_id.save()

            return Response({"error": error, "id": post_cmnt.id})
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            post_cmnt = models.post_Comments.objects.get(id=int(data["cmnt_id"]))
            post_cmnt.delete()
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            post.comment_count -= 1
            post.algoValue = (
                datetime_weight * int(post.posted_date.timestamp())
                + like_weight * (post.like_count)
                + comment_weight * (post.comment_count)
            )
            post.save()
        except:
            error = True
        return Response({"error": error})


class POST_LIKE_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def post(self, request):
        error = False
        try:
            data = request.data
            user = request.user
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            post_like = models.post_Likes()
            post_like.username = user
            post_like.post_id = post
            post_like.domain = user.domain
            post_like.save()
            post.like_count += 1
            post.algoValue = (
                datetime_weight * int(post.posted_date.timestamp())
                + like_weight * (post.like_count)
                + comment_weight * (post.comment_count)
            )
            post.save()

        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            post = models.PostTable.objects.get(id=int(data["post_id"]))
            try:
                like = models.post_Likes.objects.get(post_id=post, username=user)
                like.delete()
            except:
                like = models.post_Likes.objects.filter(post_id=post, username=user)
                for i in like:
                    i.delete()
            post.like_count -= 1
            post.algoValue = (
                datetime_weight * int(post.posted_date.timestamp())
                + like_weight * (post.like_count)
                + comment_weight * (post.comment_count)
            )
            post.save()
        except:
            error = True
        return Response({"error": error})


class EVENT_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            start = int(data["num_list"])
            if data["domain"] == "All":
                event_list = models.Events.objects.filter(all_universities=True)
            else:
                if user.domain == data["domain"]:
                    event_list = models.Events.objects.filter(domain=data["domain"])
                else:
                    event_list = models.Events.objects.filter(
                        domain=data["domain"], all_universities=True
                    )
            event_list = event_list[start : 10 + start]
            for i in event_list:
                try:
                    like = models.Event_likes.objects.filter(event_id=i, username=user)
                    if len(like) >= 1:
                        i.is_like = True
                    elif len(like) > 1:
                        for i in range(len(like) - 1):
                            i.delete()
                except:
                    i.is_like = False
            serializer = serializers.EventsSerializer(event_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            event = models.Events()
            event.username = user
            event.title = data["title"]
            event.domain = user.domain
            event.description = data["description"]
            event.event_img = ContentFile(
                base64.b64decode(data["file"]), data["file_name"]
            )
            event.img_ratio = float(int(data["image_ratio"]))
            event.event_date = data["event_date"]
            event.all_universities = data["is_all_university"]

            if data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                club.event_count += 1
                club.save()
                event.club = club
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                sport.event_count += 1
                sport.save()
                event.sport = sport
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                fest.event_count += 1
                fest.save()
                event.fest = fest
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                sac.event_count += 1
                sac.save()
                event.sac = sac
            event.category = data["category"]
            event.domain = user.domain

            event.save()

        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            event = models.Events.objects.get(id=int(data["event_id"]))
            event.delete()
        except:
            error = True
        return Response({"error": error})


class EVENT_LIKE_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            event = models.Events.objects.get(id=int(data["event_id"]))
            likes_list = event.event_like_id.all()
            serializer = serializers.EventsLikeSerializer(likes_list, many=True)
            return Response(serializer.data)

        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            data = request.data
            user = request.user
            event = models.Events.objects.get(id=int(data["event_id"]))
            event_like = models.Event_likes()
            event_like.username = user
            event_like.domain = user.domain
            event_like.event_id = event
            event_like.save()
            event.like_count += 1
            event.save()
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            event = models.Events.objects.get(id=int(data["event_id"]))
            try:
                like = models.Event_likes.objects.get(username=user, event_id=event)
                like.delete()
            except:
                like = models.Event_likes.objects.filter(username=user, event_id=event)
                for i in like:
                    i.delete()
            event.like_count -= 1
            event.save()
        except:
            error = True
        return Response({"error": error})

    ## EVENT_UPDATE USING EVENT LIKE URL

    def put(self, request):
        error = False
        try:
            data = request.query_params
            event = models.Events.objects.get(id=int(data["event_id"]))
            event.event_updates = data["event_update"] + "`" + event.event_updates
            event.save()

            try:
                data = Message(
                    notification=Notification(
                        title=event.title + " update ", body=data["event_update"]
                    )
                    # topic="Optional topic parameter: Whatever you want",
                )
                # notifications().notifications(data,3)
            except:
                a = ""
        except:
            error = True
        return Response({"error": error})


class ALERT_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            start = int(data["num_list"])
            if data["domain"] == "All":
                data1 = models.Alerts.objects.filter(
                    all_universities=True
                ) | models.Alerts.objects.filter(
                    all_universities=False, domain=user.domain
                )
            else:
                if user.domain == data["domain"]:
                    data1 = models.Alerts.objects.filter(domain=data["domain"])
                else:
                    data1 = models.Alerts.objects.filter(
                        domain=data["domain"], all_universities=True
                    )
            data1 = data1[start : 10 + start]
            data = []
            for i in data1:
                if i.username == user:
                    data.append(i)
                    continue
                if (
                    user.branch in i.allow_branchs
                    and i.allow_years[user.year - 1] == "1"
                    and user.course in i.allow_courses
                ):
                    data.append(i)
            serializer = serializers.AlertsSerializer(data, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            data = request.data
            user = request.user
            alert = models.Alerts()
            alert.username = user
            if data["file_type"] != 0:
                alert.img = ContentFile(
                    base64.b64decode(data["base64file"]), data["fileName"]
                )
                alert.img_ratio = float(data["file_type"])
            else:
                alert.img_ratio = 0.0
            alert.domain = user.domain
            alert.title = data["title"]
            alert.description = data["description"]
            alert.allow_branchs = data["allow_branchs"]
            alert.allow_years = data["allow_years"]
            alert.allow_courses = data["allow_courses"]
            alert.all_universities = data["is_all_university"]

            if data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                club.thread_count += 1
                club.save()
                alert.club = club
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                sport.thread_count += 1
                sport.save()
                alert.sport = sport
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                fest.thread_count += 1
                fest.save()
                alert.fest = fest
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                sac.thread_count += 1
                sac.save()
                alert.sac = sac
            else:
                user.thread_count += 1
                user.save()
            alert.category = data["category"]
            alert.domain = user.domain

            alert.save()

        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            alert = models.Alerts.objects.get(id=int(data["alert_id"]))
            alert.delete()
            user.thread_count -= 1
            user.save()
        except:
            error = True
        return Response({"error": error})


class ALERT_CMNT_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    def get(self, request):
        error = False
        try:
            data = request.query_params
            user = request.user
            # LST_list = models.Lost_Found.objects.get(title = "Lost my soulmate")
            ALERT_list = models.Alerts.objects.get(id=int(data["alert_id"]))
            comments = ALERT_list.alert_comment.all()
            serializer = serializers.Alert_CommentsSerializer(comments, many=True)
            response = serializer.data
            return Response(response)
        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            ALERT_list = models.Alerts.objects.get(id=int(data["alert_id"]))
            ALERT_list.comment_count += 1
            new_comment = models.ALERT_Comments()
            new_comment.alert_cmnt_id = ALERT_list
            new_comment.Comment = data["comment"]
            new_comment.domain = user.domain
            new_comment.username = user
            if data["file_type"] != 0:
                new_comment.img = ContentFile(
                    base64.b64decode(data["base64file"]), data["fileName"]
                )
                new_comment.img_ratio = float(data["file_type"])
            else:
                new_comment.img_ratio = 0.0
            new_comment.allow_branchs = data["allow_branchs"]
            new_comment.allow_years = data["allow_years"]
            new_comment.domain = user.domain
            new_comment.save()
            ALERT_list.save()

            return Response({"error": error, "id": new_comment.id})
        except:
            error = True
        return Response({"error": error})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            comment_list = models.ALERT_Comments.objects.get(
                id=int(data["alert_cmnt_id"])
            )  # id is primary key of comments
            comment_list.delete()
            alert = models.Alerts.objects.get(id=int(data["alert_id"]))
            alert.comment_count -= 1
            alert.save()
        except:
            error = True
        return Response({"error": error})


class PEOFILE_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    # UPDATE PROFILE WITH OR WITH IMAGE
    def post(self, request):
        error = False
        try:
            data = request.data
            user = request.user
            user.username = data["username"]
            user.phn_num = data["phone_number"]
            if data["file_type"] == "2":
                user.profile_pic = ContentFile(
                    base64.b64decode(data["file"]), data["file_name"]
                )
                user.file_type = "1"
            user.course = data["course"]
            user.branch = data["branch"]
            user.year = data["year"]
            user.bio = data["bio"]
            user.batch = data["batch"]
            user.save()
        except:
            error = True
        return Response({"error": error})

    # PROFILE CATEGORY DATA BASED ON IDS
    def delete(self, request):
        error = False
        try:
            data = request.data
            user = request.user

            # GETTING HEADS OF CATEGORY EX:- CLUBS,SPORTS ETC..
            heads_ids = data["head_ids"].split("#")
            heads = []
            head_serializer_data = []
            for i in heads_ids:
                try:
                    if data["category"] == "club":
                        club = api2_models.AllClubs.objects.get(id=int(i))
                        heads.append(club)
                    elif data["category"] == "sport":
                        sport = api2_models.AllSports.objects.get(id=int(i))
                        heads.append(sport)
                    elif data["category"] == "fest":
                        fest = api2_models.AllFests.objects.get(id=int(i))
                        heads.append(fest)
                    elif data["category"] == "sac":
                        sac = api2_models.SAC_MEMS.objects.get(id=int(i))
                        heads.append(sac)
                except:
                    a = 0
            else:
                try:
                    if data["category"] == "club":
                        head_serializer = api2_serializers.AllClubsSerializer(
                            heads, many=True
                        )
                        head_serializer_data = head_serializer.data
                    elif data["category"] == "sport":
                        head_serializer = api2_serializers.AllSportsSerializer(
                            heads, many=True
                        )
                        head_serializer_data = head_serializer.data
                    elif data["category"] == "fest":
                        head_serializer = api2_serializers.AllFestsSerializer(
                            heads, many=True
                        )
                        head_serializer_data = head_serializer.data
                    elif data["category"] == "sac":
                        head_serializer = api2_serializers.SAC_MEMSSerializer(
                            heads, many=True
                        )
                        head_serializer_data = head_serializer.data
                except:
                    a = 0

            # GETTING MEMBERS OF CATEGORY EX:- CLUBS,SPORTS ETC..
            mems_ids = data["member_ids"].split("#")
            mems = []
            mems_serializer_data = []
            for i in mems_ids:
                try:
                    if data["category"] == "club":
                        club = api2_models.AllClubs.objects.get(id=int(i))
                        mems.append(club)
                    elif data["category"] == "sport":
                        sport = api2_models.AllSports.objects.get(id=int(i))
                        mems.append(sport)
                    elif data["category"] == "fest":
                        fest = api2_models.AllFests.objects.get(id=int(i))
                        mems.append(fest)
                    elif data["category"] == "sac":
                        sac = api2_models.SAC_MEMS.objects.get(id=int(i))
                        mems.append(sac)
                except:
                    a = 0
            else:
                try:
                    if data["category"] == "club":
                        mems_serializer = api2_serializers.AllClubsSerializer(
                            mems, many=True
                        )
                        mems_serializer_data = mems_serializer.data
                    elif data["category"] == "sport":
                        mems_serializer = api2_serializers.AllSportsSerializer(
                            mems, many=True
                        )
                        mems_serializer_data = mems_serializer.data
                    elif data["category"] == "fest":
                        mems_serializer = api2_serializers.AllFestsSerializer(
                            mems, many=True
                        )
                        mems_serializer_data = mems_serializer.data
                    elif data["category"] == "sac":
                        mems_serializer = api2_serializers.SAC_MEMSSerializer(
                            mems, many=True
                        )
                        mems_serializer_data = mems_serializer.data
                except:
                    a = 0

            ## returning all the data

            return Response([head_serializer_data, mems_serializer_data, data])

        except:
            error = True
        return Response({"error": error})

    # Profile User Posts Data
    def get(self, request):
        error = False
        try:
            app_user = request.user
            data = request.query_params
            post_list = []
            if data["category"] == "student":
                user = User.objects.get(email=data["email"])
                post_list = user.post_table_username.all()
            elif data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                post_list = club.post_from_club.all()
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                post_list = sport.post_from_sport.all()
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                post_list = fest.post_from_fest.all()
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                post_list = sac.post_from_sac.all()

            for i in post_list:
                try:
                    like = models.post_Likes.objects.get(post_id=i, username=app_user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.PostTableSerializer(post_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    # Profile User Threads Data
    def put(self, request):
        error = False
        try:
            app_user = request.user
            data = request.data
            thread_list = []
            if data["category"] == "student":
                user = User.objects.get(email=data["email"])
                thread_list = user.alerts_username.all()
            elif data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                thread_list = club.thread_from_club.all()
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                thread_list = sport.thread_from_sport.all()
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                thread_list = fest.thread_from_fest.all()
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                thread_list = sac.thread_from_sac.all()

            serializer = serializers.AlertsSerializer(thread_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    # Profile User Activities Data
    def patch(self, request):
        error = False
        try:
            app_user = request.user
            data = request.data
            event_list = []
            if data["category"] == "student":
                user = User.objects.get(email=data["email"])
                event_list = user.post_table_username.all()
            elif data["category"] == "club":
                club = api2_models.AllClubs.objects.get(id=int(data["category_id"]))
                event_list = club.event_from_club.all()
            elif data["category"] == "sport":
                sport = api2_models.AllSports.objects.get(id=int(data["category_id"]))
                event_list = sport.event_from_sport.all()
            elif data["category"] == "fest":
                fest = api2_models.AllFests.objects.get(id=int(data["category_id"]))
                event_list = fest.event_from_fest.all()
            elif data["category"] == "sac":
                sac = api2_models.SAC_MEMS.objects.get(id=int(data["category_id"]))
                event_list = sac.event_from_sac.all()

            for i in event_list:
                try:
                    like = models.Event_likes.objects.get(event_id=i, username=app_user)
                    i.is_like = True
                except:
                    i.is_like = False
            serializer = serializers.EventsSerializer(event_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})


class CALENDER_EVENTS_list(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    # TO GET ALL EVENTS_DATES
    def patch(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            dates = {}
            activities = models.Events.objects.filter(domain=data["domain"])
            for i in activities:
                a = i.event_date
                dates[str(a) + "&&" + i.title] = ""
            cal_events = models.CalenderEvents.objects.filter(
                username=user, domain=data["domain"]
            ) | models.CalenderEvents.objects.filter(
                cal_event_type="all", domain=data["domain"]
            )
            for i in cal_events:
                if i.cal_event_type == "self":
                    dates[str(i.event_date) + "&&" + i.title] = ""
                elif (
                    (i.year[user.year - 1] == "1")
                    and (user.branch in i.branch)
                    and (user.course in i.course)
                ):
                    dates[str(i.event_date) + "&&" + i.title] = ""
            final_dates = list(dates.keys())
            final_dates.sort()
            return Response(final_dates)
        except:
            error = True
        return Response({"error": error})

    # TO GET INDUVIDUAL DATE EVENTS
    def get(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params

            if user.domain == data["domain"]:
                calender_date_events_all = models.CalenderEvents.objects.filter(
                    cal_event_type="all", domain=data["domain"]
                )
                calender_date_events_self = models.CalenderEvents.objects.filter(
                    username=user, cal_event_type="self", domain=data["domain"]
                )
            else:
                calender_date_events_all = models.CalenderEvents.objects.filter(
                    cal_event_type="all", domain=data["domain"], all_universities=True
                )
                calender_date_events_self = []

            calender_date_events = []
            for i in calender_date_events_self:
                a = str(i.event_date)
                if a[:10] == data["calender_date"]:
                    calender_date_events.append(i)
            for i in calender_date_events_all:
                a = str(i.event_date)
                if (
                    a[0:10] == data["calender_date"]
                    and i.year[user.year - 1] == "1"
                    and user.branch in i.branch
                    and user.course in i.course
                ):
                    calender_date_events.append(i)
            if data["domain"] == user.domain:
                activities_all = models.Events.objects.filter(domain=data["domain"])
            else:
                activities_all = models.Events.objects.filter(
                    domain=data["domain"], all_universities=True
                )

            date_activities = []
            for i in activities_all:
                a = str(i.event_date)[0:10]
                if a == data["calender_date"]:
                    date_activities.append(i)
                    try:
                        like = models.Event_likes.objects.filter(
                            event_id=i, username=user
                        )
                        if len(like) >= 1:
                            i.is_like = True
                        elif len(like) > 1:
                            for i in range(len(like) - 1):
                                i.delete()
                    except:
                        i.is_like = False
            event_serializer = serializers.EventsSerializer(date_activities, many=True)
            calender_date_serializer = serializers.CALENDER_EVENTSerializer(
                calender_date_events, many=True
            )

            return Response([event_serializer.data, calender_date_serializer.data])

        except:
            error = True
        return Response({"error": error})

    def post(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            calander_event = models.CalenderEvents()
            calander_event.username = user
            calander_event.cal_event_type = data["cal_event_type"]
            calander_event.title = data["title"]
            calander_event.domain = user.domain
            calander_event.description = data["description"]
            if data["file_type"] != "0":
                calander_event.calender_date_file = ContentFile(
                    base64.b64decode(data["file"]), data["file_name"]
                )
            calander_event.file_type = data["file_type"]
            calander_event.branch = data["branch"]
            calander_event.year = data["year"]
            calander_event.course = data["course"]
            calander_event.event_date = data["event_date"]
            calander_event.domain = user.domain
            try:
                calander_event.all_universities = data["all_universities"]
            except:
                calander_event.all_universities = True
            calander_event.save()
            return Response({"error": error, "id": calander_event.id})
        except:
            error = True
        return Response({"error": error, "id": 0})

    def delete(self, request):
        error = False
        try:
            data = request.query_params
            message = models.CalenderEvents.objects.get(
                id=int(data["calender_event_id"])
            )
            message.delete()
        except:
            error = True
        return Response({"error": error})

    def put(self, request):
        error = False
        try:
            user = request.user
            data = request.data
            calander_event = models.CalenderEvents.objects.get(id=int(data["id"]))
            calander_event.username = user
            calander_event.cal_event_type = data["cal_event_type"]
            calander_event.title = data["title"]
            calander_event.description = data["description"]
            if data["file_type"] != "0":
                calander_event.calender_date_file = ContentFile(
                    base64.b64decode(data["file"]), data["file_name"]
                )
            calander_event.file_type = data["file_type"]
            calander_event.branch = data["branch"]
            calander_event.year = data["year"]
            calander_event.course = data["course"]
            calander_event.event_date = data["event_date"]
            calander_event.save()
            return Response(
                {
                    "error": error,
                    "id": calander_event.id,
                    "date": calander_event.event_date,
                }
            )
        except:
            error = True
        return Response({"error": error, "id": 0})


class USER_Messanger(APIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        TokenAuthentication,
    ]

    ## NAME MATCH USERS

    def get(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            start = int(data["num_list"])
            if data["domain"] == "All":
                users_list = User.objects.filter(
                    email__icontains=data["username_match"]
                ) | User.objects.filter(username__icontains=data["username_match"])
            else:
                users_list = User.objects.filter(
                    email__icontains=data["username_match"], domain=data["domain"]
                ) | User.objects.filter(
                    username__icontains=data["username_match"], domain=data["domain"]
                )
            users_list = users_list[start : 100 + start]
            serializer = serializers.SmallUserSerializer(users_list, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})

    ## USER TO USER MESSAGES NOTIFICATIONS

    def delete(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params

            user_ids = data["chattinguser_email"].split("#")

            fcm_tokens = []
            temp_users = []
            for i in user_ids:
                try:
                    temp_user = User.objects.get(user_uuid=i)
                except:
                    a = 0
                temp_users.append(temp_user)
                fcm_tokens.append(temp_user.token)

            api2_views.bulk_notifications(
                fcm_tokens, user.email, ": Messaged : " + data["message"]
            )

            return Response({"error": error})
        except:
            error = True
        return Response({"error": error})

    ## USER TO USER MESSAGES NOTIFICATIONS DATING USER

    def patch(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params

            temp_user = User.objects.get(user_uuid=data["chattinguser_email"])
            fcm_tokens = [temp_user.token]

            datingUser = api2_models.DatingUser.objects.get(username=temp_user)

            api2_views.bulk_notifications(
                fcm_tokens, datingUser.dummyName, ": Messaged : " + data["message"]
            )

            return Response({"error": error})
        except:
            error = True
        return Response({"error": error})

    ## UUID TO USERS LIST.

    def put(self, request):
        error = False
        try:
            user = request.user
            data = request.query_params
            all_uuids = data["user_uuids"].split("#")
            all_msg_users = []
            for i in all_uuids:
                try:
                    user = User.objects.get(user_uuid=i)
                    all_msg_users.append(user)
                except:
                    a = 0

            serializer = serializers.SmallUserSerializer(all_msg_users, many=True)
            return Response(serializer.data)
        except:
            error = True
        return Response({"error": error})
