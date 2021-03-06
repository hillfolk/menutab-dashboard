
var status = ['취소','대기','처리','완료'];

var order_list = [];

var order = {};
	var pageID = "history_page";
var historyGrid = new AXGrid();


var setOrderConfig = function (){
historyGrid.setConfig({
				targetID : "history_grid",
				height:"auto",
				colHeadAlign: "center", // 헤드의 기본 정렬 값
				colGroup : [
					{key:"order_time", label:"주문시간", width:"120", align:"center",formatter:"datetime"},
					{key:"status_set_time", label:"처리시간", width:"120", align:"center",formatter:"datetime"},
					{key:"row", label:"층", width:"50", align:"center"},
					{key:"table_code", label:"테이블", width:"100", align:"center"},
					{key:"menu_name", label:"메뉴", width:"*"},
					{key:"menu_price", label:"가격", width:"100", align:"right", formatter:"money"},
					{key:"count", label:"수량", width:"50", align:"center"},
					{key:"cost", label:"금액", width:"80", align:"right", formatter:function(){
						return (this.item.menu_price.number() * this.item.count.number()).money();
						}},
				],
				body : {
					onclick: function(){
						// 상태 변경 모
					},
					/* ondblclick 선언하면 onclick 이벤트가 0.25 초 지연 발생 됩니다. 주의 하시기 바람니다. */
					ondblclick: function(){

					},
					addClass: function(){	
						// red, green, blue, yellow, white, gray
						/*
						if(this.index % 2 == 0){
							return "green";
						}else{
							return "red";
						}
						*/
					}
				},
				page: {
                paging: false
            }
			});

}







var doReload = function() {
	console.log(order_list.length);     

	doGetOrderBoard(1);
} 

var doUpdate = function() {
	console.log(order_list.length);     

	doGetOrderBoard(0);
}

var doClear = function() {
		$('#historyarea').html('')
}





var doLogout = function() {
	resetLoginString();
	window.location = "login.html";
};



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
		},
	});
}



var doCancel = function() {
	location.reload();
};
//
var doSearchOrder = function(search_value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'orderhistory/',beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},data:search_value
		,
		success : function(data) {
	 		historyGrid.setList(data.history_list);

	},error : function(msg) {
			alert("Fail to get data!");
		}, });

}

//
var doCancleOrder = function(search_value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'orderhistory/',beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},data:search_value
		,
		success : function(data) {
	 	historyGrid.setList(data.history_list);

	},error : function(msg) {
			alert("Fail to get data!");
		}, });

}

var doChSeldate = function fnChSeldate(){
	var term = $('#seldate').val();
  	var date = new Date();
  	var today = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
	var strdate;
	if(term == '1'){
		$('#AXInputDateST').val(today);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '7'){
		date.setDate(date.getDate()-7);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '30'){
		date.setDate(date.getDate()-30);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '90'){
		date.setDate(date.getDate()-90);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '180'){
		date.setDate(date.getDate()-180);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}else if(term == 'sel'){
		$('#AXInputDateST').val('');
		$('#AXInputDateED').val('');					
	}				
}

var doSearchHistory = function fnSearchHistory(){
	var term = $('#seldate').val();
  	var date = new Date();
  	var today = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
	var strdate;
	var dateset = {ST_objID:"AXInputDateST",ED_objID:"AXInputDateED",ST_value:today,ED_value:today}
	if(term == '1'){
		doSearchOrder(Object.toJSON(dateset));
		$('#AXInputDateST').val(today);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '7'){
		date.setDate(date.getDate()-7);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		dateset.ST_value = strdate;
		doSearchOrder(Object.toJSON(dateset));
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '30'){
		date.setDate(date.getDate()-30);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		dateset.ST_value = strdate;
		doSearchOrder(Object.toJSON(dateset));
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '90'){
		date.setDate(date.getDate()-90);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		dateset.ST_value = strdate;
		doSearchOrder(Object.toJSON(dateset));
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);					
	}
	else if(term == '180'){
		date.setDate(date.getDate()-180);
		strdate = date.getFullYear()+'/'+((date.getMonth()+1)<10 ? '0'+(date.getMonth()+1):(date.getMonth()+1))+'/'+(date.getDate()<10 ? '0'+date.getDate():date.getDate());
		dateset.ST_value = strdate;
		doSearchOrder(Object.toJSON(dateset));
		$('#AXInputDateST').val(strdate);
		$('#AXInputDateED').val(today);
	}else if(term == 'sel'){
		dateset.ST_value = $('#AXInputDateST').val();
		dateset.ED_value = $('#AXInputDateED').val();
		doSearchOrder(Object.toJSON(dateset));					
	}
}