from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth import get_user_model
#from .models import customUser
User = get_user_model()
from api2 import models as api2_models


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SmallUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','domain','email','user_mark','star_mark','profile_pic','phn_num','file_type','is_student_admin']

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
        if response['post_category'] == "club":
            response['club_post'] = AllClubs1Serializer(instance.club_post).data
        elif response['post_category'] == "sport":
            response['sport_post'] = AllSports1Serializer(instance.sport_post).data
        elif response['post_category'] == "fest":
            response['fest_post'] = AllFests1Serializer(instance.fest_post).data
        elif response['post_category'] == "sac":
            response['sac_post'] = SAC_MEMS1Serializer(instance.sac_post).data
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
        if response['event_category'] == "club":
            response['club_event'] = AllClubs1Serializer(instance.club_event).data
        elif response['event_category'] == "sport":
            response['sport_event'] = AllSports1Serializer(instance.sport_event).data
        elif response['event_category'] == "fest":
            response['fest_event'] = AllFests1Serializer(instance.fest_event).data
        elif response['event_category'] == "sac":
            response['sac_event'] = SAC_MEMS1Serializer(instance.sac_event).data


        return response

class AlertsSerializer(ModelSerializer):
    class Meta:
        model = models.Alerts
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        if response['thread_category'] == "club":
            response['club_thread'] = AllClubs1Serializer(instance.club_thread).data
        elif response['thread_category'] == "sport":
            response['sport_thread'] = AllSports1Serializer(instance.sport_thread).data
        elif response['thread_category'] == "fest":
            response['fest_thread'] = AllFests1Serializer(instance.fest_thread).data
        elif response['thread_category'] == "sac":
            response['sac_thread'] = SAC_MEMS1Serializer(instance.sac_thread).data


        return response

class Alert_CommentsSerializer(ModelSerializer):
    class Meta:
        model = models.ALERT_Comments
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response




class Post_LikeSerializer(ModelSerializer):
    class Meta:
        model = models.post_Likes
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = UserSerializer(instance.username).data
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




### SERIALIZERS FOR POST OF CLUB/FEST/SPORT/SAC


class SAC_MEMS1Serializer(ModelSerializer):
    class Meta:
        model = api2_models.SAC_MEMS
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = None
        return response

class AllClubs1Serializer(ModelSerializer):
    class Meta:
        model = api2_models.AllClubs
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = None
        return response


class AllSports1Serializer(ModelSerializer):
    class Meta:
        model = api2_models.AllSports
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = None
        return response



class AllFests1Serializer(ModelSerializer):
    class Meta:
        model = api2_models.AllFests
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = None
        return response



















