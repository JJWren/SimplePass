import os
from dotenv import load_dotenv
from requests import get
from json import loads


def get_random_word() -> str:
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


def get_random_words(num_of_words: int) -> list:
    print("\nDepending on the desired number of words, this could take a little while. Please be patient as your words are collected for you.\n")
    word_set = set()
    while len(word_set) != num_of_words - 1:
        word_set.add(get_random_word())
    return word_set


def get_user_int() -> int:
    try:
        user_input = int(input("Enter an integer from 4 to 20: "))
    except ValueError:
        print("You must enter an integer from 4 to 20.")
        get_user_int()
    return user_input


if __name__ == "__main__":
    print(get_random_words(5))
