from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import CourseInfo
# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
    phone = models.CharField(max_length=11,verbose_name="手机")
    course = models.CharField(max_length=20,verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "咨询信息"
        verbose_name_plural = verbose_name

class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile,verbose_name="收藏用户")
    love_id = models.IntegerField(verbose_name="收藏ID")
    love_type = models.IntegerField(choices=((1,'机构'),(2,'课程'),(3,'老师')),verbose_name="收藏类别")
    love_status = models.BooleanField(default=False,verbose_name="收藏状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="收藏时间")

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = "收藏信息"
        verbose_name_plural = verbose_name

class UserCourse(models.Model):
    study_man = models.ForeignKey(UserProfile, verbose_name="学习用户")
    study_course=models.ForeignKey(CourseInfo,verbose_name="学习课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="学习时间")

    def __str__(self):
        return self.study_man.username

    class Meta:
        unique_together = ('study_man','study_course')
        verbose_name = "用户学习课程信息"
        verbose_name_plural = verbose_name

class UserComment(models.Model):
#     TODO 继续完成后续的模型创建的工作。
