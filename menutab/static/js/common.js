var baseUrl = 'http://127.0.0.1:8000/';

var username;
var password;
var loginstring;

var order = {};

var staffcall = {};

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
			window.location = "dashboard.html";
		},
		error : function() {
			window.location = "login.html";
			//alert("Fail to get data!"+username +":"+password);
		},
	});
}
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
		},
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
		},
	});
};
var doGetName = function() {
	$.ajax({
		type : 'get',
		url : baseUrl + 'api/user/name/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			$("#getname").val(data.name);
		},
		error : function(msg) {
			alert("Fail to get data!");
		},
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
}
function setLoginString() {
	setCookie("loginstring", loginstring, 1);
	setCookie("username", username, 1);
}
function resetLoginString() {
	setCookie("loginstring", "", "-1");
	setCookie("username", "", "-1");
}

function checkLoginString() {
	if (loginstring == "") {
		history.back();
	}
}
