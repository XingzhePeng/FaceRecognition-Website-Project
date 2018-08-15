function showEmailForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeOut('fast');
        $('.passwordBox').fadeOut('fast');
        $('.messageBox').fadeOut('fast');
        $('.emailBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeOut('fast');
        });
        $('.modal-title').html('Enter your email address');
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function showPasswordForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeOut('fast');
        $('.emailBox').fadeOut('fast');
        $('.messageBox').fadeOut('fast');
        $('.passwordBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeOut('fast');
        });
        $('.modal-title').html('Create a new password');
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function showMessageForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeOut('fast');
        $('.emailBox').fadeOut('fast');
        $('.passwordBox').fadeOut('fast');
        $('.messageBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeOut('fast');
        });
        $('.modal-title').html('notice');
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.emailBox').fadeOut('fast');
        $('.passwordBox').fadeOut('fast');
        $('.messageBox').fadeOut('fast');
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Sign up');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
}

function showLoginForm(){
    $('.registerBox').fadeOut('fast',function(){
        $('.emailBox').fadeOut('fast');
        $('.passwordBox').fadeOut('fast');
        $('.messageBox').fadeOut('fast');
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');
        });

        $('.modal-title').html('Sign in');
    });
     $('.error').removeClass('alert alert-danger').html('');
}

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
        $('#loginModal').modal('show');
    }, 500);
}

function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 500);
}

function openEmailModal(){
    showEmailForm();
    setTimeout(function(){
        $('#loginModal').modal('show');
    }, 500);
}

function openPasswordModal(){
    showPasswordForm();
    setTimeout(function(){
        $('#loginModal').modal('show');
    }, 500);
}

function openMessageModal(){
    showMessageForm();
    setTimeout(function(){
        $('#loginModal').modal('show');
    }, 500);
}

function loginCheck(){
    var username=$('#username').val();
    if (username==null || username==""){
        shakeModal("Please enter a username");
        return false;
    }
    var password=$('#password').val();
    if (password==null || password==""){
        shakeModal("Please enter a password");
        return false;
    }
    return true;
}

