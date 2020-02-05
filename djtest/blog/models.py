from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Article(models.Model):
    title = models.CharField("标题",max_length=255)
    author = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    xiugai_date = models.DateField(auto_now=True)
    content = models.TextField()
    is_show = models.BooleanField()
    
    
    class Meta:
        db_table = "article"
    
    def __str__(self):
        return self.title

class Myuser(AbstractUser):


    jifen = models.IntegerField('积分',default = 0)
    class Meta:
        db_table = 'Myuser'
    def __str__(self):
        return self.username
    
class quanxian(models.Model):
    shuoming=models.CharField(max_length=100)
    def __unicode__(self):
        return self.shuoming
    class Meta:
        permissions = (
            ('part',u'部分权限'),
            ('all',u'全部'),
        )