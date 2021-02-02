#!/usr/bin/node

let number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  for (number; number > 0; number--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
