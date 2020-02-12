#!/usr/bin/node
const req = require('request');
const fs = require('fs');

req(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }

  fs.writeFile(process.argv[3], body.toString(), (err) => {
    if (err) {
      console.log(err);
    }
  });
});
