# coding:utf-8
from typing import List, Any

from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

from desk_center import models
from auto_interface import models as auto_int_models
# Create your views here.
import json, os, time, demjson
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin


from test_project.settings import BASE_DIR
from django_file_md5 import calculate_md5
from django.core import serializers #序列化


# 验证cookies
def Ver_cook_vr(req):
    try:
        vr = req.COOKIES.get("vr")
        cook = req.COOKIES.get("csrftoken")
        print("验证单独加")
        print(vr)
        # if cook == None:
        if vr == None or cook == None:
        # if cook == None:
            print("为空跳转到首页")
            return HttpResponseRedirect('/', {
                'error': "Wrong username or password!"
            })
            # return False
            # return HttpResponseRedirect(req.POST.get('next', '/') or '/')
        else:
            try:
                vr_list = models.sy_cook_vr.objects.values("vrs", "user_name", "user_id","user_login_name").filter(csrftokens=cook).order_by(
                    "-csrftokens")[0]
                print(vr_list["vrs"])
                print(vr)
                if vr == vr_list["vrs"] and vr_list["user_id"] !="":
                    return vr_list
                else:
                    print("vrlist没有此验证")
                    return HttpResponseRedirect('/', {
                        'error': "Wrong username or password!"
                    })
                    # return False
            except:
                return HttpResponseRedirect('/', {
                    'error': "Wrong username or password!"
                })
    except:
        return HttpResponseRedirect(req.POST.get('next', '/') or '/', {
            'error': "Wrong username or password!"
        })


# 添加cookies 到数据库

def add_cook_sql(req, user_id, user_name,login_name):
    vr = req.COOKIES.get("vr")
    cook = req.COOKIES.get("csrftoken")
    print(vr + "  " +cook)

    print(user_id,user_name,login_name)
    print("longn" +login_name)

    models.sy_cook_vr.objects.filter(csrftokens=cook, vrs=vr).update(
        user_id=user_id,
        user_name=user_name,
        user_login_name=login_name,
    )
    print("111111111111")
    # print(get_da.exists())
    # return get_da



# 登录页面
@csrf_protect
def login_entry(request):
    # vr = request.COOKIES.get("vr")
    cook = request.COOKIES.get("csrftoken")

    response = render(request, "index.html")

    vr = "371642342"
    response.set_cookie("vr", value=vr)
    # if vr == None:
    #     vr = "371642342"
    #     print("添加 vr")
    #     print(csrf_protect.__class__.function())
    #     response.set_cookie("vr", vr)
    #     # response.set_cookie("vr",vr,max_age=600)
    #     models.sy_cook_vr.objects.create(
    #         csrftokens="",
    #         vrs=vr,
    #         user_id="",
    #         user_name="",
    #         user_login_name=""
    #     )
    # else:
    #     print("这里是有vr")
    #     models.sy_cook_vr.objects.create(
    #         csrftokens=cook,
    #         vrs=vr,
    #         user_id="",
    #         user_name="",
    #         user_login_name=""
    #     )

        #response.set_cookie("vr", vr)
        # response.set_cookie("vr",vr,max_age=600)

    return response


