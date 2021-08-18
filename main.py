from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, and welcome to the Pokedex :-)"}

@app.get("/pokemon/{pokemon_name}")
async def pokemon(pokemon_name):
    return {"message": f"Hello, this is {pokemon_name}"}

@app.get("/pokemon/translated/{pokemon_name}")
async def pokemon_transalted(pokemon_name):
    return {"message": f"Hello, this is {pokemon_name} wityh the translated stuff"}