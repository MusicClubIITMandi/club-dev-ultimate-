from django.db import models

class Comments(models.Model):
    commentId = models.AutoField(primary_key=True)
    Time = models.CharField(max_length=100)
    Topic = models.CharField(max_length = 30)
    DisplayName = models.CharField(max_length = 30)
    Author = models.CharField(max_length = 30)
    Comment = models.TextField()