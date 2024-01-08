#!/usr/bin/node

const args = process.argv.slice(2);
if (args[0]) {
  args.forEach((arg, i) => {
    console.log(arg);
  });
} else {
  console.log('No argument');
}
