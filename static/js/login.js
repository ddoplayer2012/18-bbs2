
function  show_login_frm() {
    //login显示注册的模态对话框
    $('.login_reg_frm,.shelter').removeClass('hide');
}

function show_reg_frm() {
    //login显示注册的模态对话框
    show_login_frm();
}

function check_exist(ele) {
    /* ajax检查数据是否已被注册使用 */
    var t = ele.getAttribute("name");
    var v = ele.value;
    v = $.trim(v);
    if(v.length>0){
        $.ajax({
            type: 'POST',
            url: "/check_exist",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            data: {"check_type": t, "check_value": v},
            dataType: "json",
            success: function (response) {
                // console.log(response);
                var check_result = "";
                if(response.status=='ok'){
                    // 没有重复
                    check_result = "√";
                }else{
                    check_result = "已存在";
                    ele.setAttribute("duplicate", "duplicate");
                }
                $(ele).parent().parent().find('td:last-child').text(check_result); //在tips标签处生成提示
            }
        });
    }
}


function confirmpass() {
    if ( $('#id_password').val() != "" && $('#id_password2').val() !=""){
            if ($('#id_password').val() != $('#id_password2').val()) {
                $('#id_password2').parent().parent().find('td:last-child').text("两次密码不一致");
            } else {
                $('#id_password').parent().parent().find('td:last-child').text("√");
                $('#id_password2').parent().parent().find('td:last-child').text("√");
            }
    }
}


function register(ele) {
    // 提交时数据检查
    var check_pass = true;
    var check_list = {
        'user_name': '用户名',
        'email': '邮箱',
        'password': '密码',
        'password2': '确认密码'
   //     'verify_code': '验证码'
    };
    for(var key in check_list){
        var val = $.trim($('.reg_frm #id_' + key).val());
        if(val.length==0){
            // 如果要检查的input值为空，提醒用户
            check_pass = false;
            $(".reg_frm #id_" + key).parent().parent().find('td:last-child').text("不能为空");
        }
    }
    if(!check_pass){
        return false;
    }

    // 通过检查后
    var user_name = $.trim($('.reg_frm #id_user_name').val());
    var email = $.trim($('.reg_frm #id_email').val());
    var password = $.trim($('.reg_frm #id_password').val());
    var password2 = $.trim($('.reg_frm #id_password2').val());
 //   var verify_code = $.trim($('.reg_frm #verify_code').val());

    // 提交前，先将按钮置为不可点击
    $("div.reg_shelter").removeClass("hide");
    var data = $('#register_frm').serialize();
    console.log(data);
    $.ajax({
        type: 'POST',
        url: "/register/",
        data: data,
        dataType: "json",
        success: function (response) {
            console.log(response);
            if(response.hasOwnProperty("status")){
                if(response.status=='ok'){
                    //console.log("注册成功");
                    $("div.register_result").text("注册成功");
                    setTimeout(function () {
                        $("div.login_reg_frm").addClass("hide");
                        $("div.shelter").addClass("hide");
                    }, 2000);
                }else{
                    $("div.reg_shelter").addClass("hide");
                    $("div.register_result").text(response.msg);
                }
            }else{
                var ul = document.createElement('ul');
                for(var key in response){
                    var li = document.createElement('li');
                    li.innerText = response[key][0].message;
                    ul.appendChild(li);
                }
                $("div.register_result").html(ul.outerHTML);
                $("div.reg_shelter").addClass("hide");
            }
        },
        error: function (xhr) {
            $("div.reg_shelter").addClass("hide");
        }
    });
   // reload_verify_code();   // 无论结果如何，都刷新验证码
}