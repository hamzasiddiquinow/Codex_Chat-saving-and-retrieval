from .views import in_info


from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView, )

urlpatterns = [
    path('register/', in_info.as_view())
]
