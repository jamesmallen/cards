import itertools
from typing import Union

import pytest

from cards import Card

all_valid_card_combos = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
                                               'CDHS'))


@pytest.mark.parametrize('number,suit', all_valid_card_combos)
def test_all_cards(number: str, suit: str) -> None:
    card = Card(number, suit)


@pytest.mark.parametrize('number,suit', [
    ('ace', 'spades'),
    (2, 'CLUBS'),
    (3, 'HeArTs'),
    ('4', 'Diamonds'),
])
def test_unusual_but_valid_cards(number: Union[int, str], suit: str) -> None:
    card = Card(number, suit)


@pytest.mark.parametrize('number,suit', [
    ('a', 'a'),
    ('acer', 'spadesers'),
    ('1', 'h'),
    ('11', 'h'),
])
def test_invalid_cards(number: str, suit: str) -> None:
    with pytest.raises(ValueError):
        card = Card(number, suit)
