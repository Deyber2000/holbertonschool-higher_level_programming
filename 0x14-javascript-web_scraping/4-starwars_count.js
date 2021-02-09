#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const searchID = '/18/';
let count = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes(searchID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
