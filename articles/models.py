from django.db import models
<<<<<<< HEAD
from accounts.models import User
from django.conf import settings
=======
>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
from django.contrib.auth import get_user_model
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
<<<<<<< HEAD
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
=======

class Comment(models.Model):
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

>>>>>>> d7ec2c25f06fb9af9bc4e744f0a9afd969b6e0db
