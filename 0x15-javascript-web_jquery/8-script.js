$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.alx-tools.com/api/films/?format=json",
		function (films) {
			for (const film of films.results) {
				function (film) {
					$("UL#list_movies").append("<li>film.title<\li>");
				}
			}
		}
	);
});

