
from django.contrib import admin
from django.urls import path,include
from .views import Savechat, show_chat,create_room
    # , check

urlpatterns = [
    path("admin/", admin.site.urls),

    path('save/', Savechat.as_view()),
    # path('show/',check.as_view())
    path('show/', show_chat.as_view()),
    path('create_room/',create_room.as_view())
]