function sendemail_a(email) {
    $.ajax({
                url:"/sendemail_a/",
                type:"post",
                data:{
                    email:email,
                },
                success:function(data){
                    if(data==1){
                        showMessageForm();
                        $('.email_message').html('We have sent an activation email to you, please check your mailbox.');
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
    json_a=null;
}

function loginAjax(){
    if(loginCheck()){
        var username=$('#username').val();
        var password=$('#password').val();
        $.ajax({
                url:"/signin/",
                type:"post",
                data:{
                    username:username,
                    password:password,
                },
                success:function(data){
                    if(data.code_si==1){
                        shakeModal("User does not exit");
                        return;
                    }
                    if(data.code_si==2){
                        shakeModal("Incorrect password");
                        return;
                    }
                    if(data.code_si==3){
                        showMessageForm();
                        $('.email_message').html('Account has not been activated yet.');
                        var delay = setTimeout(function () {
                            sendemail_a(data.email);
                        },900);
                        return;
                    }
                    if(data.code_si==4){
                        window.location.replace("/main/");
                        return;
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
    }
}

function isEmail(str){
   var reg = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
   if (!reg.test(str))
        return false;
    return true;
}

function isPassword(str) {
    var reg=/^(\w){6,20}$/;
    if (!reg.test(str))
        return false;
    return true;
}

function signupCheck(){
    var username=$('#username1').val();
    if (username==null || username==""){
        shakeModal("Please enter a username");
        return false;
    }
    var email=$('#email1').val();
    if (!isEmail(email)){
        shakeModal("Please enter a valid email address");
        return false;
    }
    var password=$('#password1').val();
    var confirm_password=$('#confirm_password1').val();
    if(!isPassword(password)){
        shakeModal("The password should be 6 digits and can be numbers, letters or underscores");
        return false;
    }
    if(password!=confirm_password){
        shakeModal("Two passwords should be consistent");
        return false;
    }
    return true;
}

function signupAjax() {
    if(signupCheck()){
        var username=$('#username1').val();
        var email=$('#email1').val();
        var password=$('#password1').val();
        $.ajax({
                url:"/signup/",
                type:"post",
                data:{
                    username:username,
                    email:email,
                    password:password,
                },
                success:function(data){
                    if(data==1){
                        shakeModal("The username is not available");
                        return;
                    }
                    if(data==2){
                        shakeModal("The email is not available");
                        return;
                    }
                    if(data==3){
                        showMessageForm();
                        $('.email_message').html('We have sent a activation email to you, please check your mailbox.');
                        return;
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
    }
}

function shakeModal(error){
    $('#loginModal .modal-dialog').addClass('shake');
             $('.error').addClass('alert alert-danger').html(error);
             $('input[type="password"]').val('');
             setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 ); 
}

function activate(json_a) {
    if (json_a.code_a == 1) {
        openMessageModal();
        $('.email_message').html('Account has been activated before, directly <a href="javascript:showLoginForm()">signin</a>.');
        json_a=null;
        return;
    }
    if (json_a.code_a == 2) {
        openMessageModal();
        $('.email_message').html('Account activated successfully, now <a href="javascript:showLoginForm()">signin</a>.');
        json_a=null;
        return;
    }
    if (json_a.code_a == 3) {
        openMessageModal();
        $('.email_message').html('Activation timed out, <a href="javascript:sendemail_a(json_a.email)">resend activation email</a>?');
        return;
    }
}

//重置密码输完邮件后点击next
function sendemail_r() {
    var email=$('#email2').val();
    if (!isEmail(email)){
        shakeModal("Please enter a valid email address");
        return;
    }
    $.ajax({
                url:"/reset/",
                type:"post",
                data:{
                    email:email,
                },
                success:function(data){
                    if(data==1){
                        showMessageForm();
                        $('.email_message').html('The email is not signed up yet, would you like to <a href="javascript:showRegisterForm()">sign up</a> now?');
                        return;
                    }
                    if(data==2){
                        showMessageForm();
                        $('.email_message').html('We have sent a verification email to you, please check your mailbox.');
                        return;
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
}

function sendemail_r_p(email) {
    $.ajax({
                url:"/reset/",
                type:"post",
                data:{
                    email:email,
                },
                success:function(data){
                    if(data==1){
                        showMessageForm();
                        $('.email_message').html('The email is not signed up yet, would you like to <a href="javascript:showRegisterForm()">sign up</a> now?');
                        return;
                    }
                    if(data==2){
                        showMessageForm();
                        $('.email_message').html('We have sent a verification email to you, please check your mailbox.');
                        return;
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
}

function reset(json_r) {
    if (json_r.code_r == 1) {
        openPasswordModal();
    }
    if (json_r.code_r == 2) {
        openMessageModal();
        $('.email_message').html('Verification timed out, <a href="javascript:sendemail_r_p(json_r.email)">resend email</a>?');
    }
}

function password_rCheck() {
    var password=$('#password2').val();
    var confirm_password=$('#confirm_password2').val();
    if(!isPassword(password)){
        shakeModal("The password should be 6-20 bits long, including letters, numbers or underscores");
        return false;
    }
    if(password!=confirm_password){
        shakeModal("Two passwords should be consistent");
        return false;
    }
    return true;
}

function password_r(json_r) {
    if(password_rCheck()){
        var password=$('#password2').val();
        $.ajax({
                url:"/reset_done/",
                type:"post",
                data:{
                    username:json_r.username,
                    password:password,
                },
                success:function(data){
                    if(data==1){
                        showMessageForm();
                        $('.email_message').html('Password reset successfully, now <a href="javascript:showLoginForm()">signin</a>.');
                        json_r=null;
                        return;
                    }
                },
                error:function(e){
                    alert("Error!!");
                    window.clearInterval(timer);
                }
            });
    }
}

