from django.db import models

class Users(models.Model):
     userKey = models.IntegerField(primary_key=True, serialize=True)
     Username = models.CharField(max_length=200)
     Password = models.CharField(max_length=200)
     CreatedAt = models.DateTimeField()
     ModifiedAt = models.DateTimeField()