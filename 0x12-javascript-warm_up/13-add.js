#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
this.add = add;
