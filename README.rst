cards
=====

A module to manage decks of cards

.. image:: https://img.shields.io/travis/jamesmallen/cards.svg
        :target: https://travis-ci.org/jamesmallen/cards


Installation
------------

.. code-block:: shell

    $ pip install git+https://github.com/jamesmallen/cards.git


Usage
-----

.. code-block:: python

    >>> from cards import Deck
    >>> deck = Deck()
    >>> len(deck)
    52
    >>> deck.shuffle()
    >>> card = deck.deal_card()
    >>> print(card)
    Two of Clubs
    >>> card.number
    2
    >>> card.suit
    clubs
    >>> len(deck)
    51

You can also extend or customize the ``Deck`` class by overriding attributes. For example, to make a Euchre deck (one that only has the cards 9, 10, J, Q, K, and A for each suit)::

    >>> class EuchreDeck(Deck):
            numbers = ['9', '10', 'J', 'Q', 'K', 'A']
    >>> euchre_deck = EuchreDeck()
    >>> len(euchre_deck)
    24
    >>> euchre_deck.shuffle()
    >>> print(euchre_deck.deal_card())
    Jack of Hearts


Compatibility
-------------

- Python 3.6 or higher

License
-------

MIT License


Authors
-------

`cards` was written by `James M Allen <james.m.allen@gmail.com>`_.
