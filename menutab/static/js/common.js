var baseUrl = 'http://127.0.0.1:8000/';

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

