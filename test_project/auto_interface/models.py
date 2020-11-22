from django.db import models
from desk_center.models import *
# from desk_center import models as desk_models
import django.utils.timezone as timezone
# Create your models here.
class Req_list_data(models.Model):
    # D_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)  #名字
    req = models.CharField(max_length=20)  # 请求方式
    url = models.SlugField(max_length=255)  # 服务器地址
    url_address = models.SlugField(max_length=255)  # url路径地址
    params = models.CharField(max_length=20,null=True) #params
    headers = models.CharField(max_length=20,null=True)   #請求頭
    way_body = models.CharField(max_length=30,null=True)    #请求体的方法
    body = models.CharField(max_length=20,null=True)  #boy体
    file = models.CharField(max_length=255, null=True) #文件
    describe = models.TextField()  # 描述
    data_list_id = models.ForeignKey(to="desk_center.task_project_name",on_delete=models.CASCADE) #关联接口名
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    # assert_id = models.IntegerField()       #断言 id
    agreement = models.CharField(max_length=255)    #协议类型

    # assert_id = models.ForeignKey()

# 请求体
class req_body(models.Model):

    id = models.IntegerField(primary_key=True)
    req_body_id = models.ForeignKey(Req_list_data,on_delete=models.CASCADE) #关联req_list_data
    keys = models.CharField(max_length=255,null=True)   #键
    text_file = models.CharField(max_length=20,null=True)   # 判断是否是 text 还是 file
    values = models.CharField(max_length=255,null=True)     # 值
    describe = models.TextField()                           #描述
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)



#接口名称列表
class Left_name_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name_data = models.CharField(max_length=255)

    def __str__(self):
        return self.name_data

#接口名称列表内容
class Left_name_data_lists(models.Model):
    id = models.IntegerField(primary_key=True)
    left_name_data_id = models.ForeignKey(Left_name_data,on_delete=models.CASCADE)
    data_list_name = models.CharField(max_length=255)

    def __str__(self):
        return self.data_list_name


#测试用例名
class test_case_listname(models.Model):
    id = models.IntegerField(primary_key=True)
    project_name_id = models.ForeignKey(to="desk_center.task_projects",on_delete=models.CASCADE) #关联对应模块
    add_test_name = models.CharField(max_length=255)    #用例名
    add_test_text = models.TextField()  #备注

    create_name = models.CharField(max_length=255)
    create_name_id = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    update_name_id = models.CharField(max_length=255)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)


#添加断言
class autoin_asserts(models.Model):
    id = models.IntegerField(primary_key=True)
    Req_list_data_id = models.ForeignKey(Req_list_data,on_delete=models.CASCADE)    #关联请求表
    assert_name = models.CharField(max_length=255)
    lef_NO_num = models.IntegerField()      #用来判断是否有“contrasst” 没有是0 ，有是1, 数字是3, 字符是5
    left_contrast = models.CharField(max_length=255,blank=True,null=True)
    right_NO_num = models.IntegerField()
    right_contrast = models.CharField(max_length=255,blank=True,null=True)
    right_contrast_int = models.CharField(max_length=100,blank=True,null=True)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

