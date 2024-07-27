import typing
from typing import Optional, List

ranks = ["2", "3", "4", "5", "6", "7", "8", "9",
         "10", "Jack", "Queen", "King", "Ace"]

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

values = {"2": 2, "3": 3, "4": 4, "5": 5, 
          "6": 6, "7": 7, "8": 8, "9": 9, 
          "10": 10, "Jack": 10, "Queen": 10, "King": 10,
          "Ace" : 11}

class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
    def get_rank(self) -> int:
        return self.rank
    
    def get_suit(self) -> int:
        return self.suit

    def get_value(self) -> int:
        return self.value
    
    
class Hand:
    def __init__(self, hand: List[Card], dealer: bool) -> None:
        self.hand = hand
        self.dealer = dealer
    
    def num_aces(self) -> int:
        count = 0
        for card in self.hand:
            if card.get_rank() == "Ace":
                count += 1
        return count

    def get_value(self) -> int:
        value = sum(card.get_value() for card in self.hand) 
        if value > 21 and self.num_aces() > 0:
                value -= 10
        if value > 21 and self.num_aces() == 2:
                value -= 10
        return value

    def show_card(self, index: int) -> None:
        print(self.hand[index])

    def show_hand(self) -> None:
        for i in range(len(self.hand)):
            print(self.hand[i])

    def add_card(self, card: Card) -> None:
        self.hand.append(card)