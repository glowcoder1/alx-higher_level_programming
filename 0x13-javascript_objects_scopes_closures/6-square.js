#!/usr/bin/node
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let sqr = '';
        for (let j = 0; j < this.width; j++) {
          sqr += c;
        }
        console.log(sqr);
      }
    } else {
      this.print();
    }
  }
};
