#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    const x = this.width;
    let y = this.height;
    while (y > 0) {
      console.log('X'.repeat(x));
      y = y - 1;
    }
  }
}
module.exports = Rectangle;
