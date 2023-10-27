from django.db import models

# Create your models here.
# 웹사이트 본문에 해당하는 모델 정의하기
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')