

var order_list = [];
var staffcall_id_list = [];
var staffcall_data_list = [];



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
				// toast.push({body:'직원호출:'+data.staffcall_list[i].table_code +'테이블 '+ data.staffcall_list[i].staffcall_desc +' '+ data.staffcall_list[i].count +  '개', type:'Caution'
				// 	 ,onClick:doStaffcall(i) 
						// });	
				};
		
			};

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
			console.log(data);
			var update_check = false;
			for (var i in data.staffcall_list){
				if (staffcall_id_list.indexOf(data.staffcall_list[i].id)  == -1 && i >= 0 ) {
				staffcall_id_list.push(data.staffcall_list[i].id);
				staffcall_data_list.push(data.staffcall_list[i]);
				};
			};
			
			if (value == 1) {
				order_list.clear();
			};

			for (var i in data.order_list){
				var idx  = order_list.indexOf(data.order_list[i].id);
				if (idx == -1  ) {
				order_list.push(data.order_list[i].id);	
				doAppend(data.order_list[i]);				
				}else{
				if (!(data.order_list[i].status == 1)) {
					$('#order_'+data.order_list[i].id).remove();
					};	
				};
			
			if (update_check) {
				update(1);
			};
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
	$('#table_row', node).append(data.row );
	$('#table_code', node).append(data.table_code );
	$('#menu_name', node).append(data.menu_name);
	$('#menu_count', node).append(data.count+'개');
	
	$('#order_time', node).append(data.order_time);
	$('#LeftBtn', node).attr("value",data.id);
	$('#RightBtn', node).attr("value",data.id);
	
	node.show();
	if (data.status == 1) {
	$('#order_area').append(node);		
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
	$('#order_area').html('')


}






var doRightBtn = function() {
	var id = $(this).val() ;
	
	var status = $("#order_"+id).val();
	var status = status + 3;
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



