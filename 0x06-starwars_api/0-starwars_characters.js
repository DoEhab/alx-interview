#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (err, res, body) => {
  if (err) {
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  function printChars (index) {
    if (index >= characters.length) return;
    request(characters[index], (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
      printChars(index + 1);
    });
  }
  printChars(0);
});
