from transliterate import translit#, get_available_language_codes
import requests
import json

def translit_to_ge(text, langpair):
    translited = translit(text, 'ka')
    ge_text = translited
    params = {'q': ge_text, 'langpair': langpair}
    r = requests.get('https://api.mymemory.translated.net/get', params=params)
    if r.status_code != 200:
        return "Error"
    response_str = r.text
    response_json = json.loads(response_str)
    return response_json["responseData"]["translatedText"]

#text = "Credo Bank: Mogesalmebit, tqveni barati damzadebulia. Gtxovt, miakitxot tqvens mier mititebul CREDO Bankis servicentrs."
#ex = translit_to_ge(text)
#print(ex)

def test_translit_to_ge():
    msg = "Credo Bank: Mogesalmebit, tqveni barati damzadebulia."
    lang = "ka-ge|ru"
    translated_text = translit_to_ge(msg, lang)
    translated_example = "Кредо Банк: Здравствуйте, ваша карта изготовлена."
    assert translated_text == translated_example
    return True
