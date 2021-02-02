#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numberArray = process.argv.slice(2).sort((a, b) => a - b);
  console.log(numberArray[numberArray.length - 2]);
}
