# coding:utf-8

import json
import time,os,re,datetime
import unittest

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

from auto_interface.api_auto.configs.config import run_lis, file_save_path
from auto_interface.api_auto.lib.interface_http import interface_http
from auto_interface.api_auto.ret_list import *
from auto_interface.api_auto.run_interface.interfaces_execute import run_word
from auto_interface.api_auto.run_interface.multiple_test_execute import mul_run_word
from desk_center import models as desk_models
# 验证登录
from desk_center.views import Ver_cook_vr
from desk_center.api_tomethod import *

from test_project.settings import BASE_DIR

# Create your views here.

def auto_inters(request):
    dat = []
    return render(request, "", locals())


# auto_interface_list.html

def auto_inter(request):
    inter_list = models.Req_list_data.objects.all()
    # data = []
    # data = ret_left_interface_listname()
    # data.append(left_list_name_data)
    # print(data)
    # rnter_name_data = models.Left_name_data_lists.objects.select_related('left_name_data_id').all()

    list_inter_name = models.Left_name_data.objects.values("id", "name_data").distinct()
    # print("list_inter_name: %s" %list_inter_name)
    # list_name_data1 = models.Left_name_data_lists.objects.get()

    list_inter_name = models.Left_name_data.objects.values("id", "name_data").distinct()

    data = []
    for lis in list_inter_name:

        # print(lis)
        list_name_data = models.Left_name_data_lists.objects.values("data_list_name", "id").filter(
            left_name_data_id_id=lis["id"]).distinct()
        # print(list_name_data)
        list_data = []
        left_list_name_data = {}
        for list_name in list_name_data:
            li = []
            li.append(list_name["data_list_name"])
            li.append(list_name["id"])
            # list_data[list_name["id"]] = list_name["data_list_name"]
            list_data.append(li)
            # print(list_data)
        left_list_name_data[lis["name_data"]] = list_data

        data.append(left_list_name_data)

    # data = [{' 百度': [['百度测试1', 1], ['百度测试2', 3]]}, {'网易': [['网易1', 2]]}]
    # data = [{'百度': [['百度测试1', '1'], ['百度测试2', '3']]},{'网易': [['网易1', '2']]}]

    return render(request, "auto_interface_list.html", locals())


def auto_inter_if(request):
    return render(request, "", locals())


def auto_inter1(request):
    datas = [
        {"id": "0", "pId": "0", "name": "列表", "open": "false", "iconOpen": "/static/css/auto_in/img/diy/1_open.png",
         "iconClose": "/static/css/auto_in/img/diy/1_close.png"},
        {"id": 111, "pId": 1, "name": "新建1"},
        {"id": 121, "pId": 1, "name": "新建2"},
        {"id": 131, "pId": 1, "name": "新建3"},
        {"id": 2, "pId": 0, "name": "百度天气", "open": "false"},
        {"id": 211, "pId": 2, "name": "百度天气1"},
        {"id": 221, "pId": 2, "name": "百度天气2"},
        {"id": 21, "pId": 2, "name": "百度天气3"},
        {"id": 3, "pId": 0, "name": "百度图片", "open": "false"},
        {"id": 31, "pId": 3, "name": "百度图片1"},
        {"id": 32, "pId": 3, "name": "百度图片2"},
        {"id": 33, "pId": 3, "name": "百度图片3"}

    ]
    dat = json.dumps(datas)
    return render(request, "auto_interface.html", locals())


