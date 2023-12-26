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
from django.db.models import Q
from django.utils.timezone import localtime



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


class testing_api3(APIView):
    def get(self, request):
        error = False
        password = ""
        try:
            users = User.objects.get(username = "gautham")
            # for i in users:
            #     if i.platform == "android":
            #         i.update_mark = "instabook4"
            #         i.save()

        except:
            error = True
        return Response({"error": error, "password": password})













