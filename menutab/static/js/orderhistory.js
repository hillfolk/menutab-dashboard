
var status = ['취소','대기','처리','완료'];

var order_list = [];

var order = {};
	var pageID = "orderhistory_page";
var orderhistoryGrid = new AXGrid();


var setOrderConfig = function (){
orderhistoryGrid.setConfig({
				targetID : "orderhistory_grid",
				height:"auto",
				colHeadAlign: "center", // 헤드의 기본 정렬 값
				colGroup : [
					{key:"order_time", label:"주문시간", width:"120", align:"center",formatter:"datetime"},
					{key:"status_set_time", label:"처리시간", width:"120", align:"center",formatter:"datetime"},
					{key:"row", label:"층", width:"50", align:"center"},
					{key:"table_code", label:"테이블", width:"100", align:"center"},
					{key:"menu_name", label:"메뉴", width:"100"},
					{key:"menu_price", label:"가격", width:"100", align:"right", formatter:"money"},
					{key:"count", label:"수량", width:"50", align:"center"},
					{key:"cost", label:"금액", width:"80", align:"right", formatter:function(){
						return (this.item.menu_price.number() * this.item.count.number()).money();
						}},
					{key:"customer_key", label:"고객번호", width:"*", align:"right", formatter:"string"},
					// 	return (this.item.price.number() * this.item.amount.number()).money();
					// {key:"amount", label:"수량", width:"80", align:"right", formatter:"money"},
					// {key:"cost", label:"금액", width:"100", align:"right", formatter:function(){
					// 	return (this.item.price.number() * this.item.amount.number()).money();
					// }},
					// {key:"desc", label:"비고", width:"*"}
				],
				body : {
					onclick: function(){
						// 상태 변경 모
					},
					/* ondblclick 선언하면 onclick 이벤트가 0.25 초 지연 발생 됩니다. 주의 하시기 바람니다. */
					ondblclick: function(){
						// toast.push("더블클릭");
						//toast.push(Object.toJSON({index:this.index, r:this.r, c:this.c, item:this.item}));
						//alert(this.list);
						//alert(this.page);
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
				}
			});

}







var doReload = function() {
	console.log(order_list.length);     


	//doClear();
	doGetOrderBoard(1);
} 

var doUpdate = function() {
	console.log(order_list.length);     


	//doClear();
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
			// alert("Fail to get data!");
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
		url : baseUrl + 'getsearchboard/',beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},data:search_value
		,
		success : function(data) {
	 	console.log(search_value)
		orderhistoryGrid.setList(data.order_list);

	},error : function(msg) {
			alert("Fail to get data!");
		}, });

}

//
var doCancleOrder = function(search_value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'getcancleboard/',beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},data:search_value
		,
		success : function(data) {
	 	console.log(search_value)
		orderhistoryGrid.setList(data.order_list);

	},error : function(msg) {
			alert("Fail to get data!");
		}, });

}

