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
    >>> len(deck.cards)
    52
    >>> deck.shuffle()
    >>> card = deck.deal_one()
    >>> print(card)
    Two of Clubs
    >>> card.number
    2
    >>> card.suit
    clubs
    >>> len(deck.cards)
    51

Compatibility
-------------

- Python 3.6 or higher

Licence
-------

MIT License


Authors
-------

`cards` was written by `James M Allen <james.m.allen@gmail.com>`_.
