# Generated by Django 4.2.3 on 2023-07-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="u_registration",
            fields=[
                ("u_ID", models.AutoField(primary_key=True, serialize=False)),
                ("f_name", models.CharField(max_length=20)),
                ("l_name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=35)),
                ("dob", models.DateTimeField()),
                ("u_name", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=40)),
            ],
        ),
    ]
