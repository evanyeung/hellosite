$( document ).ready(function() {
	$("#comment-submit").click(function() {
		console.log("clicked");
		var url = 'localhost:8000/helloworld/ajax';
		$.post(url, function( data ) {
			console.log("posted?");
			data = json.parse( data )
			var message_html = ""
			for(var i = 0; i < len(data); i++) {
				console.log("message "  + i);
				message_html += "<div class="row">
									<div class='col-md-10 col-md-offset-2 message-div'>
										<h3>Author: + " data[i].fields.author " + </h3>
										<p>Message: + " data[i].fields.message " + </p>
										<p>date posted: + " data[i].fields.pub_date " +  + </p>
									</div>
								</div><!--row-->
								<br/>"
			}
			$("#message-col").html(message_html);
		}, "json");
	});
});