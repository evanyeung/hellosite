$( document ).ready(function() {
	//for csrf
	var csrftoken = $.cookie('csrftoken');
	function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
		//contentType: "application/x-www-form-urlencoded",
		success: function(){alert("success"); console.log("success");},
		error: function(){alert("error"); console.log("success");},
		complete: function(){alert("complete"); console.log("complete");},
		crossDomain: false, // obviates need for sameOrigin test
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$("#comment-submit").click(function() {
		alert("clicked");
		//var url = 'localhost:8000/helloworld/ajax/';
		$.post('http://localhost:8000/helloworld/ajax/',{'name': 'country'}, function( data, status ) {
			console.log(status)
			alert("called"); });
			/*data = json.parse( data )
			var message_html = ""
			for(var i = 0; i < len(data); i++) {
				console.log("message "  + i);
				message_html += "<div class='row'>" +
									"<div class='col-md-10 col-md-offset-2 message-div'>" +
										"<h3>Author:" + data[i].fields.author + "</h3>" +
										"<p>Message:" + data[i].fields.message + "</p>" +
										"<p>date posted:" + data[i].fields.pub_date + "</p>" +
									"</div></div><!--row--><br/>"
			}
			$("#message-col").html(message_html);
		});*/

	});
});