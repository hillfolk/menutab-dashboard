var baseUrl = 'http://dashobard.woodongpan.com/';

var username;
var password;
var loginstring;

var order_list = new Array();
var finish_list = new Array();
var cancle_list = new Array();
var staffcall_id_list = new Array();
var staffcall_data_list = new Array();


var status = ['취소','대기','처리','완료'];

var goAdmin = function() {
	location.href = baseUrl + "admin/";
}

var doLogin = function() {
	username = $('#username').val();
	password = $('#password').val();
	loginstring = "Basic " +  Base64.encode(username + ":" + password);

	$.ajax({
		type : 'get',
		async : true,
		url : baseUrl + 'orders/login/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			setLoginString();
			window.location = "orderboard.html";
		},
		error : function() {
		alert("로그인에 실패하였습니다.");
			window.location = "login.html";
		}
	});
};

var doReLogin = function() {
	getLoginString();
        if (typeof loginstring != 'undefined')
        window.location = "orderboard.html";
	
};

var doLogout = function() {
	resetLoginString();
	window.location = "login.html";
};


//FOR ACCOUNT
var doCheckPassword = function() {
	$.ajax({
		type : 'post',
		url : baseUrl + 'api/user/checkpassword/',
		data : {password:$("#oldpassword").val()},
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			alert(data.status);
			console.log(data);
		},
		error : function(msg) {
			alert("Fail to get data!");
		}
	});
};
var doSetPassword = function() {
	$.ajax({
		type : 'post',
		url : baseUrl + 'api/user/setpassword/',
		data : {password:$("#newpassword").val()},
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			alert("OK");
			loginstring = "Basic " +
						  Base64.encode(username + ":" + $("#newpassword").val());
			setLoginString();
			$("#oldpassword").val($("#newpassword").val());
			$("#newpassword").val("");
		},
		error : function(msg) {
			alert(msg.responseText);
		}
	});
};




// UTILITY METHODS
function setCookie(name, value, day) {
	var expire = new Date();
	expire.setDate(expire.getDate() + day);
	cookies = name + '=' + escape(value) + '; path=/ ';
	if (typeof day != 'undefined')
		cookies += ';expires=' + expire.toGMTString() + ';';
	document.cookie = cookies;
}

function getCookie(name) {
	name = name + '=';
	var cookieData = document.cookie;
	var start = cookieData.indexOf(name);

	var value = '';
	if (start != -1) {
		start += name.length;
		var end = cookieData.indexOf(';', start);
		if (end == -1)
			end = cookieData.length;
		value = cookieData.substring(start, end);
	}
	return unescape(value);
}

function getLoginString() {
	loginstring = getCookie("loginstring");
	username = getCookie("username");
	password = getCookie("password");
}
function setLoginString() {
	setCookie("loginstring", loginstring, 1);
	setCookie("username", username, 1);
	setCookie("password",password,1);
}
function resetLoginString() {
	setCookie("loginstring", "", "-1");
	setCookie("username", "", "-1");
	setCookie("password","","-1");
}

function checkLoginString() {
	if (loginstring == "") {
		history.back();
	}
}
