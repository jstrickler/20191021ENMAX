#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

c1 = CardDeck("Sylvia")

print(c1)

c2 = CardDeck("Ian")

print(c1.dealer)
print(c2.dealer)

c1.shuffle()
CardDeck.shuffle(c1)

print(c1.cards)

for i in range(10):
    card = c1.draw()
    print(card)

c2.shuffle()

j1 = JokerDeck("Jane")
print(j1)
j1.shuffle()
print(j1.draw())

print(j1.cards)


