#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    for (const user of result) {
      if (user.completed === true) {
        const objId = user.userId;
        if (!dict[objId]) {
          dict[objId] = 1;
        } else {
          dict[objId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
