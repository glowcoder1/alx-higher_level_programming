#!/usr/bin/node

const arg1 = process.argv.slice(2)[0];

if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg1; i++) {
    let sq = '';
    for (let j = 0; j < arg1; j++) {
      sq = sq + 'X';
    }
    console.log(sq);
  }
}
