#!/usr/bin/node
const req = require('request');

req(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  console.log(resp.statusCode.toString());
});
