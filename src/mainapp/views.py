from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.renderers import JSONRenderer
# Create your views here.


class DetailProfile(APIView):
    def get(self,request,format=None):
        prof = Profile.objects.all()
        # loc = Location.objects.all()
        res = ProfileSerializer(prof,many=True)

        return Response(res.data)


