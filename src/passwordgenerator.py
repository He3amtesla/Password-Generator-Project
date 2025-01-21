import string
from abc import ABC, abstractmethod
from random import choice

import nltk


nltk.download("words")


list_words = nltk.corpus.words.words()

class PasswordGenerator(ABC):   
    @abstractmethod
    def generator(self):
        pass
    

class PinPasswordGenerator(PasswordGenerator):
    def __init__ (self, length_numbers: str): #جایی که آبجکت ساخته میشود.
        self.length_numbers= length_numbers
        
    def generator(self) -> str:
        return ''.join( [choice(string.digits) for _ in range(self.length_numbers)] )


class RandomPasswordGenerator(PasswordGenerator):
    def __init__ (self, length_numbers: int, upper: bool = False, lower: bool = False): #جایی که آبجکت ساخته میشود.
        self.length_numbers= length_numbers
        self.punctuation = string.punctuation
        if upper:
            self.ascii_letters = string.ascii_letters.upper()
            #self.punctuation = string.punctuation.upper()
        elif lower:
            self.ascii_letters = string.ascii_letters.lower()
            #self.punctuation = string.punctuation.lower()
        else:
           self.ascii_letters = string.ascii_letters
          # self.punctuation = string.punctuation
    
    def generator(self) -> str :
        return(''.join( [choice(string.digits + self.ascii_letters + self.punctuation) for _ in range(self.length_numbers)] ))


class RandomPasswordGenerator2(PasswordGenerator):
    def __init__ (self, length_numbers: int, in_clude_numbers: bool = False, in_clude_symbol: bool = False): #جایی که آبجکت ساخته میشود.
        self.length_numbers = length_numbers
        self.charctors = string.ascii_letters
        
        if in_clude_numbers:
            self.charctors += string.digits
        if in_clude_symbol:
            self.charctors += string.punctuation
    
    def generator(self) -> str:
        return ''.join([choice(self.charctors) for _ in range(self.length_numbers)])
    
    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, number_of_words: int = 4, separator_symbol: str = '-', capitalize: bool = None):
        self.number_of_words = number_of_words
        self.separator_symbol = separator_symbol
        self.capitalize = capitalize
        
    def generator(self) -> str:
        if self.capitalize:
            return (self.separator_symbol.join([choice(list_words).upper() for _ in range(self.number_of_words)]))
        
        if self.capitalize == None:
            #return (self.separator_symbol.join([choice([choice (list_words), choice(list_words).upper()]) for _ in range(self.number_of_words)]))
            return (self.separator_symbol.join([choice(list_words).upper() if choice([True, False]) else choice(list_words).lower() for _ in range(self.number_of_words)]))
        
        return (self.separator_symbol.join([choice(list_words).lower() for _ in range(self.number_of_words)]))
    
    
def test_pin_password_genrator():
    pin_gen = PinPasswordGenerator(length_numbers=4)
    pin = pin_gen.generator()
    assert len(pin) == 4
    assert all(charters in string.digits for charters in pin)


def test_random_password_generator():
    rndger = RandomPasswordGenerator(length_numbers = 10, upper = True)
    rndome = rndger.generator()
    print(rndome)
    assert len(rndome) == 10
    assert any(_ in string.punctuation for _ in rndome)
    assert any(_ in string.ascii_uppercase for _ in rndome)
    
   
def test_random_password_generator2():
    rndger = RandomPasswordGenerator2(10, in_clude_numbers=True)
    rndome = rndger.generator()
    print(rndome)
    assert len(rndome) == 10
    assert any(charters in string.digits for charters in rndome)

def test_memorable_password_generator():
    m_password = MemorablePasswordGenerator()
    mpass = m_password.generator()
    print(mpass)
    assert len(mpass.split('-')) == 4
    assert '-' in mpass
    
    
if __name__ == "__main__":
    print("pin password generator: ")
    test_pin_password_genrator()
    print("random password generator: ")
    test_random_password_generator()
    print("random password generator2: ")
    test_random_password_generator2()
    print("memorable password generator: ")
    test_memorable_password_generator()
