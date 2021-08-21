
import requests
import logging

def get_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon_name

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return convert_response_to_pokemon(response.json())
    except:
        logging.warning(f"Error from {url} with status code {response.status_code} \n {response.text}")
    return None

def convert_response_to_pokemon(response):
    response_dict = {
        "name":None,
        "description":None,
        "habitat":None,
        "isLegendary":False
    }

    #Name
    try:
        name = response.get("name",None)
        if name:
            response_dict['name'] = name
    except:
        logging.warning("Failed to get the pokemon's name")
        pass

    #Description
    try:
        flavor_text = response.get("flavor_text_entries",None)
        if type(flavor_text) == list:
            description = flavor_text[0].get("flavor_text",None)
        if description:
            description = description.replace('\n',' ')
            description = description.replace('\f',' ')
            response_dict['description'] = description
    except:
        logging.warning("Failed to get the pokemon's description")
        pass

    #Habitat
    try:
        habitat = response.get("habitat",None)
        if habitat:
            response_dict['habitat'] = habitat.get("name",None)
    except:
        logging.warning("Failed to get the pokemon's habitat")
        pass

    #ledgend
    try:
        is_legendary = response.get("is_legendary",None)
        if is_legendary:
            response_dict['isLegendary'] = is_legendary
    except:
        logging.warning("Failed to get the pokemon's ledgendary statusc")
        pass

    # Just for a warning, in case the json changes for the response
    if None in response_dict.values():
        logging.warning(f"Some values are missing in the response: {response_dict}")

    return response_dict
