
    // {#断言请求#}
    function to_req_assert(){
        var tab_req_assert = get_table_assert(document.getElementById('tab_req_assert'),2);

        // {#获取id #}
        var add_id = document.getElementById("add_req_name").getAttribute("valueOf");


        if (!add_id){
            alert("请先保存表单");
            console.log(add_id);
            return false;
        }



        $.ajax({
            url:'{% url "req_assert" %}',
            type:"POST",
            // {#contentType:"application/json",#}
            dataType:"json",
            processData: false,
            contentType: false,
            data:JSON.stringify({
                "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
                "add_id":add_id,
                "tab_req_assert":tab_req_assert
            }),
            success:function (data) {
                if (data["success"]){
                    console.log("后台返回成功");
                    alert(data["data"]["ret_resu"]);

                }else {
                    console.log("后台返回失败");
                    alert(data["fail"]);
                }

                // {#显示返回来的断言结果#}
                show_assert(data["data"]["ret_resu"],data["data"]["result"]);


                // {#alert("提交成功")#}
            }
        })
    };

        function get_ass_help(){
            var dat = "status_code : 状态码 \n" +
                "content  : 返回的数据二进制显示\n" +
                "json : 获取返回的json数据，非json数据不可用"

            alert(dat)
        }

        function select_assert(d){
            // {#this.d.value;#}
            // {#alert(this.d.value);#}
            // {#alert(document.getElementById("tab_req_assert_1").getAttribute("value"));#}
        }

        // {#显示断言结果#}
        function show_assert(d_vi,d_data){
            // {#assert_get_data = document.getElementById("tab_get_assert_req").innerText;#}
            document.getElementById("tab_get_assert_req").innerText = "断言验证结果：" + d_vi + "  " + d_data;


            // {#alert(assert_get_data);#}
            // {#alert(document.getElementById("tab_get_assert_req").getAttribute("value"));#}
        }

        // {#编辑描述#}
        function up_describe(){
        var par = document.getElementById("describe_text").style.display;
        if(par=="none"){
            t = document.getElementById("describe_text_show").innerText;
            // {#alert(t)#}
            document.getElementById("describe_text").value =t;

            document.getElementById("describe_text").style.display="";
            document.getElementById("describe_text_show").style.display="none";

        }
        else{
            document.getElementById("describe_text").style.display="none";
            document.getElementById("describe_text_show").style.display="";
            t = document.getElementById("describe_text").value;
            document.getElementById("describe_text_show").innerText =t;
        }
    }


        // {#显示和隐藏params#}
        function on_params(){
        var par = document.getElementById("par_none").style.display;
        if(par=="none"){
            document.getElementById("par_none").style.display="";
        }
        else{
            document.getElementById("par_none").style.display="none";
        }
    }


        // {#var todata = document.getElementById('add_req');#}
