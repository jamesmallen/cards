"""
Deck
"""
import itertools
from typing import Iterable

from cards import Card


class Deck:
    """
    Class to represent a deck of cards.

    Subclasses may override the numbers/suits attributes to have special decks
    """
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [
        'clubs',
        'diamonds',
        'hearts',
        'spades',
    ]

    def __init__(self, ) -> None:
        self.cards = list(self.generate_cards())

    @classmethod
    def generate_cards(cls) -> Iterable[Card]:
        """
        Builds the card objects that are in the Deck.

        Subclasses may override this method to have different decks (e.g., euchre decks)
        """
        for suit, number in itertools.product(cls.suits, cls.numbers):
            yield Card(number, suit)
