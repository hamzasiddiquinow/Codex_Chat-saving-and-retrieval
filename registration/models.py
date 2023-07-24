import datetime

from django.db import models


class u_registration(models.Model):
    u_ID = models.AutoField(primary_key=True, null=False)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.CharField(max_length=35)
    dob = models.DateTimeField(datetime.date)
    u_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    objects = models.Manager()

    def __str__(self):
        return self.f_name
