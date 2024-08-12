#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characters = film.characters;

    if (!Array.isArray(characters)) {
      throw new Error('Characters data is not an array');
    }

    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          try {
            const character = JSON.parse(charBody);
            console.log(character.name);
          } catch (parseError) {
            console.error('Failed to parse character data:', parseError);
          }
        }
      });
    });
  } catch (parseError) {
    console.error('Failed to parse movie data:', parseError);
  }
});
