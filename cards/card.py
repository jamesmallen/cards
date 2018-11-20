"""
Card
"""
from typing import Union

ACE = 'a'
JACK = 'j'
KING = 'k'
QUEEN = 'q'

FACES = {JACK, QUEEN, KING, ACE}
NUMBERS = set(str(x) for x in range(2, 11))
VALID_NUMBERS = FACES | NUMBERS
NUMBER_TRANS = {
    'a': 'ace',
    'j': 'jack',
    'k': 'king',
    'q': 'queen',
}

SUITS = {
    'c': 'clubs',
    'd': 'diamonds',
    'h': 'hearts',
    's': 'spades',
}


class Card:
    """
    Represents a card, which consists of a number and a suit

    "Numbers" are 2-10 or "jack", "queen", "king", or "ace"

    "Suits" are clubs, diamonds, hearts, or spades
    """
    def __init__(self, number: Union[int, str], suit: str) -> None:
        number = str(number)
        if number.lower() not in VALID_NUMBERS:
            raise ValueError(f'Invalid number: {number}')
        self.number = number.lower()

        if suit.lower() not in SUITS.keys() and suit.lower() not in SUITS.values():
            raise ValueError(f'Invalid suit: {suit}')
        self.suit = suit.lower()

    def __str__(self) -> str:
        return f'{NUMBER_TRANS.get(self.number, self.number).title()} of {SUITS.get(self.suit, self.suit).title()}'
