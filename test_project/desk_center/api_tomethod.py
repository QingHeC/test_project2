# coding:utf-8

import json


def str_to_json(data):
    data_jso = json.loads(data.replace("'", "\""))
    data_lis = []
    for i_list in data_jso.keys():
        data_lis.append([i_list, data_jso[i_list]])
    return data_lis


def list_values_tojson(data):
    json_data = {}
    for dat in data:
        unm = 0
        key_data = ""
        value_data = ""
        print("--转换valus---")
        # print(dat.keys())
        # print(dat)

        for da in dat.keys():

            if unm ==0:
                key_data = dat[da]
            elif unm == 1:
                json_data[key_data] =  dat[da]
            unm+=1

    print("json_data:")
    print(json_data)
    return json_data
