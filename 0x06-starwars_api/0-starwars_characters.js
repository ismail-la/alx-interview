#!/usr/bin/node

'use strict';

const request = require('request');

/**
 * Function to make a request to the Star Wars API to retrieve movie information
 * and print the characters of the movie based on the provided Movie ID.
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function getMovieCharacters(movieId) {
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(movieUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      return;
    }

    try {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      if (!characters || characters.length === 0) {
        console.log('No characters found for this movie.');
        return;
      }

      // Print characters
      characters.forEach(characterUrl => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
            return;
          }

          if (response.statusCode !== 200) {
            console.error('Invalid response:', response.statusCode);
            return;
          }

          const characterData = JSON.parse(body);
          console.log(characterData.name);
        });
      });
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  });
}

// Get the Movie ID from the command line arguments
const args = process.argv.slice(2);
const movieId = args[0];

if (!movieId) {
  console.error('Please provide the Movie ID as the first argument.');
  process.exit(1);
}

getMovieCharacters(movieId);
