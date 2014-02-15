var baseUrl = 'http://127.0.0.1:8000/';

var username;
var password;
var loginstring;
var status = ['취소','대기','처리','완'];

var doJoin = function() {
	username = $("#username").val();
	name = $("#name").val();
	password = $("#password").val();
	$.ajax({
		type : 'post',
		url : baseUrl + 'api/user/create/',
		data : {
			username : username,
			name : name,
			password : password
		},
		success : function() {
			alert("OK");
			location.href = "login.html";
		},
		error : function(msg) {
			alert("Error!");
		},
	});
}

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



var doGetOrderBoard = function() {
	$.ajax({
		type : 'get',
		url : baseUrl + 'orders/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			for (var i in data.order_list) {
				doAppend(data.order_list[i]);
			}
			$("#total").html(data.total_count);
			$("#username").html(username);
		},
		error : function() {
			location.href = "login.html";
		},
	});
}

var doAppend = function(data) {
	
	node = $('#orderTemplate').clone();
	
	$('.name', node).append(data.row+'층'+data.table_code );
	$('.content', node).append(data.menu_name + data.count+'');
	$('.date', node).append(data.order_time);
	$('.cookstart', node).prepend(status[data.status]+" 상태입니다.");
	$('.order_id',node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('#LeftBtn', node).attr("value",data.id);
	$('#RightBtn', node).attr("value",data.id);
	
	node.show();
	if (data.status === 1) {
		$('#watchingarea').append(node);	
	};
		if (data.status === 2) {
		$('#processingarea').append(node);	
	};	

	if (data.status === 3) {
		$('#donearea').append(node);	
	};	
	


}

var doReload = function() {
	doClear();
	doGetOrderBoard();
}
var doClear = function() {
	$('#watchingarea').html('')
	$('#processingarea').html('')
	$('#donearea').html('')

}
var doWClear = function() {
	$('#watchingarea').html('')

}






var doLogout = function() {
	resetLoginString();
	window.location = "login.html";
};
var doRightBtn = function() {
	var id = $(this).val() ;
	
	var status = $("#order_"+id).val();
	var status = status + 1;
	$.ajax({
		type : 'post',
		url : baseUrl + 'orders/' + id + "/update/",
		data :{
		status:status

		},
		success : function() {
			doReload();
		},
		error : function(msg) {
			alert("Fail to set data!");
		},
	});
}

var doLeftBtn = function() {
	var id = $(this).val() ;
	var status = $("#order_"+id).val();
	var status = status - 1;
	$.ajax({
		type : 'post',
		url : baseUrl + 'orders/' + id + "/update/",
		data : {
			status : status
		},
		success : function() {
			doReload();
		},
		error : function(msg) {
			
		},
	});
}


var doGetOrderInfo = function() {
	var order_id= $("div", this).html() ;
	$.ajax({
		type : 'get',
		url : baseUrl + 'api/profile/' + order_id + "/",
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			$("#modalid").html(data.username);
			$("#modalnickname").html(data.nickname);
			$("#modalcountry").html(data.country);
			$("#modalcomment").html(data.comment);
			$("#modalurl").html(data.url);
			$("#myModal").modal("show");
			
		},
		error : function(msg) {
			alert("Fail to get data!");
		},
	});
}



var doCancel = function() {
	location.reload();
};
//END PROFILE



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
