#!/usr/bin/node
this.addMeMaybe = function (number, theFunction) {
  if (this.myNum === undefined) {
    this.myNum = 1;
  }
  theFunction(this.myNum + number);
  this.myNum = this.myNum + 1;
};
