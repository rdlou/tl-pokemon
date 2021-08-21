from pokedex import convert_response_to_pokemon, get_pokemon

def test_convert_response_to_pokemon():
    #name
    assert convert_response_to_pokemon({"name":"george"}).get("name") == "george"
    #is ledg
    assert convert_response_to_pokemon({"is_legendary":False}).get("isLegendary") == False
    #description
    assert convert_response_to_pokemon({"flavor_text_entries":[{"flavor_text":"test_the_dict_override_words"}]}).get("description") == "test_the_dict_override_words"
    #habitat
    assert convert_response_to_pokemon({"habitat":{"name":"george"}}).get("habitat") == "george"


def test_get_pokemon():
    #test it doesn't find gibberish
    assert get_pokemon("alksdjfhasdf") == None
    #test a well known
    assert get_pokemon("mewtwo").get("name") == "mewtwo"

