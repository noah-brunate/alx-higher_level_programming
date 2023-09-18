#!/usr/bin/node

const request = require('request');

url = "https://kontests.net/api/v1/all";


request(url, (error, response, body) => {
	if (error) {
		console.log("An error happened");
	}
	console.log(response.statusCode);
	console.log(body);
});
