var doOrderProcess = function(order) {

			if(order.status == 1)	{
			doOrderAppend(order);
			$('#finish_area #order_'+order.id).remove();
			$('#cancle_area  #order_'+order.id).remove();
			doSoundPlay();

			}
			 if(order.status == 4){
			$('#order_area #order_'+order.id).remove();
			doFinishAppend(order);
			}
			if(order.status == 0){
			$('#order_area #order_'+order.id).remove();
			doCancleAppend(order);
			}


};

var doStaffCallProcess = function(staffcall) {
			if(staffcall.status == 0)	{
			doStaffcallAppend(staffcall);
			doSoundPlay();
			}else if(staffcall.status == 1){
			$('#order_area #staff_'+staffcall.id).remove();
			}


};




var doStaffcall = function() {
	var id = $(this).val() ;
	var status = $("#staff_"+id).val();
	var status = status + 1;
	$.ajax({
		type : 'post',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		url : baseUrl + 'staffcall/' + id + "/update/",
		data : {
			status : status
		},
		success : function() {
			$('#staff_'+id).remove()
		},
		error : function(msg) {
		alert("통신이 실패하였습니다.");
		}
	});
}



var doGetStaffcall = function() {
	$.ajax({
		type : 'post',
		url : baseUrl + 'staffcall/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			for (var i in data.staffcall_list){
				if (staffcall_id_list.indexOf(data.staffcall_list[i])  == -1 && i >= 0 ) {
					staffcall_id_list.push(data.staffcall_list[i].id);
				staffcall_data_list.push(data.staffcall_list[i]);
					doStaffcallAppend(data.staffcall_list[i]);
				};

			};

		},
		error : function() {
		alert("통신이 실패하였습니다.");
		}
	});
}

var doGetOrderboard = function(value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'orderboard/',

		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			count = 0;
			for (var i in data.order_list){
				var idx  = order_list.indexOf(data.order_list[i].id);
				if (idx == -1) {
					count++;
					order_list.push(data.order_list[i].id);
					doOrderAppend(data.order_list[i]);
				}else{
				if (!(data.order_list[i].status == 1)) {
					$('#order_'+data.finish_list[i].id).remove();
						};
				};


		};

		},
		error : function() {
		alert("통신이 실패하였습니다.");
		}
	});
}


var doGetFinishboard = function(value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'finishboard/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {

			for (var i = data.finish_list.length - 1; i >= 0; i--){
				var idx  = finish_list.indexOf(data.finish_list[i].id);
				if (idx == -1  ) {
				finish_list.push(data.finish_list[i].id);
				doFinishAppend(data.finish_list[i]);
				}
		};

		},
		error : function() {
		alert("통신이 실패하였습니다.");
		}
	});
}

doGetCancleboard = function(value) {
	$.ajax({
		type : 'post',
		url : baseUrl + 'cancleboard/',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		success : function(data) {
			for (var i = data.cancle_list.length - 1; i >= 0; i--){
				var idx  = cancle_list.indexOf(data.cancle_list[i].id);
				if (idx == -1  ) {
				cancle_list.push(data.cancle_list[i].id);
				doCancleAppend(data.cancle_list[i]);
				}else{
				if (!(data.cancle_list[i].status == 1)) {
					$('#order_'+data.cancle_list[i].id).remove();
					};
				};
		};
		},
		error : function() {
		alert("통신이 실패하였습니다.");
		}
	});
}



var doStaffcallAppend = function(data) {

	node = $('#staff_').clone();
	$(node).attr("id", "staff_"+ data.id).attr("value",data.status);
	$('#table_row', node).append(data.row );
	$('#table_code', node).append(data.table_code );
	$('#staff_desc', node).append(data.staffcall_desc);
	$('#staff_count', node).append(data.count+'개');
	$('#staff_time', node).append( data.staffcall_time.substring(8));
	$('#RightBtn', node).attr("value",data.id);

	node.show();
	if (data.status == 0) {
	$('#order_area').append(node);
	};

}


