"""cards - A module to manage decks of cards"""

__version__ = '0.1.0'
__author__ = 'James M Allen <james.m.allen@gmail.com>'

from cards.card import Card
from cards.deck import Deck
from cards.exceptions import DeckEmpty

__all__ = [
    'Card',
    'Deck',
    'DeckEmpty',
]
