#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  return list.map((item, i) => list[len - (i + 1)]);
};
