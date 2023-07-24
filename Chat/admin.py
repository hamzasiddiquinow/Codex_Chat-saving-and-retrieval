from django.contrib import admin

from Chat.models import chats
from registration.models import u_registration

# Register your models here.
admin.site.register(chats)
admin.site.register(u_registration)
