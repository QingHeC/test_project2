#coding:utf-8

from django.urls import path
from desk_center.views import  *


urlpatterns = [
    path(r'', login_entry ,name = "login_"),
    # path(r'/login/', login_entry ,name = "login_"),
    # path(r'/', login_entry ,name = "login_"),
    path(r'index/', home, name="home_in"),
    path(r'log_out/', log_out, name="log_out"),
    path(r'idc/', inde ,name = "index_in"),
    path(r'stagings/', stagings, name="stagings"),
    path(r'task_project/get_project/', get_projectshow, name="get_project_show"),
    path(r'task_project/addGroup_name/', addGroup_project, name="addGroup_project"),    #添加项目
    path(r'task_project/addGroup/', addGroup, name="addGroup"),    #添加分组名
    path(r'task_project/add_project/', add_project, name="add_project"),    #添加项目
    path(r'task_project/add_project/task_project_details/', task_project_details, name="task_project_details"),    #项目页面详情
    path(r'task_project/add_project/task_project_get_list/', task_project_get_list, name="task_project_get_list"),    #项目页面详情
    path(r'task_project/add_project/task_project_details/add_project_name/', add_project_name, name="add_project_name"),    #添加分组模块
    path(r'task_project/add_project/task_project_details/add_project_name/task_name', add_project_task_name, name="add_project_task_name"),    #添加项目任务名
    path(r'task_project/add_project/task_project_details/add_project_name/task_name/show_data', show_data, name="show_data"),    #添加项目模块
    path(r'task_project/', task_project, name="task_project"),
    path(r'distribute/tack/', dis_tack, name="dis_tack"),
    path(r'stagings/app/runtasks/run_myword/', run_word_my, name="run_word_my"),
    path(r'stagings/app/runtasks/add_run/', runtask_addrun, name="runtask_addrun"),
    path(r'stagings/app/runtasks/show_report/', show_reports, name="show_reports"),
    path(r'stagings/app/runtask/', runtask, name="runtask"),
    path(r'add_interface/', add_interface_http, name = "add_http_req"),
    path(r'updates/files/',add_files, name ="add_files"),

]