from django.db import models
from auto_interface.models import *
import django.utils.timezone as timezone
from auto_interface import models as auto_int_models

# Create your models here.

#分配的任务，名字

class work_tasking_name(models.Model):
    """需要加 给谁的任务、创建时间、执行时间"""
    id = models.IntegerField(primary_key=True)
    describe = models.TextField()   #每个任务的名字
    create_date = models.DateTimeField(auto_now=True)

#用户列表
class list_user_info(models.Model):
    id = models.IntegerField(primary_key=True)
    login_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name_email = models.EmailField()
    phone = models.IntegerField()
    def __str__(self):
        return self.name

#分配任务的列表
class work_tasking_list(models.Model):
    id = models.IntegerField(primary_key=True)
    work_tasking_name_id = models.ForeignKey(work_tasking_name,on_delete=models.CASCADE)# work_tasking_name id
    req_list_data_id = models.ForeignKey(Left_name_data_lists,on_delete=models.CASCADE) # Req_list_data_id 接口
    describe = models.TextField()   #每个接口或每个自动化的名字
    create_date = models.DateTimeField(auto_now=True)


class work_distribution_task(models.Model):
    id = models.IntegerField(primary_key=True)
    list_user_info_id = models.CharField(max_length=255)      #list_user_info id  用户列表 谁给的任务
    list_user_info_name = models.CharField(max_length=255)      #执行人 名字
    req_list_data_id = models.CharField(max_length=255)     #分配的工作ID
    task_name_id = models.CharField(max_length=255)                 # 分配人 id 给他的任务
    task_name_name = models.CharField(max_length=255)                 # 分配人名字
    work_name = models.CharField(max_length=255)        #分配任务的名字
    model_work_name = models.CharField(max_length=255)        #分配任务的名字
    create_date = models.DateTimeField(auto_now=True)


#自己要执行的任务

class work_run_task(models.Model):
    id = models.IntegerField(primary_key=True)          #id
    req_list_data_id = models.CharField(max_length=255)     #任务列表中的id
    run_name = models.CharField(max_length=255)             #运行人的名字
    work_name = models.CharField(max_length=255)            #工作的名字，属于哪个接口
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    if_work = models.CharField(max_length=25)               #是否执行 0为未执行


#添加断言
class desk_center_asserts(models.Model):
    id = models.IntegerField(primary_key=True)
    assert_name = models.CharField(max_length=255)
    describe = models.TextField()       #断言的描述
    lef_NO_num = models.IntegerField()      #用来判断是否有“contrasst” 没有是0 ，有是1, 数字是3, char是5
    # left_contrast = models.CharField(max_length=255,)
    right_NO_num = models.IntegerField()
    # right_contrast = models.CharField(max_length=255)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)




# 添加cook
class sy_cook_vr(models.Model):
    id = models.IntegerField(primary_key=True)
    csrftokens = models.CharField(max_length=255)
    vrs = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255,null=True)
    user_name = models.CharField(max_length=255,null=True)
    user_login_name = models.CharField(max_length=255,null=True)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)


#分组名称，项目左侧分组
class grouping_name_projects(models.Model):
    id = models.IntegerField(primary_key=True)
    gro_name = models.CharField(max_length=255) #分组名称
    gro_text = models.TextField(null=True)      #备注
    power = models.TextField(null=True)         #权限是否公开   私有0    公开1
    create_name = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)

#分组权限
class grouping_name_staff(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=255) #登陆用户账号
    smail = models.CharField(max_length=255) #登陆用户邮箱
    project_id = models.ForeignKey(grouping_name_projects, on_delete=models.CASCADE) #关联grouping_name_projects
    create_name = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)




#项目
class task_projects(models.Model):
    id = models.IntegerField(primary_key=True)
    pro_name = models.CharField(max_length=255)
    pro_text = models.TextField(null=True)
    create_name = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    grouping_name_projects = models.ForeignKey(grouping_name_projects,on_delete=models.DO_NOTHING,null=True)


#项目中的模块
class task_project_model(models.Model):
    id = models.IntegerField(primary_key=True)
    task_projects_id = models.CharField(max_length=20)
    pro_name_model = models.CharField(max_length=255)
    pro_text_model = models.TextField(null=True)
    create_name = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)


#任务名
class task_project_name(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)     #任务名
    agreement = models.CharField(max_length=200)    #协议
    text = models.TextField()                   #备注
    create_name = models.CharField(max_length=255)
    update_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    task_id = models.ForeignKey(task_project_model,on_delete=models.DO_NOTHING,null=True)


#任务运行情况
class work_historys(models.Model):
    id = models.IntegerField(primary_key=True)
    req_id = models.ForeignKey(auto_int_models.Req_list_data,on_delete=models.CASCADE,null=True)
    execute_sign = models.CharField(null=True,max_length=200)       #执行标记--执行时的名字
    run_work_name = models.CharField(max_length=20)     #执行人登录名
    run_work_fullname = models.CharField(max_length=20)     #执行人名字
    task_name = models.CharField(max_length=200)     #标记 和 用例id
    task_state = models.CharField(max_length=200,null=True)     #任务状态，是否执行成功。0默认未执行，1执行成功，-1执行失败
    states = models.CharField(max_length=200)       #是否执行，控制执行 0执行 ，1不执行
    task_module = models.CharField(max_length=200,null=True)       #模块
    execute_situation = models.CharField(max_length=200,null=True)  #执行报告或情况
    execute_situation_path = models.CharField(max_length=255,null=True)  #执行报告路径
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)


#记录执行结果
class work_run_request_history(models.Model):
    id = models.IntegerField(primary_key=True)
    req_id = models.ForeignKey(auto_int_models.Req_list_data,on_delete=models.DO_NOTHING,null=True)
    req_name = models.TextField()    #记录请求名称
    req_url = models.TextField()    #记录请求url
    req_param = models.TextField()    #记录请求param
    req_body = models.TextField()    #记录请求body
    req_headers = models.TextField()    #记录请求headers
    req_assert = models.TextField()    #记录断言
    req_html = models.TextField()    #记录请求返回结果
    req_assert_to = models.TextField()    #记录断言结果
    execute_sign = models.CharField(null=True,max_length=200)       #执行标记--执行时的名字
    run_work_name = models.CharField(max_length=20)     #执行人登录名
    run_work_fullname = models.CharField(max_length=20)     #执行人名字
    task_state = models.CharField(max_length=200,null=True)     #任务状态，是否执行成功。0默认未执行，1执行成功，-1执行失败
    states = models.CharField(max_length=200)       #是否执行，控制执行 0执行 ，1不执行
    task_module = models.CharField(max_length=200,null=True)       #模块
    task_module_id = models.CharField(max_length=200,null=True)       #模块id
    task_sort = models.CharField(max_length=200,null=True)       #分类
    task_sort_id = models.CharField(max_length=200,null=True)       #分类id
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)



class files_save(models.Model):
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    file_md5 = models.CharField(max_length=200)
    update_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default = timezone.now)
    update_date = models.DateTimeField(auto_now=True)