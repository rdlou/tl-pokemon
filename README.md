# tl-Pokemon
Pokedex API

## Install instructions
First make sure you have Docker installed.

* Download Docker from here: ..................
* Install instructions for Mac and Linux here:................

Once Docker is installed, clone this repositry.  This can be done from the Github website using these instructions: 

Or from the command line using these instructions:

Once you have this locally on your machine, in your terminal navigate to the directory and run the following command:
* docker build

Once the project has been built, 2 endpoints will be exposed.

They will be:

* http://127.0.0.1:8080/pokemon/{pokemon_name}
* http://127.0.0.1:8080/pokemon/translated/{pokemon_name}

## Current Architecture
The basis of this is a FastAPI, uusing the standard python requests libarary to further query the pokeapi and the translation apis.  Pytest is doing the tests

## Production Architecture
I think the endpoints would be AWS lambda functions, rather than using FastAPI.  The reason for this is so that Amazon could deal with any scaling.  Secondly, I hate serializing API calls, so I would run a scheduled task at somepoint daily, which would drag the Pokedex db (only what's needed for our responses) and put it in a dynamoDb, sitting within the same environment as the lambda functions.  The scheduled job would add, remove and update entries from what currently sits within the database.  Any request coming to our lambda functions would now simply query our db.  Calls to the Pokedex API from the scheduler would be done using the requests module and asyncio.  As Pokemon are added to the db, so would their necessary transalations (these calls again being done by requests).  Finally, I'd have a separate service which could be called to query the Pokedex API, in the case that we do not find that Pokemon in our dynamoDb.

