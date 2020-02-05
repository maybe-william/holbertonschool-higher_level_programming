#!/usr/bin/node
let x = process.argv.slice(2);
x = x.map(y => parseInt(y));
x.sort();
x.reverse();
x = x.filter(y => !isNaN(y));
if (x.length < 2) {
  console.log('0');
} else {
  console.log(x[1]);
}