// {#        发送数据，并保存#}
        function tofromdata(id){

            // {#获取当前url参数#}
            var cur_url = document.location.toString();
　　　　    var par_url = cur_url.split("?")[1];
// {#　　　　    var par_url = par_u[1];#}
// {#            alert(par_url);#}
//            接口名ID
            var add_interface_id = document.getElementById('add_req_name').valueOf;

            // {#接口名#}
            var add_req_name = document.querySelector('#add_req_name>h5>input').value;

            // {#编号#}
            // var add_id = document.getElementById("add_req_name").getAttribute("value");
            var add_id = add_interface_id;

            // {#alert(add_req_name)#}
            // {#接口属于：       #}
            // var add_of = document.getElementById("add_of");
            // add_req_of = add_of.getAttribute("value");
            // {#alert(add_req_of);#}
            // if (add_req_of ==""){
            //     alert("接口属于为空，请返回上一级重新选择对应的接口类别。");
            //     return false;
            // }

            var par = document.getElementById("describe_text").style.display;
            if(par=="none"){
                var add_req_texts = document.getElementById("describe_text_show").innerText;
            }
            else{
                var add_req_texts = document.getElementById("describe_text").value;
            }

            var req_data = document.getElementById('req_data').value;
            var url_address = document.getElementById('url_address').value;
            var url_address2 = document.getElementById('url_address2').value;


            // {# Params: #}
            var par = document.getElementById("par_none").style.display;
            if(par=="none"){
                var tab_request_par = {};
            }
            else{
                var tab_request_par = get_tables(document.getElementById('tab_request_par'),2);
            }

            var tab_request_head = get_tables(document.getElementById('tab_request_head'),2);
            // {#alert(tab_request_head)#}
            var ger_id = document.querySelector('.container_fluid .tab-content>div.active').getAttribute('id');
            // {#alert(ger_id);#}

            if(ger_id=="formdata-0001"){
                var form_data = get_formdata_tables(document.getElementById('form_data'),3);
            }
            if(ger_id=="panel-0002"){
                var application_x_w = get_tables(document.getElementById('application_x_w'),2);
            }
            if(ger_id=="panel-0004"){
                // alert("暂未开放")
                // return false;
                var raw_json = document.getElementById('req_json').text;
                console.log(raw_json);
            }
            if(ger_id=="panel-0003"){
                // {#alert("进入上传文件");#}
                // {#var md = update_files();#}
                var fil = "t_file"
                var file_names = get_tables(document.getElementById('update_file2'),2);
                // {#var file_list = document.querySelector("#file_Id").files;#}
                // {#var xhr = new XMLHttpRequest();#}
                 //定义表单变量
                // {#var file = document.querySelector("#file_Id").files;#}
                 //新建一个FormData对象
                 // {#file_lists = new FormData(document.getElementById("file_Id")[0]);#}
                 // {#form_dat = new FormData();#}
                 // {#var formDatas ={};#}
                 //追加文件数据
                // {#form_data.append('jsp',file[0]);#}
                // {# for(i=0;i<file_lists.length;i++){#}
                //       {#formData.append("file["+i+"]", file[i]);#}
                //      {#form_dat.append(file_lists[i]);}#}
                //  {##}
                // {#return false;#}

            }
            // {#console.log(form_dat);#}
            // {##}
            var tab_req_assert = get_table_assert(document.getElementById('tab_req_assert'),5);

            // {#alert("123");#}
            //         {#"csrfmiddlewaretoken":"csrf"#}
            $.ajax({
                url:"/test/interface/add_interface/add_http",
                type:"POST",
                // {#contentType:"application/json",#}
                dataType:"json",
                processData: false,
                contentType: false,
                data:JSON.stringify({
                    "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
                    "id":id,
                    "add_interface_id":add_interface_id,
                    "par_url":par_url,
                    "method":req_data,
                    // "add_req_of":add_req_of,
                    "url":url_address,
                    "url2":url_address2,
                    "add_req_name":add_req_name,
                    "add_id":add_id,
                    "add_req_texts":add_req_texts,
                    "data":{
                        "Params":tab_request_par,
                        "tab_request_head":tab_request_head,
                        "form_data":
                            {
                                "form_data":form_data,
                                "application_x_w":application_x_w,
                                "raw_json":raw_json
                            },
                        "files":file_names,
                        "file_data_Id":fil
                    },
                    "tab_req_assert":tab_req_assert,
                }),
                success:function (data) {

                    if (data["success"]){
                        //get_result
                        console.log("后台返回成功");
                        // console.log(data["body"]);
                        // console.log("后台返回成功");
                        if (data.hasOwnProperty("get_result")) {
                            console.log(data["get_result"]["ret_resu"]);
                            alert("断言结果："+data["get_result"]["ret_resu"]);
                            show_assert(data["get_result"]["ret_resu"],data["get_result"]["result"]);
                        }else {
                            alert("保存成功");
                        }

                        // alert(data["body"]);
                        req_ret_data(data["body"],data["headers"]);

                        // {#console.log(data["body"]);#}
                        // {#alert(data["get_req_data"]);#}
                        if (data["get_req_data"]){
                            // {#alert(data["get_req_data"]);#}
                            show_assert(data["get_req_data"]["ret_resu"],data["get_req_data"]["result"]);
                        }
                        // console.log("id是 %s" %data["data_id"]);
                        // {#alert(req_ret_data);#}
// {#                        添加url参数#}
//                         var url = window.location.href;
//                         if(url.indexOf("ecdi") != -1){
//
//                         }else {
//                             window.location.href = url + "&ecdi="+ data["data_id"] +"";
//                         }
                        // {#window.location.replace("ru='123'");#}
                        // {#alert(window.location.href);#}
                    }else {
                        console.log("后台返回失败");
                        alert(data["fail"]);
                    }


                    // {#alert("提交成功")#}
                }
            })
        };
        


        function update_files(obj){
            // {#var file_lists = document.getElementById("file_Id")[0].files[0];#}
            var file_lists = $("#file_Id1")[0]; //.files[0]
            // {#var file_lists = new FormData(document.getElementById("file_Id")[0]);#}
            // {#file_lists = new FormData(document.getElementById("file_Id")[0]);#}
            var form_dat = new FormData();
            // {#for(var i = 0; i< file_lists.length;i++){#}
            // {#    //file_lists.files[i]#}
            // {#    form_dat.append('files',file_lists.files[i]);}#}
            // {#form_dat.append('files',file_lists)#}
            // {#form_dat.append('files',file_lists.files);#}
            //      {#var formDatas ={};#}
                 //追加文件数据
            //     {#form_data.append('jsp',file[0]);#}
            // {#console.log(file_lists.files.length);#}
            for(i=0;i<file_lists.files.length;i++){
                console.log("这里是 updat_files中");
                //formData.append("file["+i+"]", file[i]);
                //console.log(file_lists.files[i]);
                form_dat.append("files",file_lists.files[i]);}
            // {#form_dat.append("files",file_lists.files);}#}



            // {#console.log(file_lists.files[0]);#}
            // {#console.log(file_lists.files[1]);#}
            console.log(form_dat);

            $.ajax({
                    url: '{% url "add_files" %}',
                    type: 'post',
                    data: form_dat,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        // {#alert(data["files"]);#}
                        // {#console.log(data.files);#}
                        console.log(data["files"]);
                        for(var i = 0;i < data["files"].length;i++){
                            add_table_files(obj,data["files"][i]);
                        }
                    }
                })
        };

        // {#请求网络返回请求消息#}


        // {#处理返回成功的数据，填写在页面上#}
        function req_ret_data(bod ,head){
            // t = document.getElementById("req_response_").innerText = bod;
            // {#alert(t)#}
            // console.log(bod);
            document.getElementById("req_response_").value = bod;
            // $("#req_response_").snippet("javascript", { style: "random", collapse: true, startCollapsed: false});

            // document.getElementById("to_head").value =head;
            // $("#add_req_name").attr("value",data_id);
            // {#document.getElementById("add_req_name").getAttribute("value") = data_id;#}

            // {#getAttribute("value") = data_id;#}
            // {#document.getElementById("add_req_name").value =data_id;#}

        }

        function postfile(){
            // 获得上传文件DOM对象
            var oFiles = document.querySelector("#file_Id");

            // 实例化一个表单数据对象
            var formData = new FormData();
            // 遍历图片文件列表，插入到表单数据中
            for (var i = 0, file; file<file.length; i++) {
                // 文件名称，文件对象
                formData.append(file.name, file);
            }
            return formData;
        };


        function get_tables(table,ce_nub) {
            var tableData = new Array();
            var table_lise = [];

            // {#var table_data = [];#}
            // alert("行数：" + table.rows[1].cells[2].innerHTML);
            var table_datas = {};
            // alert("行数：" + table.rows.length);
            for (var i = 1; i < table.rows.length; i++) {

                    // console.log(table.rows[i].cells[3].childNodes[0].value);
                    // {#console.log(table.rows[i].cells[3].childNodes[0].textContent);#}
        // table_datas.push();
                if (table.rows[i].cells[3].childNodes[0].value == "修改"){
                    var name = table.rows[i].cells[1].innerHTML;
                    table_datas[name] = table.rows[i].cells[ce_nub].innerHTML;

                    // table_datas["keys"] = table.rows[i].cells[1].innerHTML;
                    // table_datas["values"] = table.rows[i].cells[ce_nub].innerHTML;
                }
                if (table.rows[i].cells[3].childNodes[0].value == "删除"){
                    var file_name =  table.rows[i].cells[1].innerHTML;
                    file_name = $.trim(file_name);
                    console.log(file_name);
                    // file_name = $.trim(file_name)
                    table_datas[file_name] = table.rows[i].cells[ce_nub].innerHTML;

                    // table_datas["keys"] = table.rows[i].cells[1].innerHTML;
                    // file_name = $.trim(file_name)
                    // table_datas["values"] = table.rows[i].cells[ce_nub].innerHTML;
                }
                // table_lise.push(table_datas);

                // {#alert(table_datas)#}
                //
                // {#table_data.push(table_datas);#}

            }
            console.log(table_datas);
            return table_datas;

        };


        function get_tables_file(table,ce_nub) {
            var tableData = new Array();
            var table_lise = [];

            // {#var table_data = [];#}
            // alert("行数：" + table.rows[1].cells[2].innerHTML);

            alert("行数：" + table.rows.length);
            for (var i = 1; i < table.rows.length; i++) {
                console.log("111");
                    var table_datas = {};
                    console.log(table.rows[i].cells[3].childNodes[0].value);
                    // {#console.log(table.rows[i].cells[3].childNodes[0].textContent);#}
        // table_datas.push();

                    var file_name = table.rows[i].cells[1].innerHTML;
                    // file_name = $.trim(file_name)
                    table_datas[file_name] = table.rows[i].cells[ce_nub].innerHTML;

                    // table_datas["keys"] = table.rows[i].cells[1].innerHTML;
                    // file_name = $.trim(file_name)
                    // table_datas["values"] = table.rows[i].cells[ce_nub].innerHTML;

                table_lise.push(table_datas);

                // {#alert(table_datas)#}
                //
                // {#table_data.push(table_datas);#}

            }
            console.log(table_lise);
            return table_lise;

        };

        function get_formdata_tables(table,ce_nub) {
            var tableData = new Array();
            var table_datas = [];
            // alert("行数：" + table.rows[1].cells[2].innerHTML);
            // alert("行数：" + table.rows.length);
            for (var i = 1; i < table.rows.length; i++) {
                    console.log(table.rows[i].cells[3].childNodes[0].value);
                    // {#console.log(table.rows[i].cells[3].childNodes[0].textContent);#}
        // table_datas.push();
                var table_data = {}
                if (table.rows[i].cells[ce_nub+1].childNodes[0].value == "修改"){
                    table_data['key'] = table.rows[i].cells[1].innerHTML
                    table_data['values'] = table.rows[i].cells[3].innerHTML;
                    table_data["file_text"] = table.rows[i].cells[2].innerHTML;

                    // {#table_data.push([#}
                    // {#    table.rows[i].cells[1].innerHTML,#}
                    // {#    table.rows[i].cells[2].innerHTML,#}
                    // {#    table.rows[i].cells[3].innerHTML#}
                    // {#])#}
                }
                if (table.rows[i].cells[ce_nub+1].childNodes[0].value == "删除"){
                    table_data['file_name'] = table.rows[i].cells[1].innerHTML
                    table_data['file_md5'] = table.rows[i].cells[2].innerHTML;}

                // {#alert(table_datas)#}
                table_datas.push(table_data);
            }
            console.log(table_datas);
            // {#alert(table_data);#}
            return table_datas;
        };


        // {# 断言列表#}
        function get_table_assert(table,ce_nub) {
            var tableData = new Array();
            // {#var table_datas = {};#}
            // {#var table_datas = [];#}
            // alert("行数：" + table.rows[1].cells[2].innerHTML);

            // alert("行数：" + table.rows.length);
            for (var i = 1; i < table.rows.length; i++) {
        // table_datas.push();
                var data_lis = []
                if (table.rows[i].cells[ce_nub].childNodes[0].value == "修改"){
                    assert_name = table.rows[i].cells[1].innerHTML;

                    assert_left = table.rows[i].cells[2].innerHTML;
                    assert_right_INT = table.rows[i].cells[3].innerHTML;
                    assert_right = table.rows[i].cells[4].innerHTML;
                    // {#data_lis = [assert_name,assert_left,assert_right]#}

                    tableData.push([assert_name,assert_left,assert_right,assert_right_INT]);
                    // {#table_data.push(table_datas);#}
                }else {

                }

                // {#if (table.rows[i].cells[ce_nub].childNodes[0].value == "删除"){#}
                // {#    file_name = table.rows[i].cells[1].innerHTML;#}
                //
                // {#    file_md5 = table.rows[i].cells[2].innerHTML;#}
                //     {#data_lis = [assert_name,assert_left,assert_right]#}
                //
                // {#    tableData.push([file_name,file_md5]);}#}


            }

            return tableData;

        }
// {#                上传文件#}

        function read_files(id) {
            file_lists = [];
            var files = new FormData($(id)[0]);

            // {#get_files = this.files;#}

            console.log(files);



        }

//初始化Table
//
//     $(function() {
//         var source = [];
//
//         function resetTabullet() {
//             $("#table").tabullet({
//                 data: source,
//                 action: function(mode, data) {
//                     console.dir(mode);
//                     if (mode === 'save') {
//                         source.push(data);
//                     }
//                     if (mode === 'edit') {
//                         for (var i = 0; i < source.length; i++) {
//                             if (source[i].id == data.id) {
//                                 source[i] = data;
//                             }
//                         }
//                     }
//                     if (mode == 'delete') {
//                         for (var i = 0; i < source.length; i++) {
//                             if (source[i].id == data) {
//                                 source.splice(i, 1);
//                                 break;
//                             }
//                         }
//                     }
//                     resetTabullet();
//                 }
//             });
//         }
//
//         resetTabullet();
//     });
