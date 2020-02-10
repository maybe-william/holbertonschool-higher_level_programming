#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
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

  rotate () {
    this.height = this.width ^ this.height;
    this.width = this.height ^ this.width;
    this.height = this.width ^ this.height;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
