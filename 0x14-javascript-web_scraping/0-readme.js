#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', error);

function error (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
}
