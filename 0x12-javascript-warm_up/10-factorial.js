#!/usr/bin/node

const arg1 = process.argv.slice(2)[0];

if (isNaN(arg1)) {
  console.log(1);
} else {
  const val = Number(arg1);
  const res = factorial(val);
  console.log(res);
}

function factorial (a) {
  if (a < 2) {
    return 1;
  }
  return a * factorial(a - 1);
}
