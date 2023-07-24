import subprocess

from rest_framework import status
from rest_framework.response import Response
from threading import Thread
from .models import chats
from .serializer import chatsSerializer
from django.http import request
import requests


def save(data):
    data = data.copy()
    serial = chatsSerializer(data=data)
    serial.is_valid(raise_exception=True)
    serial.save()

    # if data.get('chat_ID'):
    #     data.update({'chat_ID': data.get('chat_ID')})
    #     serial = chatsSerializer('chat_ID')
    #     serial.is_valid(raise_exception=True)
    #     serial.save()
    #
    # if data.get('sender'):
    #     data.update({'sender': data.get('sender')})
    #     # try:
    #     #     if 'sender' not in User.first_name + '@ahsan.org':
    #     #         return Response({" User not matched"}, status=status.HTTP_400_BAD_REQUEST)
    #     # except Exception as e:
    #     #     print(e)
    #     serial = chatsSerializer('sender')
    #     serial.is_valid(raise_exception=True)
    #     serial.save()
    #
    # if data.get('receiver'):
    #     data.update({'receiver': data.get('receiver')})
    #     # try:
    #     #     if 'reciever' not in User.first_name + '@ahsan.org':
    #     #         return Response({" User not matched"}, status=status.HTTP_400_BAD_REQUEST)
    #     # except Exception as e:
    #     #     print(e)
    #     serial = chatsSerializer('receiver')
    #     serial.is_valid(raise_exception=True)
    #     serial.save()
    #
    #     if len(data.get('message')) <= 1000:
    #         data.update({'message': data.get('message')})
    #         try:
    #             if len(data.get('message')) >= 1000:
    #                 return Response({" Too large message"}, status=status.HTTP_400_BAD_REQUEST)
    #         except Exception as e:
    #             print(e)
    #
    #         serial = chatsSerializer(data=data)
    #         serial.is_valid(raise_exception=True)
    #         serial.save()
    #         return Response({" Messge saved"})


def check_data(request):
    # Create an instance of MyModel
    instance = chats.chat_ID.all()
    for i in instance:
        print(i)

def retrieve(request):
    send = request.data['sender']
    recv = request.data['receiver']
    mess = list()
    obj = chats.objects.filter(sender=send, receiver=recv).order_by('date').values()[::1]
    serial = chatsSerializer(obj, many=True)
    data1 = serial.data
    obj2 = chats.objects.filter(sender=recv, receiver=send).order_by('date').values()[::1]
    serial = chatsSerializer(obj2, many=True)
    data2 = serial.data
    return Response(data1 + data2)


def createroom(request):
    ejabberd_api_url = "http://localhost:5280/api/create_room"  # Replace with your Ejabberd API URL

    data = {
        "name": request.data.get("name"),  # The name of the MUC room
        "service": request.data.get("service"),                                   #"conference.example.com",  # XMPP service domain
        "host": request.data.get("host")   #"example.com",  # XMPP server domain
        # "options": {
        #     "members_only": True,
        #     "persistent": True,
        #     "public": False,
        # }
    }

    response = requests.post(ejabberd_api_url, json=data)
    print({response.status_code})
    if response.status_code == 201:
        return Response({"message": "MUC room created successfully!"})
    else:
        return Response({"error": response.status_code}, status=response.status_code)

