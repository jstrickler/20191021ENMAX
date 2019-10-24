#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        joker1 = 'Joker', 1
        joker2 = 'Joker', 2
        self._cards.append(joker1)
        self._cards.append(joker2)

