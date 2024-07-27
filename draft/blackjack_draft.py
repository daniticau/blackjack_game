"""
import typing
from typing import Optional
import random

values = {'2': 2, '3': 3, '4': 4, '5': 5, 
          '6': 6, '7': 7, '8': 8, '9': 9, 
          '10': 10, 'J': 10, 'Q': 10, 'K': 10,
          'A' : 11}

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.populate()
        self.shuffle()

    def populate(self) -> None:
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def reveal_cards(self, n: int) -> None:
        for i in range(n):
            print(self.cards[i].__str__())

    def deal_card(self) -> Card:
        return self.cards.pop()
    
class Person:
    def __init__(self, money: Optional[int]) -> None:
        self.money = money
        self.hand = []
        self.value = 0
    
    def add_card(self, card: Card):
        self.hand.append(card)
        if card.rank == "A" and self.value + 11 > 21:
            self.value += 1
        else:
            self.value += values[card.rank]

    def display_hand(self):
        for i in range(len(self.hand)):
            print(f"{self.hand[i].__str__()}")
        print(f"Value: {self.value}")
        print()

    def get_value(self) -> int:
        return self.value
    
    def has_blackjack(self) -> bool:
        global values 
        if len(self.hand) == 2:
            total = sum(values[card] for card in self.hand if card in values)
            if total == 21:
                return True
        return False
    


def blackjack_round(deck: Deck, dealer: Person, player: Person):
    for i in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
    
    print("Dealer:")
    dealer.display_hand()
    print("Player:")
    player.display_hand()

    player_busted = False
    dealer_busted = False
    
    can_double = False
    can_split = False

    if player.get_value() == 9 or 10 or 11:
        can_double = True
    if player.hand[0].rank == player.hand[1].rank:
        can_split = True

    while True:
        decision = input("hit/stand (h/s): ").lower()
        if decision == 'h':
            player.add_card(deck.deal_card())
            print("Player:")
            player.display_hand()
            if player.get_value() > 21:
                print("player busted!")
                player_busted = True
                break
        elif decision == 's':
            break
        else:
            print("Invalid input.")
    
    while dealer.get_value() <= 16: 
        dealer.add_card(deck.deal_card())
        print("Dealer:")
        dealer.display_hand()
        if dealer.get_value() > 21:
            dealer_busted = True
            print("dealer busted!")
            break




def main(): 
    deck = Deck()
    dealer = Person(None)
    player = Person(1000)

    blackjack_round(deck, dealer, player)

if __name__ == "__main__":
    main()

"""

