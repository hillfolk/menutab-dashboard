
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
					{key:"id", label:"번호", width:"50", align:"right"}, 
					{key:"menu_name", label:"메뉴", width:"100"},
					{key:"table_code", label:"테이블", width:"100", align:"center"},
					{key:"order_time", label:"주문시간", width:"100", align:"center",formatter:"datetime"},
					{key:"row", label:"층", width:"100", align:"center"},
					{key:"status", label:"상태", width:"100", align:"center"}
					// {key:"", label:"가격", width:"100", align:"right", formatter:"money"},
					// {key:"amount", label:"수량", width:"80", align:"right", formatter:"money"},
					// {key:"cost", label:"금액", width:"100", align:"right", formatter:function(){
					// 	return (this.item.price.number() * this.item.amount.number()).money();
					// }},
					// {key:"desc", label:"비고", width:"*"}
				],
				body : {
					onclick: function(){
						// toast.push(Object.toJSON({index:this.index, r:this.r, c:this.c, item:this.item}));
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

var doGetOrderBoard = function(value) {
	$.ajax({
		type : 'get',
		url : baseUrl + 'orders/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			if (value == 1) {

				order_list = [];
				doClear();
			};
			
			for (var i in data.order_list){
				if (order_list.indexOf(data.order_list[i].id)  == -1  ) {
					console.log(order_list.indexOf(data.order_list[i]));
				order_list.push(data.order_list[i].id);	
				console.log(data.order_list[i])
				doAppend(data.order_list[i]);				
			};
			
				
				

			 
				
			};
			// order_list = data.order_list;

			$("#total").html(data.total_count);
			$("#username").html(username);
		},
		error : function() {
			location.href = "login.html";
		},
	});
}

var doAppend = function(data) {
						// <div class='content'>
						// <span class = 'order_date'></span>
						// <span class = 'process date'></span>
						// <span class = 'table_code'></span>
						// <span class = 'menu_name'></span>
						// <span class = 'menu_price'></span>
						// <span class = 'order_count'></span>
						// <span class = 'order_price'></span>
						// <span class = 'order_status'></span>
					
	node = $('#orderhistoryTemplate').clone();
	$('.order_id',node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('.order_date', node).append(data.order_time);
	$('.process_date', node).append(data.order_time);
	$('.table_code', node).append(data.row+data.table_code );
	$('.menu_name', node).append( data.menu_name);
	$('.order_count', node).append( data.count);

	$('.menu_price', node).append(data.menu_price);
	$('.order_price', node).append(data.menu_price * data.count);
	$('.menu_price', node).append(status[data.status]);
	

	
	node.show();
	
		$('#historyarea').append(node);	
		
	

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
			alert("Fail to get data!");
		},
	});
}



var doCancel = function() {
	location.reload();
};
//
var doSearchOrder = function(starttime,endtime) {
	$.ajax({
		type : 'get',
		url : baseUrl + 'orders/',beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},success : function(data) {
	 console.log(data)
		orderhistoryGrid.setList(data.order_list);

	},error : function(msg) {
			alert("Fail to get data!");
		}, });

}
