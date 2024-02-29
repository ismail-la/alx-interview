#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function sendRequest(characterList) {
  try {
    for (const characterUrl of characterList) {
      const response = await axios.get(characterUrl);
      console.log(response.data.name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

async function main() {
  try {
    const response = await axios.get(movieEndpoint);
    const characterList = response.data.characters;
    await sendRequest(characterList);
  } catch (error) {
    console.error(error.message);
  }
}

main();
