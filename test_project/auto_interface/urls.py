#coding:utf-8

from django.urls import path
from auto_interface.views import  *


urlpatterns = [
    # path(r'', auto_inter, name = "auto_interf"),
    path(r'add_interface',add_interface, name ="add_interface"),
    path(r'add_interface/list_name/',list_name, name ="list_name"),
    # path(r'add_interface/list_name/%d/', list_name, name="list_name"),
    path(r'add_interface/add_http',add_interface_add, name ="add_interface_add"),
    path(r'add_testcase',add_testcase, name ="add_testcase"),
    path(r'add_interface/runlist',runlist_project, name ="runlist"),
    path(r'add_interface/runlist/get_result',get_result, name ="get_result"),
    path(r'add_interface/runlist/get_result_data',get_result_data, name ="get_result_data"),
    path(r'add_interface/add_http/req_assert',req_assert, name ="req_assert"),
    path(r'add_interface/run_interfaces',run_interfaces, name ="run_interfaces"),
    path(r'add_interface/api/list/deletes',req_list_deletes, name ="req_list_deletes"),
    path(r'add_interface/api/list/updates',req_list_updates, name ="req_list_updates"),

]