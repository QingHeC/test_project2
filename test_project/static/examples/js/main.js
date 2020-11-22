$(document).ready(function(){

    //本地数据
    var items = [{'id': 18, 'name': '55', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '', 'data_list_id__agreement': 'http', 'req': 'GET', 'url': 'http://t.weather.sojson.com', 'url_address': '/api/weather/city/101030100', 'params': '[]', 'headers': '{}', 'body': "[{'key': 'fo1', 'values': 'fo1', 'file_text': 'text'}, {'key': 'fo2', 'values': 'fo2', 'file_text': 'text'}]", 'way_body': 'form_data'}, {'id': 19, 'name': '分组', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '', 'data_list_id__agreement': 'http', 'req': 'GET', 'url': '', 'url_address': '', 'params': '[]', 'headers': "{'Content-Type': 'application/x-www-form-urlencoded'}", 'body': "[{'keys': 'xx1', 'values': 'xx1'}, {'keys': 'xx2', 'values': 'xx2'}]", 'way_body': 'application_x_w'}, {'id': 20, 'name': 'zzz', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '1', 'data_list_id__agreement': 'HTTP', 'req': 'GET', 'url': '', 'url_address': '', 'params': '[]', 'headers': '{}', 'body': "[{'key': '1', 'values': '2', 'file_text': 'text'}]", 'way_body': 'form_data'}, {'id': 23, 'name': 'test1', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '', 'data_list_id__agreement': 'HTTP', 'req': 'GET', 'url': '', 'url_address': '', 'params': '[]', 'headers': '{}', 'body': "[{'keys': ' 一对黑白色小猫可爱图片_彼岸图网.jpg', 'values': '4c137e89724828e31cadca1fce32ab88'}]", 'way_body': 'file'}, {'id': 24, 'name': 'TTT', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '', 'data_list_id__agreement': 'http', 'req': 'GET', 'url': '', 'url_address': '', 'params': '[]', 'headers': "{'Content-Type': 'application/x-www-form-urlencoded'}", 'body': '', 'way_body': 'application_x_w'}, {'id': 26, 'name': '33', 'data_list_id__task_id__pro_name_model': 'aa', 'data_list_id__text': '', 'data_list_id__agreement': 'http', 'req': 'POST', 'url': 'http://www.baidu.com', 'url_address': '/?', 'params': "[{'keys': 't2', 'values': '2'}, {'keys': 't3', 'values': '3'}]", 'headers': "[{'keys': 'h1', 'values': 'h1'}, {'keys': 'h2', 'values': 'h2'}, {'keys': 'h3', 'values': 'h3'}]", 'body': "[{'key': '33', 'values': '33', 'file_text': 'text'}]", 'way_body': 'form_data'}];
    var fixed2 = function(val){
        return val.toFixed(2);
    }

    //加百分号
    var fixed2percentage = function(val){
        return fixed2(val)+'%';
    }
    //高亮
    var highliht = function(val){
        if(val > 0){
            return '<span style="color: #b00">' + fixed2(val) + '</span>';
        }else if(val < 0){
            return '<span style="color: #0b0">' + fixed2(val) + '</span>';
        }
        return fixed2(val);
    };
    //列
    var cols = [
                    { title:'任务名', name:'name' ,width:100, align:'right', sortable: true },
                    { title:'分类', name:'data_list_id__task_id__pro_name_model' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'描述', name:'data_list_id__text' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'协议', name:'data_list_id__agreement' ,width:100, align:'right', sortable: true },
                    { title:'请求类型', name:'req' ,width:100, align:'right', sortable: true },
                    { title:'服务地址', name:'url' ,width:100, align:'right', sortable: true },
                    { title:'地址', name:'url_address' ,width:100, align:'right', sortable: true },
                    { title:'URL参数', name:'params' ,width:100, align:'right', sortable: true },
                    { title:'请求头', name:'headers' ,width:100, align:'right', sortable: true },
                    { title:'请求体', name:'body' ,width:100, align:'right', sortable: true },
                    { title:'请求方式', name:'way_body' ,width:100, align:'right', sortable: true },
                    { title:'断言', name:'PREVCLOSINGPRICE' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'操作', name:'' ,width:150, align:'center', lockWidth:true, lockDisplay: true, renderer: function(val){
                        return '<button  class="btn btn-info">查看</button> <button  class="btn btn-danger">删除</button>'
                    }}
                ];

    //本地示例
    $('#table2-1').mmGrid({
        cols: cols,
        items: items
    });
    //AJAX示例
    $('#table2-2').mmGrid({
        cols: cols,
        url: 'stockQuote.json',
        method: 'get'
    });





    var cols3 = [
                    { title:'任务名', name:'name' ,width:100, align:'right', sortable: true },
                    { title:'分类', name:'data_list_id__task_id__pro_name_model' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'描述', name:'data_list_id__text' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'协议', name:'data_list_id__agreement' ,width:100, align:'right', sortable: true },
                    { title:'请求类型', name:'req' ,width:100, align:'right', sortable: true },
                    { title:'服务地址', name:'url' ,width:100, align:'right', sortable: true },
                    { title:'地址', name:'url_address' ,width:100, align:'right', sortable: true },
                    { title:'URL参数', name:'params' ,width:100, align:'right', sortable: true },
                    { title:'请求头', name:'headers' ,width:100, align:'right', sortable: true },
                    { title:'请求体', name:'body' ,width:100, align:'right', sortable: true },
                    { title:'请求方式', name:'way_body' ,width:100, align:'right', sortable: true },
                    { title:'断言', name:'PREVCLOSINGPRICE' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'操作', name:'' ,width:150, align:'center', lockWidth:true, lockDisplay: true, renderer: function(val){
                        return '<button  class="btn btn-info">查看</button> <button  class="btn btn-danger">删除</button>'
                    }}
                ];
    //客户端排序示例
    $('#table3-1').mmGrid({
        cols: cols3,
        items: items,
        sortName: 'DAYCHANGERATE',
        sortStatus: 'desc'
    });
    //服务器端排序示例
    $('#table3-2').mmGrid({
        cols: cols3,
        url: 'data/stockQuote.json',
        method: 'get',
        remoteSort:true ,
        sortName: 'SECUCODE',
        sortStatus: 'asc'
    });



    //锁定列宽
    var cols41 = [
        {title:'行情', name:'', width: 30, align: 'center',lockWidth:true, renderer: function(val,item,rowIndex){
            return '<div class="btnPrice"></div>';
        }},
        { title:'股票代码', name:'SECUCODE' ,width:80,lockWidth:true, align:'center' },
        { title:'股票名称', name:'SECUABBR' ,width:80,lockWidth:true, align:'center'},
        { title:'今收盘', name:'CLOSINGPRICE' ,width:60,lockWidth:true, align:'right', renderer: fixed2},
        { title:'涨跌幅', name:'DAYCHANGERATE' ,width:60,lockWidth:true, align:'right',renderer: highliht}
    ];
    $('#table4-1').mmGrid({
        height: 200,
        cols: cols41,
        items: items
    });

    //隐藏列
    var cols42 = [
        {title:'行情', name:'',width: 30, align: 'center', renderer: function(val,item,rowIndex){
            return '<div class="btnPrice"></div>';
        }},
        { title:'股票代码', name:'SECUCODE' ,width:80, align:'center', hidden: true },
        { title:'股票名称', name:'SECUABBR' ,width:80, align:'center'},
        { title:'今收盘', name:'CLOSINGPRICE' ,width:60, align:'right', renderer: fixed2},
        { title:'涨跌幅', name:'DAYCHANGERATE' ,width:60, align:'right',renderer: highliht}
    ];
    $('#table4-2').mmGrid({
        height: 200,
        cols: cols42,
        items: items
    });

    //锁定列显示状态
    var cols43 = [
        {title:'行情', name:'',width: 30, align: 'center',lockDisplay: true, renderer: function(val,item,rowIndex){
            return '<div class="btnPrice"></div>';
        }},
        { title:'股票代码', name:'SECUCODE' ,width:80, align:'center' },
        { title:'股票名称', name:'SECUABBR' ,width:80, lockDisplay: true,align:'center'},
        { title:'今收盘', name:'CLOSINGPRICE' ,width:60, align:'right',lockDisplay: true, renderer: fixed2},
        { title:'涨跌幅', name:'DAYCHANGERATE',width:60 , align:'right',renderer: highliht }
    ];
    $('#table4-3').mmGrid({
        height: 200,
        cols: cols43,
        items: items
    });

    //内容折行
    var cols5 = [
                    { title:'任务名', name:'name' ,width:100, align:'right', sortable: true },
                    { title:'分类', name:'data_list_id__task_id__pro_name_model' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'描述', name:'data_list_id__text' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'协议', name:'data_list_id__agreement' ,width:100, align:'right', sortable: true },
                    { title:'请求类型', name:'req' ,width:100, align:'right', sortable: true },
                    { title:'服务地址', name:'url' ,width:100, align:'right', sortable: true },
                    { title:'地址', name:'url_address' ,width:100, align:'right', sortable: true },
                    { title:'URL参数', name:'params' ,width:100, align:'right', sortable: true },
                    { title:'请求头', name:'headers' ,width:100, align:'right', sortable: true },
                    { title:'请求体', name:'body' ,width:100, align:'right', sortable: true },
                    { title:'请求方式', name:'way_body' ,width:100, align:'right', sortable: true },
                    { title:'断言', name:'PREVCLOSINGPRICE' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'操作', name:'' ,width:150, align:'center', lockWidth:true, lockDisplay: true, renderer: function(val){
                        return '<button  class="btn btn-info">查看</button> <button  class="btn btn-danger">删除</button>'
                    }}
                ];

    $('#table5-1').mmGrid({
        cols: cols5,
        items: items,
        nowrap: true
    });
    $('#table5-2').mmGrid({
        cols: cols5,
        items: items
    });

    //列宽自适应表格宽度
    var cols6 = [
        {title:'行情', name:'', width: 30, align: 'center',lockWidth:true, renderer: function(val,item,rowIndex){
            return '<div class="btnPrice"></div>';
        }},
        { title:'股票代码', name:'SECUCODE' ,width:80, align:'center' },
        { title:'股票名称', name:'SECUABBR' ,width:80, align:'center'},
        { title:'今收盘', name:'CLOSINGPRICE' ,width:60, align:'right', renderer: fixed2},
        { title:'涨跌幅', name:'DAYCHANGERATE' ,width:60, align:'right',renderer: highliht}
    ];
    $('#table6-1').mmGrid({
        cols: cols6,
        items: items,
        fullWidthRows: true
    });
    $('#table6-2').mmGrid({
        cols: cols6,
        items: items
    });


    //多选
    $('#table7-1').mmGrid({
        multiSelect: true,
        cols: cols,
        items: items
    });
    $('#table7-2').mmGrid({
        cols: cols,
        items: items
    });

    //选框列
    $('#table8-1').mmGrid({
        multiSelect: true,
        checkCol: true,
        cols: cols,
        items: items
    });
    $('#table8-2').mmGrid({
        checkCol: true,
        cols: cols,
        items: items
    });


    //索引列
    $('#table9-1').mmGrid({
        indexCol: true,
        indexColWidth: 25,
        cols: cols,
        items: items
    });
    $('#table9-2').mmGrid({
        checkCol: true,
        indexCol: true,
        indexColWidth: 25,
        cols: cols,
        items: items
    });


    //显示全部行
    $('#table10-1').mmGrid({
        height: 'auto',
        cols: cols,
        items: items
    });

    //分页
    $('#table11-1').mmGrid({
        indexCol: true,
        indexColWidth: 35,
        cols: cols,
        url: 'data/stockQuotePage.json',
        method: 'get',
        root: 'items',
        plugins : [
            $('#paginator11-1').mmPaginator()
        ]
    });

    //表头分组
    var groupCols = [
                    { title:'任务名', name:'name' ,width:100, align:'right', sortable: true },
                    { title:'分类', name:'data_list_id__task_id__pro_name_model' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'描述', name:'data_list_id__text' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'协议', name:'data_list_id__agreement' ,width:100, align:'right', sortable: true },
                    { title:'请求类型', name:'req' ,width:100, align:'right', sortable: true },
                    { title:'服务地址', name:'url' ,width:100, align:'right', sortable: true },
                    { title:'地址', name:'url_address' ,width:100, align:'right', sortable: true },
                    { title:'URL参数', name:'params' ,width:100, align:'right', sortable: true },
                    { title:'请求头', name:'headers' ,width:100, align:'right', sortable: true },
                    { title:'请求体', name:'body' ,width:100, align:'right', sortable: true },
                    { title:'请求方式', name:'way_body' ,width:100, align:'right', sortable: true },
                    { title:'断言', name:'PREVCLOSINGPRICE' ,width:100, align:'right', hidden: true, sortable: true },
                    { title:'操作', name:'' ,width:150, align:'center', lockWidth:true, lockDisplay: true, renderer: function(val){
                        return '<button  class="btn btn-info">查看</button> <button  class="btn btn-danger">删除</button>'
                    }}
                ];
    $('#table12-1').mmGrid({
        cols: groupCols,
        items: items
    });
});
