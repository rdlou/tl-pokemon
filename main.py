from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pokedex import get_pokemon
import translator
import json
import pytest


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, and welcome to the Pokedex :-)"}

@app.get("/pokemon/{pokemon_name}")
async def pokemon(pokemon_name):
    pokemon = get_pokemon(pokemon_name)

    if not pokemon:
        return JSONResponse(content={"message":f"Unable to find a pokemon with the name {pokemon_name}"},status_code=404)
    return pokemon

@app.get("/pokemon/translated/{pokemon_name}")
async def pokemon_transalted(pokemon_name):
    pokemon = get_pokemon(pokemon_name)
    translated_pokemon = translator.translate(pokemon)
    return translated_pokemon