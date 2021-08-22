# tl-Pokemon
Pokedex API

## Install instructions
First make sure you have Docker downloaded and installed.

* Follow the instructions for your operating system from here https://docs.docker.com/desktop/mac/install/

Once Docker is installed, clone this repositry.  This can be done from the Github website using these instructions: 

Or from the command line using these instructions: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository

Once you have this locally on your machine, in your terminal navigate to the directory and run the following command:
* docker build -t pokeapi .

Now the image has been built, we need to run the container with the following command:
* docker run -d --name pokeapi -p 80:80 pokeapi

Once the project has been built, 2 endpoints will be exposed.

They will be:

* http://127.0.0.1/pokemon/{pokemon_name}
* http://127.0.0.1/pokemon/translated/{pokemon_name}

## Current Architecture
The basis of this is a FastAPI, uusing the standard python requests libarary to further query the pokeapi and the translation apis.  Pytest is doing the tests

## Production Architecture
I think the endpoints would be AWS lambda functions, rather than using FastAPI.  The reason for this is so that Amazon could deal with any scaling.  Secondly, I hate serializing API calls, so I would run a scheduled task at somepoint daily, which would drag the Pokedex db (only what's needed for our responses) and put it in a dynamoDb, sitting within the same environment as the lambda functions.  The scheduled job would add, remove and update entries from what currently sits within the database.  Any request coming to our lambda functions would now simply query our db.  Calls to the Pokedex API from the scheduler would be done using the requests module and asyncio.  As Pokemon are added to the db, so would their necessary transalations (these calls again being done by requests).  Finally, I'd have a separate service which could be called to query the Pokedex API, in the case that we do not find that Pokemon in our dynamoDb.

