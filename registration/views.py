from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from.action import save
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




# from rest_framework_simplejwt.authentication import  JWTAuthentication


# Create your views here.
class in_info(APIView):
    def post(self, request):
        save(request.data)
        return HttpResponse("credential saved")


