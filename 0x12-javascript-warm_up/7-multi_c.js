#!/usr/bin/node
let x = parseInt(process.argv[2]);
while (x > 0 && !isNaN(x)) {
  console.log('C is fun');
  x = x - 1;
}
