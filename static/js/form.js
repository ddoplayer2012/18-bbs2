/**
 */


GROUP = [
    {"id": 1, "value": "IT"},
    {"id": 2, "value": "PHP"},
    {"id": 3, "value": "ToC"}
];

STATUS = [
    {"id": 1, "value": "运行"},
    {"id": 2, "value": "关机"}
];
//进入行编辑
function EnterLineEdit(arg) {
    //arg是tr      ,用于ajax传值的表单元素 $('#data_show').children().children().children()
    //                                                       tr          td        input/select
    arg.children().children().each(function(){
        //判断元素是否可编辑
        if ($(this).parent().attr("writeable") == "true"){
            if ($(this).attr("used") == "select"){
                //获取select选项
                    $(this).removeAttr("disabled");
            }
            else if($(this).attr("used") == "text"){
                    count+=1;
                    $(this).removeAttr("readonly");
            }
            else {

            }
        }
    });
}

var count = 0;
$('#submit_data').on('click',function () {
      if  (!$("#edit").hasClass("writing")){
             select_TO_input();
            count+=1;
            commint_data();
            console.log(count);
      }else{
          alert('需要退出编辑模式才可更新数据到数据库！')
      }
})




//退出行编辑,arg指的是这个tr
function ExitLineEdit(arg) {
    //arg是datashow
    arg.children().children().addClass("updated");
    arg.children().children().each(function () {
        if ($(this).parent().attr("writeable") == "true") {
            if ($(this).attr("used") == "select") {
                //获取select选项
                  $(this).attr("disabled",'true');
            }
            else if($(this).attr("used") == "text"){
                  $(this).attr("readonly",'true');

            }
            else {

            }

        }

    });

}
//单选
function SingleSelect(arg) {
    if ($("#edit").hasClass("writing")) {
        if (arg.prop("checked")) {
            EnterLineEdit(arg.parent().parent()) //传的data_show
        } else {
            ExitLineEdit(arg.parent().parent())
        }
    }
}
//绑定单选
    $("input:checkbox").on('click',function(){
        SingleSelect($(this))
    })

//全选
    $("#check-all").on('click',function(){
      $("input:checkbox").each(function () {
            if ($(this).prop("checked") == false) {
                $(this).prop("checked",true);
                SingleSelect($(this))
            }
        })
    })

//反选
    $("#select-invert").on('click',function(){
        $("input:checkbox").each(function () {
            if ($(this).prop("checked")) {
                $(this).prop("checked",false);
                SingleSelect($(this))
            } else {
                $(this).prop("checked",true);
                SingleSelect($(this));
            }
        })
    })

//取消
    $("#cancel").on('click',function(){
        $("input:checkbox").each(function() {
            if ($(this).prop("checked")) {
                $(this).prop("checked", false);
                SingleSelect($(this))
            }
        })
    })


//编辑模式
    $("#edit").on('click',function(){
        if ($(this).hasClass("writing")) {
            $(this).removeClass("writing");
            $(this).text("进入编辑模式");
            select_TO_input();
            $("input:checkbox").each(function () {
                if ($(this).prop("checked")) {
                    $(this).prop("checked",false);
                    ExitLineEdit($('#data_show').children())
                }
            })
        } else {
            $(this).addClass("writing");
            $(this).text("退出编辑模式");
            $("input:checkbox").each(function () {
                if ($(this).prop("checked")) {
                    EnterLineEdit($('#data_show').children())
                }
            })
        }
    })


function  commint_data() {
    /*
    * 由于使用模板生成相同的name,无法serialize,只能筛选出tr .
    * 问题1：select无法被form.serialize()选中，所以借用隐藏input来传值
    * */
    $.ajax({
        url: "/host_ajax",
        type: 'POST',
        contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        //data: {'hostname': $('#host').val(), 'ip': $('#ip').val(), 'port': $('#port').val(), 'b_id': $('#sel').val()},
        data: $("#show_host_list").serialize(),
        success: function (data) {
            var obj = JSON.parse(data);
            if (obj.status) {
                location.reload();
            } else {
                $('#erro_msg').text(obj.error);
            }
        }
    })
}



function select_TO_input(){
    /*隐藏input得到值 ,由于select被禁用无法取值，需要做判断
    * */
     $('select').each(function(){
       if (typeof($(this).attr("disabled"))=="undefined"){
           $(this).parent().find('input[used=text]').attr("value", $(this).find("option:selected").text());
           $(this).parent().find('input[used=text]').attr('name',$(this).attr('name'));
       }else{
           $(this).parent().find('input[used=text]').attr("value", $(this).val());
           $(this).parent().find('input[used=text]').attr('name',$(this).attr('name'));
       }

     })
}


    $('#adddata').on('click',function(){
    //打开模态对话框
        $('.shade,.add-modal').removeClass('hide');
              });
   $('#quit').on('click',function(){
        $('.shade,.add-modal').addClass('hide');
              });


$('#ajax_submit').on('click',function () {
    /*   增加一行主机信息
    * */
     $.ajax({
        url: "/add_host_ajax",
        type: 'POST',
        contentType: "application/x-www-form-urlencoded; charset=UTF-8",
        //data: {'hostname': $('#host').val(), 'ip': $('#ip').val(), 'port': $('#port').val(), 'b_id': $('#sel').val()},
        data: $("#add_form").serialize(),
        success: function (data) {
            var obj = JSON.parse(data);
            if (obj.status) {
                location.reload();
            } else {
                $('#erro_msg2').text(obj.error);
            }
        }
    })
})

$('#delete_data').on('click',function () {
    //删除选中的所有主机信息
       var myArray = [];
    $("input:checkbox").each(function () {

        if($(this).prop("checked")){
           primary_key_val= ($(this).parent().siblings().find('input[id=id]').val());
           myArray.push(primary_key_val) ;
        }

    })

     $.ajax({
            url: "/del_host_ajax",
            type: 'POST',
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            data: {myArray : myArray},
            success: function (data) {
            var obj = JSON.parse(data);
            if (obj.status) {
                location.reload();
            } else {
                $('#error_msg').text(obj.error);
            }
        }
    })
})