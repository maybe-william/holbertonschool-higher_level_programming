#!/usr/bin/node

const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    let x = c;
    if (c === undefined) {
      x = 'X';
    }
    x = x.repeat(this.width);
    let y = this.height;
    while (y > 0) {
      console.log(x);
      y = y - 1;
    }
  }
}
module.exports = Square;