# 首页
def home(request):
    vr = request.COOKIES.get("vr")
    cook = request.COOKIES.get("csrftoken")
    if vr == None:
        vr = "371642342"
        print("添加 vr")
        # response.set_cookie("vr",vr,max_age=600)
        models.sy_cook_vr.objects.create(
            csrftokens=cook,
            vrs=vr,
            user_id="",
            user_name="",
            user_login_name=""
        )
    else:
        print("这里是有vr")
        models.sy_cook_vr.objects.create(
            csrftokens=cook,
            vrs=vr,
            user_id="",
            user_name="",
            user_login_name=""
        )

    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        response = render(request, "showhome.html")
        vr = request.COOKIES.get("vr")
        cook = request.COOKIES.get("csrftoken")


        if request.method == "POST":
            user = request.POST['user']
            pwd = request.POST['pwd']
            print("user:%s" % user)
            print("pwd:%s" % pwd)
            try:
                find_user = models.list_user_info.objects.values("id", "name", "password").filter(
                    login_name=user).order_by("-login_name")
                print(find_user)


                print("用户是否存在：")
                print(find_user.exists())
                # add_cook_sql(vr, cook, )
                if find_user.exists():

                    if find_user[0]["password"] == pwd:

                        print("用户名和密码正确")
                        # add_cook_sql(request, find_user[0]["id"], find_user[0]["name"])
                        # user = [find_user[0]["id"], find_user[0]["name"]]
                        print("user: " + user)
                        # 给相应的cook 加上用户名
                        add_cook_sql(request, find_user[0]["id"], find_user[0]["name"],user)
                        # user = {find_user[0]["id"]:find_user[0]["name"]}
                        # return render(request, "select_test_means.html",locals())
                        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
                        return render(request, "showhome.html", locals())
                        # return HttpResponseRedirect(request.POST.sget('next'))
                        # return render(request, "task_projects.html",locals())


                    else:
                        return HttpResponseRedirect(request.POST.sget('next', '/') or '/', {
                            'error': "Wrong username or password!"
                        })

                else:
                    return HttpResponseRedirect(request.POST.sget('next', '/') or '/', {
                        'error': "Wrong username or password!"
                    })
            except:

                return HttpResponseRedirect(request.POST.get('next', '/') or '/')

            print("1234")
        if request.method == "GET":
            pass

        return render(request, "showhome.html")
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

    # return response
    # return render(request, "select_test_means.html")
    # return render(request, "showhome.html")


