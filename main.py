import password_prelim


def SimplePass() -> str:
    '''Connects to WordsAPI and gathers an assortment of words to generate a password.\n
    Returns the password as a string.'''

    num_of_words = password_prelim.get_user_int()

    word_list = list(password_prelim.get_random_words(num_of_words))
    return " ".join(word_list)


if __name__ == "__main__":
    # test case
    print(SimplePass())
