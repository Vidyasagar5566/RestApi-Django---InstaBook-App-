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
        if response['category'] == "club":
            response['club'] = AllClubs1Serializer(instance.club).data
        elif response['category'] == "sport":
            response['sport'] = AllSports1Serializer(instance.sport).data
        elif response['category'] == "fest":
            response['fest'] = AllFests1Serializer(instance.fest).data
        elif response['category'] == "sac":
            response['sac'] = SAC_MEMS1Serializer(instance.sac).data
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
        response['username'] = SmallUserSerializer(instance.username).data
        if response['category'] == "club":
            response['club'] = AllClubs1Serializer(instance.club).data
        elif response['category'] == "sport":
            response['sport'] = AllSports1Serializer(instance.sport).data
        elif response['category'] == "fest":
            response['fest'] = AllFests1Serializer(instance.fest).data
        elif response['category'] == "sac":
            response['sac'] = SAC_MEMS1Serializer(instance.sac).data

        return response

class AlertsSerializer(ModelSerializer):
    class Meta:
        model = models.Alerts
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        if response['category'] == "club":
            response['club'] = AllClubs1Serializer(instance.club).data
        elif response['category'] == "sport":
            response['sport'] = AllSports1Serializer(instance.sport).data
        elif response['category'] == "fest":
            response['fest'] = AllFests1Serializer(instance.fest).data
        elif response['category'] == "sac":
            response['sac'] = SAC_MEMS1Serializer(instance.sac).data


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

class MessagesSerializer(ModelSerializer):
    class Meta:
        model = models.Messanger
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['message_sender'] = SmallUserSerializer(instance.message_sender).data['email']
        response['message_receiver'] = SmallUserSerializer(instance.message_receiver).data['email']
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



















