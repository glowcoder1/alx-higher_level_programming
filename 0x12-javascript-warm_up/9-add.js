#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(args[0]) || isNaN(args[1])) {
  console.log('NaN');
} else {
  const sum = add(args[0], args[1]);
  console.log(sum);
}

function add (a, b) {
  return +a + +b;
}
