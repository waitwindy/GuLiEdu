from datetime import  datetime

from django.db import models

# Create your models here.
class CityInfo (models.Model):
    name = models.CharField(max_length=20,verbose_name="城市名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name

class OrgInfo(models.Model):
    image = models.ImageField(upload_to='org/',max_length=200,verbose_name="机构封面")
    name = models.CharField(max_length=20,verbose_name="机构名称")
    course_num = models.IntegerField(default=0,verbose_name="课程数")
    study_num = models.IntegerField(default=0,verbose_name="学习人数")
    address = models.CharField(max_length=200,verbose_name="机构地址")
    desc = models.CharField(max_length=200,verbose_name="机构简介")
    detail = models.TextField(verbose_name="机构详情")
    love_num = models.IntegerField(default=0,verbose_name="收藏数")
    click_num = models.IntegerField(default=0,verbose_name="访问量")
    cetegory = models.CharField(choices=(('pxjg','培训机构'),('gx','高校'),('gr',"个人")),max_length=10,verbose_name="机构类别")
    cityinfo = models.ForeignKey(CityInfo,verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "机构信息"
        verbose_name_plural = verbose_name
class TeacherInfo (models.Model):
    image = models.ImageField(upload_to='teacher/', max_length=200, verbose_name="讲师头像")
    name = models.CharField(max_length=20, verbose_name="讲师姓名")
    work_year=models.IntegerField(default=3,verbose_name="工作年限")
    work_position = models.CharField(max_length=20,verbose_name="工作职位")
    work_sytle = models.CharField(max_length=20,verbose_name="教学特点")
    work_company = models.ForeignKey(OrgInfo,verbose_name="所属机构")
    age = models.IntegerField(default=30,verbose_name="讲师年龄")
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), max_length=10, verbose_name="讲师性别", default='girl')
    love_num = models.IntegerField(default=0,verbose_name="收藏量")
    click_num = models.IntegerField(default=0,verbose_name="点击量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "讲师信息"
        verbose_name_plural = verbose_name
