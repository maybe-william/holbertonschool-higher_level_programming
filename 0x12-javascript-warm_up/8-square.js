#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
}
const y = x;
while (x > 0 && !isNaN(x)) {
  console.log('X'.repeat(y));
  x = x - 1;
}