# 退出,退出登录人所有账号
def log_out(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        user_ = Ver_cook["user_name"]
        user_Id = Ver_cook["user_id"]
        models.sy_cook_vr.objects.filter(user_name=user_,user_id=user_Id).delete()

        return HttpResponseRedirect(request.POST.get('next', '/') or '/')


# 项目页面
def task_project(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        # 给相应的cook 加上用户名

        # add_cook_sql(request)user_name","user_id
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        if request.method == "GET":

            task_pro = models.task_projects.objects.all()

        # elif request.method =="POST":
        #     dat = json.loads(request.body)
        #
        #     task_pro = models.task_projects.objects.values().filter(grouping_name_projects_id=dat["did"])
        # else:
        #
        #     task_pro = models.task_projects.objects.all()

        #项目列表
        project_list = models.grouping_name_projects.objects.all()

        return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

#显示分组的项目
@csrf_exempt
@xframe_options_sameorigin
def get_projectshow(request):
    Ver_cook = Ver_cook_vr(request)
    # print(Ver_cook)
    if Ver_cook:

        # 给相应的cook 加上用户名

        # add_cook_sql(request)user_name","user_id


        if request.method =="POST" :
            print("这是post请求")
            dat = json.loads(request.body)
            print(dat)

            task_pro = models.task_projects.objects.values_list("id","pro_name","pro_text").filter(grouping_name_projects_id=dat["did"])


            task_pro = list(task_pro)
            dat = []
            if task_pro:
                for i in task_pro:
                    data_json = {"id":i[0],"pro_name":i[1],"pro_text":i[2]}
                    dat.append(data_json)



            return HttpResponse(json.dumps({"success": "查询成功","data":dat}))

        #分组列表
        # project_list = models.grouping_name_projects.objects.all()


    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')




#分组名

@csrf_exempt
def addGroup(request):
    Ver_cook = Ver_cook_vr(request)
    print("打印")
    print(Ver_cook)
    if Ver_cook:

        # use= [Ver_cook["user_id"], Ver_cook["user_name"]]
        if request.method == "POST":
            dat = json.loads(request.body)
            print("数据：")
            print(dat)
            if dat["pro_name"]:

                models.grouping_name_projects.objects.create(
                    gro_name= dat["pro_name"],
                    gro_text= dat["pro_text"],
                    create_name= Ver_cook["user_login_name"],
                    update_date= Ver_cook["user_login_name"],
                )
                ret = {"success": "添加成功"}
            else:
                ret = {"success": "添加失败"}
            # models.task_projects.objects.create(
            #             #     pro_name=dat["pro_name"],
            #             #     pro_text=dat["pro_text"],
            #             #     create_name="",
            #             # )


        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')





# 添加分组
@csrf_exempt
def addGroup_project(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        # user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        if request.method == "POST":
            dat = json.loads(request.body)
            print(dat)
            models.task_projects.objects.create(
                pro_name=dat["pro_name"],
                pro_text=dat["pro_text"],
                create_name="",
            )
            ret = {"success": "添加成功"}

        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

# 添加项目
@csrf_exempt
def add_project(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        if request.method == "POST":
            dat = json.loads(request.body)
            print(dat)

            if dat["pro_name"] and dat["pro_pid"]:
                models.task_projects.objects.create(
                    pro_name=dat["pro_name"],
                    pro_text=dat["pro_text"],
                    create_name= Ver_cook["user_login_name"],
                    grouping_name_projects_id= dat["pro_pid"],
                )
                ret = {"success": "添加成功"}
            else:
                if dat["pro_pid"]:
                    ret = {"success": "项目名必填"}
                else:
                    ret = {"success": "请先选择分组"}

        return HttpResponse(json.dumps(ret))
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')


# 项目页面详情
def task_project_details(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        # response = render(request, "index.html")
        if request.method == "POST":
            pass
        if request.method == "GET":

            ctd = request.GET.get("ctd")
            print("ctd:%s" %ctd)
            print("ctd:%s" %ctd)
            u = request.GET.get("id")
            print("u：%s" % u)
            if ctd =="":
                auto_int_models.test_case_listname.objects.values().filter(
                    project_name_id=u
                )

            # 查询相应的项目

            # read_task_project = models.task_projects.objects.values("id", "pro_name", "pro_text").filter(id=u)
            read_task_project = models.task_projects.objects.values("id", "pro_name", "pro_text","grouping_name_projects__gro_name").filter(id=u)
            # models.task_projects.objects.annotate()

            # print(dataas)
            revert_lists = []
            print(read_task_project)
            for read_tp in read_task_project:
                date = {'id': read_tp["id"], 'name': read_tp["pro_name"], 'text': read_tp["pro_text"]}
                # date = '{id:%s, name: %s, text: %s}'%( read_tp["id"], read_tp["pro_name"], read_tp["pro_text"])
                revert_lists.append(date)


            print(revert_lists)
            data_reques = models.Req_list_data.objects.values("id", "name", "data_list_id__task_id__pro_name_model",
                                                              "data_list_id__text", "data_list_id__agreement",
                                                              "req", "url", "url_address", "params", "headers",
                                                              "body", "way_body").filter(
                data_list_id__task_id__task_projects_id=u)

            print("data_reques:")
            print(list(data_reques))
            data_reques = list(data_reques)

            # 显示相应项目下面的模块名

            task_project_datas = models.task_project_model.objects.values("id", "pro_name_model",
                                                                          "pro_text_model").filter(task_projects_id=u)
            task_project_names = models.task_project_name.objects.values().filter(task_id__task_projects_id=u)

            print("task_project_names : %s" % task_project_names)
            print("task_project_datas : %s" % task_project_datas)
            task_Datas = []
            task_names = []
            for task_data in task_project_datas:
                task_Datas.append([task_data["id"], task_data["pro_name_model"], task_data["pro_text_model"]])

            for task_name in task_project_names:
                task_names.append([task_name["id"], task_name["name"], task_name["text"],task_name["task_id_id"]])
            print(task_Datas)


            task_case_names = auto_int_models.test_case_listname.objects.values("id","add_test_name").filter(project_name_id=u)

            case_names = []
            for case_name in task_case_names:
                case_names.append([case_name["id"],case_name["add_test_name"]])

            print("case_names")
            print(case_names)


            return render(request, "task_project_details.html", locals())


#获取当前模块，分组下列表数据
@csrf_exempt
def task_project_get_list(request):
    # models.task_project_model.objects.values(id).filter(task_project_id=u)
    # models.task_project_name.objects.values(task_project).filter(task_id_id="")
    id = request.GET.get("id")
    urid = request.GET.get("urid")

    ctd = request.GET.get("ctd")
    # 用例列表
    ctd_list = request.GET.get("ctd_list")

    print("urid:")
    print(id)
    print(urid)
    print(ctd)
    if ctd=="":
        print("ctd")
    if urid =="":
        print("urid 空")
    if urid or urid=="":
        if urid:
            data_reques = models.Req_list_data.objects.values("data_list_id__id", "name", "data_list_id__task_id__pro_name_model",
                                                          "data_list_id__text", "data_list_id__agreement",
                                                          "req", "url", "url_address", "params", "headers",
                                                          "body", "way_body").filter(
                data_list_id__task_id__task_projects_id=id, data_list_id__task_id=urid)
        else:
            data_reques = models.Req_list_data.objects.values("data_list_id__id", "name", "data_list_id__task_id__pro_name_model",
                                                          "data_list_id__text", "data_list_id__agreement",
                                                          "req", "url", "url_address", "params", "headers",
                                                          "body", "way_body").filter(
                data_list_id__task_id__task_projects_id=id )
    elif ctd or ctd=="":
        print("进入ctd")
        if ctd == "":
            data_reques = auto_int_models.test_case_listname.objects.values("id","add_test_name","add_test_text").filter(
                project_name_id=id
            )
        else:
            data_reques = auto_int_models.test_case_listname.objects.values("id","add_test_name","add_test_text").filter(
                project_name_id=id,

            )
    else:
        data_reques = models.Req_list_data.objects.values("data_list_id__id", "name",
                                                          "data_list_id__task_id__pro_name_model",
                                                          "data_list_id__text", "data_list_id__agreement",
                                                          "req", "url", "url_address", "params", "headers",
                                                          "body", "way_body").filter(
            data_list_id__task_id__task_projects_id=id)

    print("data_reques:")
    print(list(data_reques))
    data_reques = list(data_reques)

    return HttpResponse(json.dumps(data_reques))

#返回右侧接口页面数据
@csrf_exempt
def show_data(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]

        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
            print(dat)


            try:
                TaskProject_name = models.task_project_name.objects.values("id","name","agreement").get(id=dat["id"])

                to_data = {"id": TaskProject_name["id"], "name": TaskProject_name["name"], "agreement": TaskProject_name["agreement"]}

                get_Req_data = auto_int_models.Req_list_data.objects.values("name","req","url","url_address",
                                                                            "params","headers","way_body",
                                                                            "body","file","agreement").filter(data_list_id=dat["id"]).distinct().order_by("create_date")[0]


                get_asserts = auto_int_models.autoin_asserts.objects.values("assert_name","left_contrast","right_contrast","right_contrast_int").filter(Req_list_data_id__data_list_id=dat["id"])

                if get_asserts:
                    to_data["get_asserts"] = list(get_asserts)


                if get_Req_data:
                    to_data["get_Req_data"] = get_Req_data

                else:
                    pass
                print("to_data")
                print(to_data)

            except Exception as e:
                print("错误：%s" % e)
                ret = {"fail": "操作失败"}

            ret = {"success": "添加成功","data":to_data}
            print(ret)

            return HttpResponse(json.dumps(ret))
        if request.method == "GET":
            pass

        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')



# 添加任务分类
@csrf_exempt
def add_project_name(request):
    # 验证
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]

        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
            print("dat")
            print(dat["model_pro_name"])
            if len(dat["model_pro_name"]) >0:


                try:
                    # 向数据库添加相应项目的 模块
                    models.task_project_model.objects.create(
                        task_projects_id=dat["model_pro_id"],
                        pro_name_model=dat["model_pro_name"],
                        pro_text_model=dat["model_pro_text"]
                    )


                except Exception as e:
                    print("错误：%s" % e)
                    ret = {"fail": "操作失败"}

                ret = {"success": "添加成功"}
                return HttpResponse(json.dumps(ret))
            else:
                ret = {"fail": "请输入分类名"}
                return HttpResponse(json.dumps(ret))
        if request.method == "GET":
            pass

        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

#添加任务名
@csrf_exempt
def add_project_task_name(request):
    # 验证
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:
        user = [Ver_cook["user_id"], Ver_cook["user_name"]]
        print(user)
        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
            print(dat)
            print("12345567")

            if dat["task_name"]=="":
                ret = {"fail": "任务名不能为空"}
                return HttpResponse(json.dumps(ret))

            # try:
                # 向数据库添加相应分组任务名
            models.task_project_name.objects.create(
                task_id_id=dat["task_Label"],
                name=dat["task_name"],
                agreement=dat["task_agreement"],
                text=dat["task_text"],
                create_name=user[0],
                update_name=user[0]
            )


            # except Exception as e:
            #     print("错误：%s" % e)
            #     ret = {"fail": "操作失败"}

            ret = {"success": "添加成功"}
            return HttpResponse(json.dumps(ret))
        if request.method == "GET":
            pass

        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')



def inde(request):
    return render(request, "test_sum.html")


def add_interface_http(request):
    return render(request, "ad_interface.html")


def stagings(request):
    # 验证
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    # print("user_Id :%s" %user_Id)

    # work_tasking_name = models.work_tasking_name.objects.all().distinct().order_by('describe')
    work_tasking_name = models.work_distribution_task.objects.values("model_work_name").filter(
        task_name_id=user_Id).distinct().order_by('model_work_name')
    print("work_tasking_name:%s" % work_tasking_name)


    return render(request, "staging_tasks.html", locals())
    # return render(request,"stagings.html",locals())


# 查询，显示分配给自己的任务
@csrf_exempt
def runtask(request):
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    if request.method == "GET":
        mod_name = request.GET.get("mod_name")
        print("u_id:%s" % mod_name)
        if mod_name:
            # work_name = models.work_tasking_name.objects.values("describe").get(id=mod_name)
            # work_name = models.work_distribution_task.objects.values("req_list_data_id").get(model_work_name=mod_name)
            # print("work_name:%s" %work_name)
            user = user[0]  # 当前用户是 task_name_id
            work_lists = models.work_distribution_task.objects.values("id", "req_list_data_id").filter(
                model_work_name=mod_name, task_name_id=user)
            print("work_lists %s" % work_lists)
            # .filter(left_name_data_id_id=lis["id"]).distinct()

            work_data_lis = []
            for work_in in work_lists:
                work_data_lis.append(work_in["req_list_data_id"])
                print("work_in:%s" % work_in)

            # auto_int_models.
            # 根据当前用户任务id 查询相应的任务
            req_listdata = auto_int_models.Req_list_data.objects.values().filter(id__in=work_data_lis).distinct()

        print("get请求")
    if request.method == "POST":
        dat = json.loads(request.body)
        print(dat)
        # dat 哪个任务
        work_name = models.work_tasking_name.objects.values("describe").get(id=dat["id"])
        user = user[0]  # 当前用户是 task_name_id
        work_lists = models.work_distribution_task.objects.values("id", "req_list_data_id").filter(task_name_id=user)

        # .filter(left_name_data_id_id=lis["id"]).distinct()

        work_data_lis = []
        for work_in in work_lists:
            work_data_lis.append(work_in["req_list_data_id"])
            print("work_in:%s" % work_in)

        # auto_int_models.
        # 根据当前用户任务id 查询相应的任务
        req_listdata = auto_int_models.Req_list_data.objects.values().filter(id__in=work_data_lis)
        print(req_listdata)
        id = dat['id']
    to_url = "/stagings/app/runtask/1"

    return render(request, "run_task_lisk.html", locals())


def show_reports(request):
    if request.method == "GET":
        u_id = request.GET.get("show")
        print("u_id:%s" % u_id)
        execute_sign = models.work_historys.objects.values("execute_sign").filter(id=u_id)[0]
        print("execute_sign :%s" % execute_sign)
        show_data = models.work_historys.objects.values("task_name").filter(execute_sign=execute_sign["execute_sign"])
        print("show_data : %s" % show_data)
        # da = models.work_historys.objects.values().filter(req_id_id = '23').Req_list_data
        # print(" task : %s" %show_data["task_name"])
        task_names = []
        for task_n in show_data:
            task_names.append(task_n["task_name"])
        print(" task_names :%s" % task_names)

        dats = models.work_historys.objects.values("id",
                                                   "req_id__name",
                                                   "req_id__agreement",
                                                   "req_id__req",
                                                   "req_id__url",
                                                   "req_id__describe",
                                                   "execute_sign",
                                                   "task_name",
                                                   "task_state",
                                                   "execute_situation",
                                                   "update_date"
                                                   ).filter(execute_sign=execute_sign["execute_sign"])[1:]

        print(dats)

        da = auto_int_models.Req_list_data.objects. \
            values(
            "id",
            "name",
            "agreement",
            "req",
            "url",
            "describe",
            "work_historys__execute_sign",
            "work_historys__task_name",
            "work_historys__task_state",
            "work_historys__execute_situation",
            "work_historys__update_date"

        ).filter(
            work_historys__task_name__in=task_names, work_historys__execute_sign=execute_sign["execute_sign"]
        )

        # da = models.work_historys.objects.select_related('Req_list_data').filter(Req_list_data_id = '23').all()
        # print("da: %s" %da)
        # print(da.all())
        # da = auto_int_models.Req_list_data.objects.filter(id__in=models.work_historys.objects.values("task_name").
        #                                              filter(execute_sign=execute_sign["execute_sign"]
        #                                                     )).all()
        # print("da : %s" %da)

        # 显示报告， 因参数化问题注释
        # print("execute_situation_path : %s" %execute_path)
        # file_path = execute_path["execute_situation_path"].replace('\\','/')
        # with open('%s' %file_path ,'rb')  as f:
        #     htm = f.read()
        # return HttpResponse(htm)
        # return HttpResponseRedirect(request.POST.get(execute_path["execute_situation_path"]))
        # return render(request, execute_path["execute_situation_path"], locals())
        return render(request, "show_performances.html", locals())


# 给自己分配执行的任务
@csrf_exempt
def runtask_addrun(request):
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    if request.method == "POST":
        dat = json.loads(request.body)

        # 运行人的id
        run_name = user_Id
        print(dat)
        if dat["work_run_lists"]:
            for req in dat["work_run_lists"]:
                # 获取当前要分配任务的信息
                ruq_list = auto_int_models.Req_list_data.objects.values().filter(id=req)
                print("ruq_list: %s" % ruq_list)
                for i in ruq_list:
                    print(i["data_list_name"])
                    crat = models.work_run_task.objects.create(
                        req_list_data_id=req,
                        run_name=run_name,
                        work_name=i["data_list_name"],
                        if_work=0
                    )

                    print(crat)
            # print("不是空的")
            # auto_int_models.Req_list_data.objects.

        ret = {"success": "分配成功"}
    return HttpResponse(json.dumps(ret))


# 执行任务, 显示任务执行情况
def run_word_my(request):

    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    user_login = Ver_cook["user_login_name"]
    if request.method == "GET":
        u_descr = request.GET.get("describe")
        print("u_descr:%s" % u_descr)
        u_user = user_Id
        execute_sign = user_login
        run_work = models.work_historys.objects.values().filter(run_work_name=execute_sign, task_name='start_', task_module = u_descr).order_by("-update_date").filter()

        # word_task_id = models.work_distribution_task.objects.values("req_list_data_id").filter(model_work_name = u_descr,task_name_id = u_user)
        # print("word_task_id :%s" %word_task_id)
        # req_list_data = []
        # for req_list in word_task_id:
        #     req_list_data.append(req_list['req_list_data_id'])
        # print("req_list_data:%s" %req_list_data)

        # run_req_list = models.Req_list_data.objects.values().filter(id__in=req_list_data)

    return render(request, "staging_run_my_work.html", locals())


# 分配处理人
@csrf_exempt
def dis_tack(request):
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        # ret_create = models.work_distribution_task.objects.create(task_name_id=data["task"],)

        # 查询分配的任务属于哪个接口任务
        Left_data = auto_int_models.Req_list_data.objects
        # list_name_data = auto_int_models.Req_list_data.objects.values("data_list_name").filter(
        #     id=data["get_tables"][0]).distinct()
        list_name_data = auto_int_models.Req_list_data.objects.values("of_big_on_small_model").get(
            id=data["get_tables"][0])
        print("list_name_data: %s" % list_name_data["of_big_on_small_model"])

        # 添加分配任务的名字
        models.work_tasking_name.objects.create(describe=list_name_data["of_big_on_small_model"])
        print("get_tables： %s" % data["get_tables"])

        # 分配人
        list_user_info_id = user[0]
        list_user_info_name = user[1]

        try:
            for distribution_man in data["task"]:
                # distribution_man 执行人
                print("distribution_man:%s" % distribution_man)
                # 执行人
                task_name_name = models.list_user_info.objects.values().filter(id=distribution_man)[0]["name"]

                print(" task_name_name : %s" % task_name_name)

                for work_table in data["get_tables"]:
                    print("work_table:%s" % work_table)
                    list_name_data_ = auto_int_models.Req_list_data.objects.values("of_big_model",
                                                                                   "of_big_on_small_model").get(
                        id=work_table)
                    print("list_name_data_ %s" % list_name_data_)
                    ret_create = models.work_distribution_task.objects.create(
                        task_name_id=distribution_man,  # 执行人ID
                        task_name_name=task_name_name,
                        work_name=list_name_data_["of_big_on_small_model"],
                        model_work_name=list_name_data_["of_big_model"],
                        req_list_data_id=work_table,
                        list_user_info_id=list_user_info_id,
                        list_user_info_name=list_user_info_name
                    )
                    print("ret_create:%s" % ret_create)
            ret = {"success": "分配成功"}
        except Exception as e:

            print("错误：%s" % e)
            ret = {"fail": "操作失败"}

    return HttpResponse(json.dumps(ret))


# 用来接收客户端上传的附件
@csrf_exempt
def add_files(request):
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    times = time.strftime("%Y-%m-%d", time.localtime())
    if request.method == "POST":
        files = request.FILES.getlist("files")
        print("获取文件：")
        print(files)
        file_save_path = "save_files"
        ret_dat = []
        for i in files:
            file_name = i.name
            print("这是i： %s" % i)
            # print(type(file_name))
            md = calculate_md5(i)
            print("md5:%s" % md)

            ret_dat.append([file_name , md])

            f_name_path = open(os.path.join(BASE_DIR, file_save_path, i.name), 'wb')

            print("f_name_path 路径是：%s" % f_name_path)
            for chunk in i.chunks():
                f_name_path.write(chunk)
            f_name_path.close()

            models.files_save.objects.create(
                file_name = i.name,
                file_path = file_save_path,
                file_md5 = md,
                update_name = user_Id
            )


        # print(len(files))

        ret = {"fail": "fanhiu","files":ret_dat}
        print(ret)
    return HttpResponse(json.dumps(ret))
