from rest_framework.serializers import ModelSerializer
from . import models
from django.contrib.auth import get_user_model
#from .models import customUser
User = get_user_model()
from api import models as api_models




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SmallUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','domain','email','user_mark','star_mark','profile_pic','phn_num','file_type','is_student_admin']




class AllClubsSerializer(ModelSerializer):
    class Meta:
        model = models.AllClubs
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = SmallUserSerializer(instance.head).data
        return response


class AllSportsSerializer(ModelSerializer):
    class Meta:
        model = models.AllSports
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = SmallUserSerializer(instance.head).data
        return response


class AllFestsSerializer(ModelSerializer):
    class Meta:
        model = models.AllFests
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['head'] = SmallUserSerializer(instance.head).data
        return response





class UniBranchesSerializer(ModelSerializer):
    class Meta:
        model = api_models.UniBranches
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response


class CalenderSubSerializer(ModelSerializer):
    class Meta:
        model = api_models.BranchSub
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class CalenderSubYearsSerializer(ModelSerializer):
    class Meta:
        model = api_models.BranchSubYears
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class CalenderSubFilesSerializer(ModelSerializer):
    class Meta:
        model = api_models.BranchSubFiles
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response

class RatingsSerializer(ModelSerializer):
    class Meta:
        model = api_models.Ratings
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['username'] = SmallUserSerializer(instance.username).data
        return response



class Mess_tableSerializer(ModelSerializer):
    class Meta:
        model = api_models.Mess_table
        fields = "__all__"

class Academic_tableSerializer(ModelSerializer):
    class Meta:
        model = api_models.Academic_table
        fields = "__all__"

class Time_tableSerializer(ModelSerializer):
    class Meta:
        model = api_models.Time_table
        fields = "__all__"





