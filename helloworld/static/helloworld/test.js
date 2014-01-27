$( document ).ready(function() {
	console.log("loaded");
	$('#test-btn').on("click", function() {
		$.get('http://localhost:8000/helloworld/ajax/', function(data) {
			$('form').html(data);
		});
	});
});