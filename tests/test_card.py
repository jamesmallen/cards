import itertools

import pytest

from cards import Card

all_valid_card_combos = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'],
                                               'CDHS'))


@pytest.mark.parametrize('number,suit', all_valid_card_combos)
def test_valid_cards(number, suit) -> None:
    card = Card(number, suit)