# 添加HTTP接口页面
def add_interface(request):
    # 验证
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]

    if request.method == "GET":
        u1 = request.get_full_path()
        print("u1 : %s" % u1)
        inter_name = request.GET.get("list_name")
        project_id = request.GET.get("project")

        case_id = request.GET.get("ecdi")
        if case_id:

            # 后续需要验证是否有权限访问

            # 查询响应case id
            try:
                case_dat = models.Req_list_data.objects.values().get(id=case_id)

                print(case_dat)
                param = case_dat["params"]
                if param:
                    param_lis = str_to_json(param)
                    print(param_lis)
                else:
                    param_lis = []

                header_da = case_dat["headers"]
                print("header_da: %s" % header_da)
                if header_da:
                    header_lis = str_to_json(header_da)
                else:
                    header_lis = []
                body_lists = []
                if case_dat["way_body"] == 'form_data':
                    body_lists = models.req_body.objects.values().filter(req_body_id_id=case_id)
                elif case_dat["way_body"] == 'application_x_w':
                    print("case_dat['body'] :%s" %case_dat["body"])
                    if case_dat["way_body"]:
                        body_lists = str_to_json(case_dat["body"])
                    else:
                        body_lists = []
                else:
                    pass
                print(body_lists)

                # 添加文件 files_upload 数据
                get_files = case_dat["file"]
                if get_files:
                    get_files = str_to_json(get_files)
                    # print(get_files)
                else:
                    get_files = []

                # print(type(get_files))


                assert_list = models.autoin_asserts.objects.values().filter(Req_list_data_id_id=case_id)
                # print(assert_list)

            except BaseException as ex:

                print(" ex : %s" % ex)
        else:
            print("没有进入")

        # 显示属于哪个项目
        pro_name = desk_models.task_projects.objects.values("pro_name").get(id=project_id)["pro_name"]
        # print(inter_name)

        # 查找断言数据
        # asser_ts = desk_models.desk_center_asserts.objects.values().all()
        asser_data ={
            "assertEqual":"assertEqual",    #相等
            "assertNotEqual":"assertNotEqual",  #不相等
            "assertIn":"assertIn", #在里面
            "assertNotIn":"assertNotIn", #不在里面
        }
        asser_dat = str(asser_data)
        # for i in asser_ts:
        #     data = {"text": i["assert_name"], "value": i["assert_name"]}
        #     asser_dat += str(data)

        # asser_dat += ""
        # 传入断言数据
        asser_dat = asser_dat.replace("}{", "},{")
        # {'text': 'assertEqual', 'value': 'a'}
        # print("asser_dat:%s" % asser_dat)
    print("111")
    return render(request, "add_interface_data.html", locals())  # ,locals()


# 根据接口名字显示相应的数据
@csrf_exempt
@xframe_options_sameorigin
def list_name(request):
    if request.method == "GET":

        # u = request.path  #路径
        # u =request.get_full_path()  #路径加参数
        # u = request.get_full_path_info() #路径加参数
        # u = request.get_raw_uri()   #全路径
        users = desk_models.list_user_info.objects.values("id", "name", "name_email")
        print(users)

        u1 = request.get_full_path()
        print("u1 : %s" % u1)
        project_number = request.GET.get("project")
        u_id = request.GET.get("id")
        u_name = request.GET.get("data")

        if u_id:
            pass
            # inter_lists = models.Left_name_data_lists.objects.get(id=u)
            # task_project_model_id = desk_models.task_project_model.objects.get(task_project_model_id = project_number)
            # print("task_project_model_id : %s" %task_project_model_id)
            # inter_list = models.Req_list_data.objects.values().filter(of_big_model_id=project_number,
            #                                                           of_big_on_small_model_id=u_id,
            #                                                           of_big_on_small_model=u_name)
            # print(inter_list)
            # print(inter_list)
        else:
            if project_number == "undefined":
                inter_list=[]
            else:
                pass
                # inter_list = models.Req_list_data.objects.values().filter(
                #     of_big_model_id=project_number).distinct()
            # inter_list = models.Req_list_data.objects.all()

    if request.method == "POST":
        # u = request.path()
        # print(u)
        # 左侧列表信息
        data = []
        left_list_name_data = ret_left_interface_listname()
        data.append(left_list_name_data)

        dat = json.loads(request.body)

        aga = dat["id"]
        # print("id是:%s" %aga)

        # inter_list = models.Req_list_data.objects.get(id=str(dat))
        inter_lists = models.Left_name_data_lists.objects.get(id=dat["id"])
        # print(inter_lists)
        inter_list = models.Req_list_data.objects.values().filter(
            data_list_name=inter_lists).distinct()
        # print(inter_list)

        # inter_list2 = models.Req_list_data.objects.get(data_list_name=inter_lists)
        # print(inter_list2)

    return render(request, "task_project_right_list.html", locals())
    # return render(request,"auto_interface_list_right.html",locals())
    # rse = {"success": inter_list}
    # return render_to_response("auto_interface_list_right.html",locals())


