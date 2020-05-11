from random import shuffle, choice


class Card:
    kind = ['diamonds', 'hearts', 'spades', 'clubs']
    worth = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck_cards = []
    single_card = None


class Deck(Card):
    def mix(self):
        for i in self.worth:
            for e in self.kind:
                if isinstance(i, int):
                    self.deck_cards.append(f'{str(i)} {e}')
                else:
                    self.deck_cards.append(f'{i} {e}')  
        shuffle(self.deck_cards)

    def get_card(self):
        self.single_card = choice(self.deck_cards)
        self.deck_cards.remove(self.single_card)
        print(self.single_card)


card = Deck()
card.mix()
card.get_card()
card.get_card()
card.get_card()
card.get_card()
print(len(card.deck_cards))
card.deck_cards.sort()
print(card.deck_cards)