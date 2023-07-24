from.serializer import registerSerializer
from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache



def save(data):
    data.copy()
    serial = registerSerializer(data=data)
    serial.is_valid(raise_exception=True)
    serial.save()


