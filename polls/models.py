from django.db import models

class LoginID(models.Model):
    username = models.CharField(max_length=200)
    password = models.IntegerField()
    def __str__(self):
        return self.username
