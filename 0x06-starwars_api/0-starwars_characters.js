#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
const movie_url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

function Req (char_List, index) {
  if (char_List.length === index) {
    return;
  }

  request(char_List[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(char_List, index + 1);
    }
  });
}

request(movie_url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const char_List = JSON.parse(body).characters;

    Req(char_List, 0);
  }
});
