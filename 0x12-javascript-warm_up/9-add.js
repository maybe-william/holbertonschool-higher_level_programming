#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
    return NaN;
  }
  console.log(a + b);
  return a + b;
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
