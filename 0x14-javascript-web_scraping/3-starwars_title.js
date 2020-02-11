#!/usr/bin/node
const req = require('request');

req('https://swapi.co/api/films/' + process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