var doOrderAppend = function(data) {

	node = $('#order_').clone();
	$(node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('#table_row', node).append(data.row );
	$('#table_code', node).append(data.table_code );
	$('#menu_name', node).append(data.menu_name);
	$('#menu_count', node).append(data.count+'개');
	$('#opt_name', node).append('옵션:'+data.option);

	$('#order_time', node).append( data.order_time.substring(8));
	$('#LeftBtn', node).attr("value",data.id);
	$('#RightBtn', node).attr("value",data.id);

	node.show();
	if (data.status == 1) {
	 $('#order_area').append(node);
	};



}


var doFinishAppend = function(data) {

	node = $('#order_').clone();
	$(node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('#table_row', node).append(data.row );
	$('#table_code', node).append(data.table_code );
	$('#menu_name', node).append(data.menu_name);
	$('#opt_name', node).append('옵션:'+data.option);
	$('#menu_count', node).append(data.count+'개');
	$('#order_time', node).append( data.order_time.substring(8));
	$('#LeftBtn', node).attr("value",data.id);
	$('#RightBtn', node).attr("value",data.id);

	node.show();

	if (data.status == 4) {
	$('#finish_area').prepend(node);
	};


}


var doCancleAppend = function(data) {

	node = $('#order_').clone();
	$(node).attr("id", "order_"+ data.id).attr("value",data.status);
	$('#table_row', node).append(data.row );
	$('#table_code', node).append(data.table_code );
	$('#menu_name', node).append(data.menu_name);
	$('#opt_name', node).append('옵션:'+data.option);
	$('#menu_count', node).append(data.count+'개');
	$('#order_time', node).append( data.order_time.substring(8));
	$('#LeftBtn', node).attr("value",data.id);
	$('#RightBtn', node).attr("value",data.id);

	node.show();

	if (data.status == 0) {
	$('#cancle_area').prepend(node);
	};
}






var doRightBtn = function() {
	var id = $(this).val() ;

	var status = $("#order_"+id).val();
	var status = status + 3;
	$.ajax({
		type : 'post',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		url : baseUrl + 'orders/' + id + "/update/",
		data :{
		status:status

		},
		success : function() {
			$('#order_'+id).remove()
		},
		error : function(msg) {
		alert("통신이 실패하였습니다.");
		}
	});
}



var doLeftBtn = function() {
	var id = $(this).val() ;
	var status = $("#order_"+id).val();
	var status = status - 1;
	$.ajax({
		type : 'post',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		url : baseUrl + 'orders/' + id + "/update/",
		data : {
			status : status
		},
		success : function() {
			$('#order_'+id).remove()
		},
		error : function(msg) {
		alert("통신이 실패하였습니다.");
		}
	});
}

var doReBackBtn = function() {
	var id = $(this).val() ;
	var status = $("#order_"+id).val();
	var status = status - 3;
	$.ajax({
		type : 'post',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		url : baseUrl + 'orders/' + id + "/update/",
		data : {
			status : status
		},
		success : function() {
		$('#order_'+id).remove()
		},
		error : function(msg) {
		alert("통신이 실패하였습니다.");
		}
	});
}


var doReRightBtn = function() {
	var id = $(this).val() ;
	var status = $("#order_"+id).val();
	var status = status + 1;
	$.ajax({
		type : 'post',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
		url : baseUrl + 'orders/' + id + "/update/",
		data :{
		status:status
		},
		success : function() {
			$('#order_'+id).remove()
		},
		error : function(msg) {
		alert("통신이 실패하였습니다.");
		}
	});
}

var doGetOrderInfo = function() {
	var order_id= $("div", this).html() ;
	$.ajax({
		type : 'get',
		beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
		},
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
			alert("통신이 실패하였습니다.");
		},
	});
}


var doShowConfirm = function() {
	console.log("클릭");
	$("#orderMdoal").modal("show");
}


var doCancel = function() {
	location.reload();
};


var doSoundPlay = function(){
var items=$('#order_area div');
if(items.length > 0){
	appendSound.play();
}
};

var doAllCompleted = function(){
	if(confirm('전체 주문을 완료처리하시겠습니까?')){
		$.ajax({
			type : 'post',
			beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
			},
			data : {
			status : status
			},
			url : baseUrl + 'orders/' + "allcompleted/",
			success : function() {
				location.reload();
			},
			error : function(msg) {
			alert("통신이 실패하였습니다.");
			}
		});
	}
}

var doAllCancle = function(){
	if(confirm('전체 주문을 취소처리하시겠습니까?')){
		$.ajax({
			type : 'post',
			beforeSend : function(req) {
			req.setRequestHeader('Authorization', loginstring);
			},
			data : {
			status : status
			},
			url : baseUrl + 'orders/' + "allcancle/",
			success : function() {
				location.reload();
			},
			error : function(msg) {
			alert("통신이 실패하였습니다.");
			}
		});
	}
}