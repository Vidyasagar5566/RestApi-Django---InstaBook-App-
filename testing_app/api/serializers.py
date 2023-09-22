from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth import get_user_model
#from .models import customUser
User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SmallUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','roll_num','profile_pic','phn_num','file_type','is_admin']

class Lost_FoundSerializer(ModelSerializer):
    class Meta:
        model = models.Lost_Found
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response


class LST_CommentsSerializer(ModelSerializer):
    class Meta:
        model = models.LST_Comments
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class PostTableSerializer(ModelSerializer):
    class Meta:
        model = models.PostTable
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class post_CommentsSerializer(ModelSerializer):
    class Meta:
        model = models.post_Comments
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class EventsSerializer(ModelSerializer):
    class Meta:
        model = models.Events
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = UserSerializer(instance.username).data
        return response

class AlertsSerializer(ModelSerializer):
    class Meta:
        model = models.Alerts
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class Alert_CommentsSerializer(ModelSerializer):
    class Meta:
        model = models.ALERT_Comments
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response


class Clubs_SportsSerializer(ModelSerializer):
    class Meta:
        model = models.Clubs_Sports
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = UserSerializer(instance.username).data
        response['head'] = UserSerializer(instance.head).data
        return response


#class Clubs_Sports_filesSerializer(ModelSerializer):
#    class Meta:
#        model = models.Clubs_Sports_files
#        fields = "__all__"

class Mess_tableSerializer(ModelSerializer):
    class Meta:
        model = models.Mess_table
        fields = "__all__"

class Academic_tableSerializer(ModelSerializer):
    class Meta:
        model = models.Academic_table
        fields = "__all__"

class Time_tableSerializer(ModelSerializer):
    class Meta:
        model = models.Time_table
        fields = "__all__"

class Post_LikeSerializer(ModelSerializer):
    class Meta:
        model = models.post_Likes
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = UserSerializer(instance.username).data
        return response

class NotificationsSerializer(ModelSerializer):
    class Meta:
        model = models.Notifications
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class MessangerSerializer(ModelSerializer):
    class Meta:
        model = models.Messanger
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['message_sender'] = SmallUserSerializer(instance.message_sender).data
        response['message_receiver'] = SmallUserSerializer(instance.message_receiver).data
        return response

class CALENDER_EVENTSerializer(ModelSerializer):
    class Meta:
        model = models.CalenderEvents
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response


class CalenderSubSerializer(ModelSerializer):
    class Meta:
        model = models.CalenderSub
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class CalenderSubYearsSerializer(ModelSerializer):
    class Meta:
        model = models.CalenderSubYears
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class CalenderSubFilesSerializer(ModelSerializer):
    class Meta:
        model = models.CalenderSubFiles
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class RatingsSerializer(ModelSerializer):
    class Meta:
        model = models.Ratings
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response
