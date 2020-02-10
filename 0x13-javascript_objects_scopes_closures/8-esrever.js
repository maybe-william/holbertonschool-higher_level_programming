#!/usr/bin/node

exports.esrever = function (arr) {
  const i = arr.slice(0);

  return i.reduceRight((ar, item) => (ar.push(item) ? ar : ar), []);
};
