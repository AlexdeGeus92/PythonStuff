#fizzbuzz.py
"""
Fooling around with Python generators and FizzBuzz.
@Author: AlexG.
"""

from itertools import cycle, chain, repeat

def fizzbuzz(n, **kwargs):
    """ 
    Play any game of FizzBuzz for N iterations.
    For **kwargs use e.g. fizz=3, buzz=5.
    """
    numbers = map(str, range(1, n+1))    
    words = map("".join, zip(*[
        cycle(chain(repeat("", value-1), [name.capitalize()]))
        for name, value in kwargs.items()
    ]))
    for number, word in zip(numbers, words):
        yield max(number, word)
 
if __name__ == "__main__": 

    for result in fizzbuzz(1000000, fizz=3, buzz=5):
        print(result)
       