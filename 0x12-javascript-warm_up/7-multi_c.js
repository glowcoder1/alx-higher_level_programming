#!/usr/bin/node

const arg1 = process.argv.slice(2)[0];

if (isNaN(arg1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
