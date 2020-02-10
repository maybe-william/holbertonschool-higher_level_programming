#!/usr/bin/node
const d = require('./101-data').dict;

const x = {};
for (const key in d) {
  x[d[key]] = x[d[key]] || [];
  x[d[key]].push(key);
}

console.log(x);
