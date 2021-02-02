#!/usr/bin/node

const argument = process.argv[2];

if (argument === '0') {
  console.log('My number: ' + parseInt(argument));
} else if (argument && Number(argument)) {
  console.log('My number: ' + parseInt(argument));
} else {
  console.log('Not a number');
}
