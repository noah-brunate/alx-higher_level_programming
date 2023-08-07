$(document).ready(function () {
	$.ajax(function () {
		url: "https://fourtonfish.com/hellosalut/?lang=fr",
		method: "GET",
		sucess: function (data) {
			$('DIV#hello').text(data.hello);
		}
	});
});
