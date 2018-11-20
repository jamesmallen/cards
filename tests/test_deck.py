from cards import Deck


def test_shuffle():
    deck = Deck()
    original_cards = list(deck.cards)
    deck.shuffle()
    assert list(deck.cards) != original_cards


def test_deal():
    deck = Deck()
    old_top_card = deck.cards[-1]
    dealt_card = deck.deal_card()
    assert dealt_card == old_top_card
    assert old_top_card not in deck.cards
