#!/usr/bin/node

exports.nbOccurences = function (arr, item) {
  let count = 0;
  let i = 0;
  for (i of arr) {
    if (i === item) {
      count = count + 1;
    }
  }
  return count;
};
