#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    if (data.id == 18) {
      consl
)};
