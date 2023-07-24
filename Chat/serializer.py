from rest_framework import serializers

from .models import chats
class chatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = chats
        fields = ('chat_ID', 'sender', 'receiver', 'message', 'date')