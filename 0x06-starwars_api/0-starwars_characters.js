#!/usr/bin/env node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
    console.log('Usage: ./0-starwars_characters.js <Movie ID>');
    process.exit(1);
}

// API endpoint for the specified movie 
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the request to the API
request(url, (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }
    // Parse the response body as JSON
    const filmData = JSON.parse(body);
    
    // Check if film data contains characters
    if (!filmData.characters) {
        console.log('No characters found for this movie.');
        return;
    }

    // Iterate through the list of character URLs
    filmData.characters.forEach(characterUrl => {
        request(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
                console.log(charError);
                return;
            }
            // Parse the character data and print the name
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
        });
    });
});
