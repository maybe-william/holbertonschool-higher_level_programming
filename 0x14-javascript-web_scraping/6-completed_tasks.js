#!/usr/bin/node
const req = require('request');

req(process.argv[2], function (error, resp, body) {
  if (error) {
    console.log(error);
  }
  const results = JSON.parse(body);
  const hash = {};
  for (const x of results) {
    const uid = x.userId.toString();
    const comp = x.completed;
    if (comp) {
      hash[uid] = hash[uid] || 0;
      hash[uid] = hash[uid] + 1;
    }
  }
  console.log(hash);
});
