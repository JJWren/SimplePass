import os
from dotenv import load_dotenv
from requests import get
from random import randrange
from json import loads


def get_random_word() -> str:
    '''Requests a random word using the wordsapi from rapidapi.\n
    Requires at least a free API key.'''
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random": "true"}
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    headers = {
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": API_KEY
    }

    json_response = loads(get(
        url, headers=headers, params=querystring).text)

    return json_response["word"]


def get_random_words() -> list:
    '''Requests a random number of random words using the wordsapi from rapidapi.\n
    Requires at least a free API key.'''
    print("\nThis could take a few seconds. Please be patient as your words are collected for you...\n")
    word_set = set()
    while len(word_set) != randrange(4, 11):
        word_set.add(get_random_word())
    return list(word_set)


if __name__ == "__main__":
    print(get_random_words())