# 添加http接口
@csrf_exempt
def add_interface_add(request):

    Ver_cook = Ver_cook_vr(request)


    if request.method == "POST":
        dat = json.loads(request.body)
        print(dat)




        para_url = dat["par_url"]
        print("para_url :%s" % para_url)
        para_url = para_url.rstrip("#")  # 去除后尾# 号
        print("para_url :%s" % para_url)
        prara_list = para_url.split("&")
        para_url_ = {}
        for lis in prara_list:
            li = lis.split("=")
            para_url_[li[0]] = li[1]
        print("para_url_ : %s" % para_url_)

        add_req_name = dat["add_req_name"]
        if add_req_name:
            pass
        else:
            return  HttpResponse(json.dumps({"fail": "请输入接口名称"}))

        add_req_texts = dat["add_req_texts"]
        # add_req_of = dat["add_req_of"]

        # 请求方法
        method = dat["method"]
        url = dat["url"]
        url2 = dat["url2"]

        params = dat["data"]["Params"]
        print("Params")
        # for i in params
        print(params)
        # print(params.keys())
        # if len(params) != 0:
        #     pass
        # else:
        #     params = ""

        header = dat["data"]["tab_request_head"]
        if len(header) != 0:
            pass
        else:
            header = {}
        print("header : %s" % header)
        # form_data = dat["data"]["tab_request_head"]
        # print(dat["data"])

        add_interface_id = dat["add_interface_id"]
        # 判断body是哪个
        way_body = ''
        get_files = ""

        #用于判断是否有数据
        req_id = dat["add_id"]

        if "application_x_w" in dat["data"]["form_data"].keys():
            boy = dat["data"]["form_data"]["application_x_w"]
            way_body = 'form'

            if "Content-Type" in header.keys():
                print("header中有Content-Type")

            else:
                # header["Content-Type"] = "application/x-www-form-urlencoded"
                print("header中没有Content-Type")
        elif 'form_data' in dat["data"]["form_data"].keys():
            way_body = 'form_data'
            boy = dat["data"]["form_data"]["form_data"]
            print("boy : %s" % boy)
        elif 'raw_json' in dat["data"]["form_data"].keys():
            way_body = 'raw_json'
            boy = dat["data"]["form_data"]["raw_json"]

        elif 'files' in dat["data"].keys():
            way_body = 'file'
            # 文件files
            # print(dat["files"])

            get_files = dat["data"]["files"]
            boy = dat["data"]["files"]
            print("get_files:")
            print(get_files)
        else:
            boy = ""
        # print()

        # print("boy是：%s" %boy)

        # if len(boy) != 0 and (len(boy) == 1 and '' not in boy.keys()):
        if boy:
            pass
        else:
            boy = ""
        print(" 验证： %s" % boy)



        # 断言
        tab_req_assert = dat["tab_req_assert"]
        # print("tab_req_assert： %s" %tab_req_assert)


        succ = "添加成功"
        try:
            # 哪个项目
            print("哪个项目")
            # of_big_model_id = para_url_["project"]
            # of_big_model = pro_name = desk_models.task_projects.objects.values("pro_name").get(id=of_big_model_id)[
            #     "pro_name"]

            # 哪个模块
            # print("哪个模块")
            # of_big_on_small_model_id = para_url_["small"].rstrip("#")
            # of_big_on_small_model = \
            #     desk_models.task_project_model.objects.values("pro_name_model").get(id=of_big_on_small_model_id,
            #                                                                         task_projects_id=of_big_model_id)[
            #         "pro_name_model"]

            # 协议
            print("协议")
            agreement = desk_models.task_project_name.objects.values("agreement").get(id=dat["add_interface_id"])
            print(agreement)




            #
            req_htm=""
            ret = {}
            if dat["id"] == 1:
                print("----1-----")
                #查询数据是否存在
                try:
                    get_req_id = models.Req_list_data.objects.get(data_list_id=req_id)
                except:
                    get_req_id=""

                print("get_req_id:%s" %get_req_id)
                if get_req_id:
                    models.Req_list_data.objects.filter(data_list_id_id=req_id).update(
                        name=add_req_name, req=method, url=url,
                        url_address=url2, params=params,
                        headers=header, body=boy, describe=add_req_texts,
                        file=get_files,
                        agreement=agreement["agreement"],
                        way_body=way_body
                    )
                    ret_id = models.Req_list_data.objects.values('id').filter(data_list_id_id=req_id)[0]["id"]
                else:
                    retd = models.Req_list_data.objects.create(name=add_req_name, req=method, url=url,
                                                               url_address=url2, params=params,
                                                               headers=header, body=boy, describe=add_req_texts,
                                                               file = get_files,
                                                               data_list_id_id=dat["add_interface_id"],
                                                               agreement=agreement["agreement"],
                                                               way_body=way_body
                                                               )
                    ret_id = models.Req_list_data.objects.values('id').filter(data_list_id_id=dat["add_interface_id"]).order_by("-id")[0]["id"]


                print("retd: %s" % ret_id)


                # if way_body =="form_data":
                #     for boy_dat in boy:
                #         print(boy_dat)
                #         models.req_body.objects.create(
                #             req_body_id_id=ret_id,
                #             keys=boy_dat["key"],
                #             text_file=boy_dat["file_text"],
                #             values=boy_dat["values"],
                #             describe=''
                #         )


                # 添加断言
                num = 1  # 判断断言右侧是否还需要填写值
                # if tab_req_assert:
                print("tab_req_assert : %s" %tab_req_assert)
                if tab_req_assert:
                    models.autoin_asserts.objects.filter(Req_list_data_id=ret_id).delete()
                    for data_ass in tab_req_assert:

                        # if data_ass[0] != "请选择" or (data_ass[1] != "" and data_ass[2] != ""):
                        ass_dat = models.autoin_asserts.objects.create(
                            Req_list_data_id_id=ret_id,
                            assert_name=data_ass[0],
                            lef_NO_num=1,
                            left_contrast=data_ass[1],
                            right_NO_num=num,
                            right_contrast=data_ass[2],
                            right_contrast_int=data_ass[3]
                        )
                    print("添加断言")

            elif dat["id"] ==0:
                print("-----2-----")
                #发起请求
                print("修改 body :%s " % boy)
                print("修改 header :%s " % header)

                req_url = url+url2

                # params = list_values_tojson(params)
                # boy = list_values_tojson(boy)
                # header = list_values_tojson(header)
                # params = list_values_tojson(params)

                print(req_url)
                print(params)
                print(boy)
                print(header)
                # print(get_file)


                ret_id = add_interface_id
                succ = "请求成功"

                # 文件 get_files
                get_file = []
                print(get_files)
                print("123456")
                print(type(get_files))
                if get_files:
                    for file in get_files.keys():
                        print(file)
                        get_file.append(("files", (file, open(os.path.join(BASE_DIR, file_save_path,file), "rb"))))
                else:
                    get_file = ""
                print("get_file :%s" % get_file)

                req_htm,get_result = interface_http().req_requests(method, url, params=params, data=boy, headers=header, files=get_file, assertE=tab_req_assert)
                print("get_result:")
                print(get_result)

                # 调用http 请求
                print("ret_id : %s" % ret_id)
                #[['assertEqual', 'status_code', '200', 'int'], ['assertEqual', 'status_code', '200', 'int']]
                #断言返回结果
                if tab_req_assert:
                    # runht = bfr(unittest.makeSuite(Testinterfexec, "test_interfac"))
                    print("进入断言")


                # 断言访问 调试注释
                # run_word().run_reqerst_http(ret_id)

                # get_req_data = run_word().run_reqerst_http(ret_id)
                # print(" get_req_data : %s" % get_req_data)
                # print("req_htm: %s" %req_htm.content)

                if add_interface_id == "":
                    print("add_interface_id 为空")
                    print(add_interface_id)
                    ret = {"fail": "请选择接口类型"}
                else:
                    print("-1-1-1-1-")
                    # req_htm = interface_http().req_requests(method, url, params=params, data=boy, headers=header,
                    #                                         files=get_file)

                    print("0")
                    # print(req_htm.text)
                    # print(req_htm.content)
                    # print(req_htm.headers)
                    print("1")
                    if req_htm.headers:
                        print("2")
                        header_data = req_htm.headers

                        print(header_data)
                    else:
                        header_data = " "



                    # 返回列表中加入断言访问情况
                    # 断言访问 调试注释

                    # if get_req_data:
                    #     print("-1-1-")
                    #     ret["get_req_data"] = get_req_data

                    if req_htm.headers and 'gbk' in req_htm.headers["Content-Type"]:
                        ret = {"body": req_htm.content.decode('gbk'),
                               "headers":str(req_htm.headers),
                               "get_result":get_result
                               }  # .decode('utf-8'),"headers":req_htm.headers
                    else:
                        ret = {"body": req_htm.content.decode('utf-8'),
                               "headers":str(req_htm.headers),
                               "get_result": get_result,
                               }
                    # print(ret)

                    # data = req_htm.content.decode('utf-8')
                    # print(req_htm.json().decode('utf-8'))

                # pass
                # print("检测")

            else:
                print("------3----")
                # pass
            # print(retd)
            # print("url: %s" %url)
            # if req_htm.headers and 'gbk' in req_htm.headers["Content-Type"]:
            #     ret = {"success": succ, "body": req_htm.content.decode('gbk'),
            #            "data_id": ret_id}  # .decode('utf-8'),"headers":req_htm.headers
            #
            # else:  # 'utf-8' in req_htm.headers["Content-Type"]:
            ret["success"] = succ


        except BaseException as ex:
            print("进入错误")
            print(ex)
            ret = {"fail": "%s" % ex}

        # print(boy)
        # success

        print("ret:")
        # print(ret)

    return HttpResponse(json.dumps(ret))  # json.dumps(ret)

