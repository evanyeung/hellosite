$( document ).ready(function() {
	$("#comment-submit").click(function() {
		var url = '/ajax';
		$.post(url, function( data ) {
			data = json.parse( data )
			var message_html = ""
			for(var i = 0; i < len(data.messages); i++) {
					message_html += "<div class="row">
										<div class='col-md-10 col-md-offset-2 message-div'>
											<h3>Author: + " data.messages.author " + </h3>
											<p>Message: + " data.messages.message " + </p>
											<p>date posted: + " data.messages.pub_date " +  + </p>
										</div>
									</div><!--row-->
									<br/>"
				}
			$("#message-col").html(messages)
		}, json);
	});
});