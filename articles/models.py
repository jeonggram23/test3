from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set : 장고가 자동으로 추가해주는 칼럼
    
    # 유저 모델을 참조하는 경우
    
    #case 1.
    # user = model.models.ForeignKey(User, on_delete=models.CASCADE)
    
    #case 2.
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #case 3.
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # user_id=
    
class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    # article_id = 장고가 자동으로 추가해주는 칼럼
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id 

