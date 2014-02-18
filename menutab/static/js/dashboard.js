

var wait_list = [];
var process_list = [];
var done_list = [];
var staffcall_id_list = [];
var staffcall_data_list = [];





// var doGetOrderBoard = function(value) {
// 	$.ajax({
// 		type : 'get',
// 		url : baseUrl + 'orders/',
// 		beforeSend : function(req) {
// 			req.setRequestHeader('Authorization', loginstring);
// 		},
// 		success : function(data) {

// 			for (var i in data.order_list){
// 				if (order_list.indexOf(data.order_list[i].id)  == -1 ) {
// 					if(order_list.) 
					
// 				order_list.push(data.order_list[i].id);	
// 				console.log(data.order_list[i])
// 				doAppend(data.order_list[i]);				
// 			};
	
// 			};
// 			// $("#total").html(data.total_count);
// 			// $("#username").html(username);
// 		},
// 		error : function() {
// 			location.href = "login.html";
// 		},
// 	});
// }

var doStaffcall = function(staffcall_idx) {
	console.log(staffcall_idx);
	staffcall_data_list[staffcall_idx].status = staffcall_data_list[staffcall_idx].status +1;
	

	$.ajax({
		type : 'post',
		url : baseUrl + 'staffcall/' + staffcall_data_list[staffcall_idx].id + "/update/",
		data :{
		status:staffcall_data_list[staffcall_idx].status

		},
		success : function() {
			// doReload();
		},
		error : function(msg) {
			// alert("Fail to set data!");
		},
	});
}


var doGetStaffcall = function() {
	$.ajax({
		type : 'get',
		url : baseUrl + 'staffcall/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			console.log(data);
			for (var i in data.staffcall_list){
				if (staffcall_id_list.indexOf(data.staffcall_list[i])  == -1 && i >= 0 ) {
						console.log('-->'+i);
				staffcall_id_list.push(data.staffcall_list[i].id);
				staffcall_data_list.push(data.staffcall_list[i]);
				toast.push({body:'직원호출:'+data.staffcall_list[i].table_code +'테이블 '+ data.staffcall_list[i].staffcall_desc +' '+ data.staffcall_list[i].count +  '개', type:'Caution'
					 ,onClick:doStaffcall(i) 
						});	
					};
		
			};


		
			// order_list = data.order_list;

		},
		error : function() {
			location.href = "login.html";
		},
	});
}

var doGetDasboard = function(value) {
	$.ajax({
		type : 'get',
		url : baseUrl + 'getdashboard/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
	
			for (var i in data.staffcall_list){
				if (staffcall_id_list.indexOf(data.staffcall_list[i].id)  == -1 && i >= 0 ) {
				staffcall_id_list.push(data.staffcall_list[i].id);
				staffcall_data_list.push(data.staffcall_list[i]);
				toast.push({body:'직원호출:'+data.staffcall_list[i].table_code +'테이블 '+ data.staffcall_list[i].staffcall_desc +' '+ data.staffcall_list[i].count +  '개', type:'Caution'
					 ,onClick:doStaffcall(i) 
				});	
			};
		
			};
			if (value == 1) {
				wait_list.clear();
				process_list.clear();
				done_list.clear();
			};
			
			for (var i in data.wait_list){
				var w_idx  = wait_list.indexOf(data.wait_list[i].id);
				if (w_idx == -1  ) {
				wait_list.push(data.wait_list[i].id);	
				doAppend(data.wait_list[i]);				
			}else{
				if (!(data.wait_list[i].status == 1)) {
								doGetDasboard(1);
				};

			}
			};
				for (var i in data.process_list){
					var p_idx  = process_list.indexOf(data.process_list[i].id);
				if (  p_idx == -1  ) {
				process_list.push(data.process_list[i].id);	
				doAppend(data.process_list[i]);				
				}else{
				if (!(data.process_list[i].status == 2)) {
								   doGetDasboard(1);
				};
				};
			};
			for (var i in data.done_list){
				var d_idx  = done_list.indexOf(data.done_list[i].id);
				if (d_idx  == -1  ) {
				done_list.push(data.done_list[i].id);	
				doAppend(data.done_list[i]);				
			}else {
				if (!(data.done_list[i].status == 3)) {
								  doGetDasboard(1);
				};
			}
				
			};

		},
		error : function() {
			location.href = "login.html";
		},
	});
}


var doAppend = function(data) {
	
	node = $('#order_').clone();
	$(node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('.name', node).append(data.row+data.table_code );
	$('.content', node).append(data.menu_name + data.count+'');
	$('.date', node).append(data.order_time);
	
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
	doGetDasboard(1);
} 

var doUpdate = function() {
	doGetDasboard(0);

}

var doClear = function() {
	$('#watchingarea').html('')
	$('#processingarea').html('')
	$('#donearea').html('')

}






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