#添加测试用例
@csrf_exempt
def add_testcase(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        print("进入任务:add_testcase")

        if request.method == "POST":
            dat = json.loads(request.body)
            print(dat)
            models.test_case_listname.objects.create(
                project_name_id_id = int(dat["project_name_id"]),
                add_test_name = dat["add_test_name"],
                add_test_text = dat["add_test_text"],
                create_name = Ver_cook["user_name"],
                create_name_id = Ver_cook["user_id"],
                update_name=Ver_cook["user_name"],
                update_name_id=Ver_cook["user_id"],
            )



        if request.method == "GET":
            pass
        ret = {"success": "添加成功"}
        return HttpResponse(json.dumps(ret))
        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')



#批量执行
@csrf_exempt
def runlist_project(request):
    Ver_cook = Ver_cook_vr(request)
    print("进入请求")
    if Ver_cook:
        try:
            if request.method == "POST":
                dat = json.loads(request.body)
                print("dat:%s" %dat)
                print(dat)
                print(dat["id"])
                print(dat["urid"])
                if dat["urid"]:
                    get_list = models.Req_list_data.objects.values("id","data_list_id__id", "name",
                                                                      "data_list_id__task_id__pro_name_model",
                                                                      "data_list_id__task_id__id",
                                                                      "data_list_id__text", "data_list_id__agreement",
                                                                      "req", "url", "url_address", "params", "headers",
                                                                      "body", "way_body","file").filter(
                        data_list_id__task_id__task_projects_id=dat["id"], data_list_id__task_id=dat["urid"])
                else:
                    get_list = models.Req_list_data.objects.values("id","data_list_id__id", "name",
                                                                      "data_list_id__task_id__pro_name_model",
                                                                      "data_list_id__task_id__id",
                                                                      "data_list_id__text", "data_list_id__agreement",
                                                                      "req", "url", "url_address", "params", "headers",
                                                                      "body", "way_body","file").filter(
                        data_list_id__task_id__task_projects_id=dat["id"])
                print("get_list是：")
                print(list(get_list))
                print(type(list(get_list)))
                get_list = list(get_list)
                print(get_list)


                assert_list_data = []

                #获取时间
                req_name = time.strftime("%Y-%m-%d_%H%M%S%MS", time.localtime())
                for req_data in get_list:
                    print(req_data)

                    assert_data = models.autoin_asserts.objects.values("assert_name",
                                                         "left_contrast",
                                                         "right_contrast",
                                                         "right_contrast_int").filter(Req_list_data_id_id=req_data["id"])

                    # 处理断言数据
                    for ass in assert_data:
                        dat_list = [ass["assert_name"],ass["left_contrast"],ass["right_contrast"],ass["right_contrast_int"]]
                        assert_list_data.append(dat_list)

                    # print("assert_list_data:")
                    # print(assert_list_data)
                    #
                    # print(type(req_data))
                    # print(req_data["name"])
                    req = req_data["req"]
                    req_url = req_data["url"]+req_data["url_address"]
                    params = req_data["params"]
                    body = req_data["body"]
                    # headers = json.loads(req_data["headers"])

                    headers = json.loads(str(req_data["headers"]).replace('\'','"'))
                    # print(type(headers))
                    print("1")
                    print(headers)
                    file = req_data["file"]


                    print(req_url)
                    # headers=json.loads(headers)
                    req_htm, get_result = interface_http().req_requests(req, url=req_url,params =params,data=body,headers=headers,
                                                                        assertE=assert_list_data
                                                                        )

                    desk_models.work_run_request_history.objects.create(
                        req_id_id=req_data["id"],
                        req_name = req_data["name"],
                        req_url = req_url,  #url
                        req_param = params,  # 记录请求param
                        req_body = body,  # 记录请求body
                        req_headers = headers,  # 记录请求headers
                        req_assert = assert_list_data,  # 记录断言
                        req_html = req_htm.content,  # 记录请求返回结果
                        req_assert_to = get_result,  # 记录断言结果
                        execute_sign = req_name,  # 执行标记--执行时的名字
                        run_work_name = Ver_cook["user_id"],  # 执行人登录名Ver_cook["user_id"], Ver_cook["user_name"]
                        run_work_fullname = Ver_cook["user_name"], # 执行人名字
                        task_state = 1,  # 任务状态，是否执行成功。0默认未执行，1执行成功，-1执行失败
                        task_module = req_data["data_list_id__id"], # 模块
                        task_module_id = dat["id"],
                        task_sort = req_data["data_list_id__task_id__pro_name_model"], #分类
                        task_sort_id = req_data["data_list_id__task_id__id"],

                    )



                    print("req_htm是：")
                    # print(req_htm)

                ret = {"success": "成功","req_name":req_name}
        except BaseException as ex:
            print("进入错误")
            ret = {"fail": "%s" % ex}
            print(ret)
        return HttpResponse(json.dumps(ret))


#显示执行结果页面
def get_result(request):
    Ver_cook = Ver_cook_vr(request)
    print("进入请求")
    if Ver_cook:
        if request.method == "GET":
            try:

                u_id = request.GET.get("get_resu")

            except BaseException as ex:
                print("进入错误")
                ret = {"fail": "%s" % ex}
                print(ret)
            return render(request, "show_resu_data.html", locals())



#显示执行结果数据
def get_result_data(request):
    Ver_cook = Ver_cook_vr(request)
    print("进入请求")
    if Ver_cook:
        if request.method == "GET":
            try:
                get_resu = request.GET.get("get_resu")
                get_id = request.GET.get("id")
                get_urid = request.GET.get("urid")
                print(get_id)

                if get_resu:
                    print("进入执行数据")
                    ret = desk_models.work_run_request_history.objects.values(
                        "execute_sign",
                        "req_name",
                        "req_url",
                        "req_param",
                        "req_body",
                        "req_headers",
                        # "req_html",
                        "req_assert",
                        "req_assert_to",
                        "run_work_fullname",
                    ).filter(execute_sign=get_resu)
                else:
                    if get_urid:
                        print("进入历史数据1")
                        ret = desk_models.work_run_request_history.objects.values(
                            "execute_sign",
                            "req_name",
                            "req_url",
                            "req_param",
                            "req_body",
                            "req_headers",
                            # "req_html",
                            "req_assert",
                            "req_assert_to",
                            "run_work_fullname",
                        ).filter(task_module_id=get_id, task_sort_id=get_urid).order_by("-create_date")
                    else:
                        print("进入历史数据2")
                        ret = desk_models.work_run_request_history.objects.values(
                            "execute_sign",
                            "req_name",
                            "req_url",
                            "req_param",
                            "req_body",
                            "req_headers",
                            # "req_html",
                            "req_assert",
                            "req_assert_to",
                            "run_work_fullname",
                        ).filter(task_module_id=get_id).order_by("-create_date")

                ret = list(ret)
                print(ret)

            except BaseException as ex:
                print("进入错误")
                ret = {"fail": "%s" % ex}

            return HttpResponse(json.dumps(ret))



# http接口断言
@csrf_exempt
def req_assert(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
            print("dat:%s" % dat)

            # 删除原来添加的断言
            data = models.autoin_asserts.objects.values().filter(Req_list_data_id=dat["add_id"])
            print("data: %s" % data)
            if data.count() != 0:
                print("进入判断")
                delete_ass = models.autoin_asserts.objects.filter(Req_list_data_id_id=dat["add_id"]).delete()

            num = 1
            for tab_req_assert_list in dat["tab_req_assert"]:
                print(tab_req_assert_list)
                print(tab_req_assert_list[1])
                if tab_req_assert_list[0] != "请选择" and (tab_req_assert_list[1] != "" and tab_req_assert_list[2] != ""):
                    ass_dat = models.autoin_asserts.objects.create(
                        Req_list_data_id_id=dat["add_id"],
                        assert_name=tab_req_assert_list[0],
                        lef_NO_num=1,
                        left_contrast=tab_req_assert_list[1],
                        right_NO_num=num,
                        right_contrast=tab_req_assert_list[2],
                        right_contrast_int=tab_req_assert_list[3]
                    )

            # 断言验证
            get_req_data = run_word().run_reqerst_http(dat["add_id"])
            print("get_req_data： %s" % get_req_data)
            print("dat[add_id]： %s" % dat["add_id"])

        if request.method == "GET":
            pass
        ret = {"success": "添加成功", "data": get_req_data}
        return HttpResponse(json.dumps(ret))
        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

    pass


# 运行接口 interface，运行选择的任务
@csrf_exempt
def run_interfaces(request):

    # 验证
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    user_login = Ver_cook["user_login_name"]

    print("run_interface")
    if request.method == "POST":
        dat = json.loads(request.body)

        print("这是运行任务 %s" % dat)
        i = 0
        for lis in dat["work_run_lists"]:
            i += 1
            run_lis.append([[str(i), lis]])
        # 毫秒
        ms_f = time.time()
        ms = int((ms_f - int(ms_f)) * 1000)

        t_name = time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + "." + str(ms)
        # t_name = t_name + "." + str(ms)

        run_work_name = user_login
        run_work_fullname = user_

        # print("run_work_name %s" % run_work_name)
        # print("run_work_fullname %s" % run_work_fullname)
        #
        work_run_list = ""
        if dat["work_run_lists"][0]:
            work_run_lists = models.Req_list_data.objects.values("of_big_model").get(id=dat["work_run_lists"][0])
            work_run_list = work_run_lists["of_big_model"]
            # print("work_run_lists %s" %work_run_lists)
        desk_models.work_historys.objects.create(
            execute_sign=t_name,  # 执行标记--执行时的名字
            run_work_name=run_work_name,  # 执行人登录名
            run_work_fullname=run_work_fullname,  # 执行人名字
            task_module = work_run_list,
            task_name='start_',  # 标记 和 用例id
            task_state='0',  # 任务状态，是否执行成功   0默认未执行
            states='0',  # 是否执行，控制执行  0执行 ，1不执行
            execute_situation=''  # 执行报告或情况
        )
        for run_id in dat["work_run_lists"]:
            desk_models.work_historys.objects.create(
                execute_sign=t_name,  # 执行标记--执行时的名字
                run_work_name=run_work_name,  # 执行人登录名
                run_work_fullname=run_work_fullname,  # 执行人名字
                task_name=run_id,  # 标记 和 用例id
                req_id_id=run_id,
                task_state='',  # 任务状态，是否执行成功 0默认未执行
                states='0',  # 是否执行，控制执行 0执行 ，1不执行
                execute_situation=''  # 执行报告或情况
            )

        # 应提供该任务是谁的，执行哪些任务
        mul_run_word().run_reqerst_http(dat["work_run_lists"], t_name)
        # run_word().run_word_interf(dat["work_run_lists"], t_name)
        # run_word().run_reqerst_http(dat["work_run_lists"])

        # u1 = run_word().run_word_interf()
        # print("u: %s" %u)
        # print("u: %s" %u)
    ret = {"success": "已执行，详见运行任务"}
    return HttpResponse(json.dumps(ret))


# 删除
@csrf_exempt
def req_list_deletes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        d_id = data["id"]
        print(data)
        reqrun = models.Req_list_data.objects.filter(id=d_id).delete()
        print(reqrun)
        print(d_id)
        ret = {"success": "删除成功"}

    return HttpResponse(json.dumps(ret))


def req_list_updates(request):
    ret = {"fail": "功能暂未实现"}

    return HttpResponse(json.dumps(ret))
