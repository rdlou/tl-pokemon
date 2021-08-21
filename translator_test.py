from translator import get_translation

def test_get_translation():
    #test for yoda
    assert get_translation({"name":"","habitat":"cave","is_legendary":False,"description":"How are you today?"}) == "You today,  how are?"
    #test for shakespear
    assert get_translation({"name":"","habitat":"moon","is_legendary":False,"description":"How are you today?"}) == "How art thee... present day?"