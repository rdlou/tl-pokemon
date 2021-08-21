##TODO
import requests
import logging


def translate(pokemon):
    translated_description = get_translation(pokemon)
    pokemon['description'] = translated_description
    return pokemon

def get_translation(pokemon):
    habitat = pokemon.get("habitat", False)
    is_legendary = pokemon.get("isLegendary", False)
    description = pokemon.get("description", "")

    data = {"text": description}

    ## If the habitat is cave, or the pokemon is a ledgend, we use
    ## the yoda translator
    ## else go with shakespear
    ## set the url here, so we only have 1 block of code to do the api call
    if habitat == "cave" or is_legendary:
        url = "https://api.funtranslations.com/translate/yoda.json"
    else:
        url = "https://api.funtranslations.com/translate/shakespeare.json"

    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            return description
        translated = response.json().get("contents").get("translated")
        print(translated)
        return translated
    except:
        logging.warning(f"Call to {url} with data {data} failed with response {response.status_code}. \n {response.text}")
        return description


get_translation({"name":"","habitat":"cave","is_legendary":False,"description":"How are you today?"})