#!/usr/bin/node

const args = process.argv.slice(2);
const len = args.length;

if (len <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => {
    if (Number(a) < Number(b)) {
      return -1;
    } else if (Number(a) > Number(b)) {
      return 1;
    } else {
      return 0;
    }
  });
  console.log(Number(args[len - 2]));
}
