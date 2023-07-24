from django.db import models

class chats(models.Model):
    chat_ID = models.AutoField(primary_key=True, null=False)
    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Add additional text to the existing value of my_field
        self.sender = self.sender + "@ahsan.org"
        self.receiver = self.receiver + "@ahsan.org"

        # Call the parent class's save() method to save the instance
        super().save(*args, **kwargs)

    objects = models.Manager()

    def __str__(self):
        return self.message
