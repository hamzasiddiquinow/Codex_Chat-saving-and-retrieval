# from requests import Response
import json
from rest_framework.response import Response

from rest_framework.views import APIView
from .action import save, retrieve, createroom
from django.http import HttpResponse, request
from.models import chats
from .serializer import chatsSerializer


class Savechat(APIView):
    def post(self, request):
        save(request.data)
        # sev = 'data saved'
        return HttpResponse("Chat Saved....!")

# class check(APIView):
#     def get(self):
#         check_data(request)
#
#             # Return an appropriate response
#         return HttpResponse('Data check complete.')

class show_chat(APIView):
    def get(self, request):
        return retrieve(request)

class create_room(APIView):
    def post (self, request):

        return createroom(request)