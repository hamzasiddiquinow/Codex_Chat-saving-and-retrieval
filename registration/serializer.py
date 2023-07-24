from rest_framework import serializers
from .models import u_registration
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = u_registration
        fields = ('u_ID','f_name', 'l_name', 'email', 'dob', 'u_name', 'password')


