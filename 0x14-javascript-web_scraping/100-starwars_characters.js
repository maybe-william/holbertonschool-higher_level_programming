#!/usr/bin/node
const req = require('request');

req('https://swapi.co/api/films/' + process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  for (const x of JSON.parse(body).characters) {
    req(x, function (er2, r2, b2) {
      console.log(JSON.parse(b2).name);
    });
  }
});
