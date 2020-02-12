#!/usr/bin/node
const req = require('request');

req(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body).results;
  const wedges = results.filter((x) => x.characters.filter((y) => y.match(/people\/18\//)).length !== 0);
  console.log(wedges.length);
});
