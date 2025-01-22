import string
from abc import ABC, abstractmethod
from random import choice

import nltk

nltk.download("words")

def pin_password_generator(lengh_numbers: int) -> str:
    """Generate pin password
    :param lengh_numbers: Gets the number of pin digits
    """
    return (''.join(choice(string.digits) for _ in range(lengh_numbers)))


def random_password_generator(length_numbers: int, upper: bool = False, lower: bool = False) -> str:
    """Generate number & alphabet & punctuation password

    :param length_numbers: Gets the number of number & alphabet & punctuation password
    :param upper: Makes the alphabet bigger, defaults to False
    :param lower: It makes the alphabet smaller, defaults to False
    :return: Combines numbers, letters, and punctuation to return a password of the specified length.
    """
    if upper:
        ascii_letters = string.ascii_letters.upper()
    elif lower:
        ascii_letters = string.ascii_letters.lower()
    else:
        ascii_letters = string.ascii_letters
        
    return ''.join([choice(string.digits + ascii_letters + string.punctuation) for _ in range(length_numbers)])


def random_password_generator2(length_numbers: int, in_clude_numbers: bool = False, in_clude_symbol: bool = False) -> str:
    """Generate a combination of symbols and numbers for the password"""
    charctors = string.ascii_letters
    
    if in_clude_numbers:
        charctors += string.digits
    if in_clude_symbol:
        charctors += string.punctuation
    
    return "".join([choice(charctors) for _ in range(length_numbers)])


def memorable_password_generator(number_of_words: int = 4, separator_symbol: str = '-', capitalize: bool = None):
    """Generator password like this--> hello-bad-boy-Nice-bye

    :param number_of_words: Password word count, defaults to 4
    :param separator_symbol: word spacing symbol, defaults to '-'
    :param capitalize: the words with capital letters --> True, words with lowercase letters --> False, both --> None | defaults to None
    :return:  A memorable password output is generated. :)
    """
    list_words = nltk.corpus.words.words()
    
    if capitalize:
        return (separator_symbol.join([choice(list_words).upper() for _ in range(number_of_words)]))
        
    if capitalize == None:
        return (separator_symbol.join([choice(list_words).upper() if choice([True, False]) else choice(list_words).lower() for _ in range(number_of_words)]))
        
    return (separator_symbol.join([choice(list_words).lower() for _ in range(number_of_words)]))
