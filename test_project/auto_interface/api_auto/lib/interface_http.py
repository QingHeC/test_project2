#coding:utf-8

from .read_json import str_con_json
import requests, json
import unittest
from BeautifulReport import BeautifulReport as bfr



class Test_assert(unittest.TestCase):

    def __init__(self,name,html_data,assertE):
        super().__init__()
        self.name = name
        self.html_data = html_data
        self.assertE = assertE

    def runTest(self):
        print("断言：")
        print(self.assertE)
        # [['assertEqual', 'status_code', '200', 'int'], ['assertEqual', 'status_code', '200', 'int']]
        for ass in self.assertE:
            if ass[3] == 'str':
                print(ass)
                getattr(self, ass[0])(
                    getattr(self.html_data,ass[1]),ass[2])
            elif ass[3] == 'int':
                print(ass)
                getattr(self, ass[0])(
                    getattr(self.html_data, ass[1]), int(ass[2]))
            elif ass[3] == 'json':
                dat_json1 = json.loads(ass[2])
                print(type(dat_json1))
                getattr(self, ass[0])(
                    eval("self.html_data.", ass[1]), int(ass[2]))


class interface_http():

    def __init__(self):
        pass

    def req_get(self,url, params, header=""):
        print(type(params))
        try:
            if type(params).__name__ != "dict":
                sj = str_con_json(params)
                if sj:
                    params = sj
        except:
            pass

        htt = requests.get(url=url,params=params ,headers=header)
        print(htt.content,htt.status_code)

    def req_post(self,url, params,request_data, header=""):
        htt = requests.post(url=url, params=params,data=request_data, headers=header)
        print(htt.content, htt.status_code)
        print("post")
        pass

    def req_requests(self,method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            timeout=None,proxies=None,json=None, assertE=None):

        print(files)
        hrm = requests.request(method,
                               url = url,
                               params = params or {},
                               data = data or {},
                               headers = headers, cookies=None, files=files,
                               timeout=None, allow_redirects=True, proxies=None,
                               json=None
                               )
        ret_resu = {}
        if assertE:
            # runht = bfr(unittest.makeSuite(Test_assert, "setUp"))
            # runht = bfr(unittest.makeSuite(Test_assert, "test_"))
            suite = unittest.TestSuite()
            unm_i = 0
            # if assertE:
            unm_i = 0
            # for ass in assertE:
            #     suite.addTest(Test_assert("test_" + str(unm_i),hrm,ass))
            #     unm_i+=1

            suite.addTest(Test_assert("test_" + str(unm_i), hrm, assertE))
            get_result = unittest.TextTestRunner(verbosity=2).run(suite)



            if get_result.failures:
                print("这是错误0: %s---" % (get_result.failures[0][1].split("getattr")[-1]))
                ret_resu["ret_resu"] = "Fail"
                ret_resu["result"] = get_result.failures[0][1].split("getattr")[-1]
                # ret_resu = ht.failures[0][1].split("getattr")[-1]
                # print(ht.failures[0][1].split("getattr")[-1])
                # print("=============")
            elif get_result.errors:
                ret_resu["ret_resu"] = "Error"
                ret_resu["result"] = get_result.errors[0][1].split("getattr")[-1]
                # ret_resu = ht.errors[0][1].split("getattr")[-1]
                print("这是错误:%s ---" % (get_result.errors[0][1].split("getattr")[-1]))
                # print(ht.errors)
            else:
                ret_resu["ret_resu"] = "OK"
                ret_resu["result"] = ""
                # ret_resu = "OK"
            print(ret_resu)



        # print(hrm.content.decode())
        return hrm ,ret_resu

    def run_list(self):
        pass


if __name__ == "__main__":
    htm = interface_http().req_requests("get","https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=2019%E5%B9%B44%E6%9C%88&co=&resource_id=6018&t=1553993862251&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu")
    print(htm.content.decode("ISO-8859-1"))
    print(htm.headers["Content-Type"])
    data = {"da":htm.content.decode("gbk")}
    h = json.dumps(data)
    print(h)