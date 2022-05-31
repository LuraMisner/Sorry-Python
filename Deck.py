from Card import *
from random import *

class Deck:
    deck = list()

    def __init__(self):
        for i in range(4):
            new_card = Card(value.One)
            self.deck.append(new_card)
            new_card = Card(value.Two)
            self.deck.append(new_card)
            new_card = Card(value.Three)
            self.deck.append(new_card)
            new_card = Card(value.Four)
            self.deck.append(new_card)
            new_card = Card(value.Five)
            self.deck.append(new_card)
            new_card = Card(value.Seven)
            self.deck.append(new_card)
            new_card = Card(value.Eight)
            self.deck.append(new_card)
            new_card = Card(value.Ten)
            self.deck.append(new_card)
            new_card = Card(value.Eleven)
            self.deck.append(new_card)
            new_card = Card(value.Twelve)
            self.deck.append(new_card)
            new_card = Card(value.Sorry)
            self.deck.append(new_card)
        shuffle(self.deck)

    def draw_card(self) -> Card:
        if len(self.deck) == 0:
            self.__init__()

        drawing_card = self.deck[len(self.deck) - 1]
        self.deck.remove(drawing_card)
        if self.deck == {}:
            self.__init__()
        return drawing_card
