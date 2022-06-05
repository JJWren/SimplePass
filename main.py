import password_prelim


def SimplePass() -> str:
    '''Connects to WordsAPI and gathers an assortment of words to generate a password.\n
    Returns the password as a string.'''
    return " ".join(password_prelim.get_random_words())


if __name__ == "__main__":
    # test case
    print(SimplePass())
