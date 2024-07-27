import typing
from typing import Optional, List
import random

from blackjack_classes import Card, Hand, ranks, suits, values

class BlackJackGame:
    def __init__(self) -> None:
        # create deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
        random.shuffle(self.deck)

        # instantiate player Hand
        player_cards = []
        for i in range(2):
            player_cards.append(self.deck.pop())
        self.player = Hand(player_cards, False)

        # instantiate dealer Hand
        dealer_cards = []
        for i in range(2):
            dealer_cards.append(self.deck.pop())
        self.dealer = Hand(dealer_cards, True)

    def show_both_hands(self) -> None:
        print("Player hand: ")
        self.player.show_hand()
        print()

        print("Dealer hand: ")
        self.dealer.show_hand()
        print()

    # player round
    def player_round(self) -> bool:
        while True:
            choice = input("Do you want to hit (h) or stand (s)? ")
            print()
            if choice == 'h':
                self.player.add_card(self.deck.pop(0))
                print(f"Player value: {self.player.get_value()}")
                print("Player hand: ")
                self.player.show_hand()
                print()
                if (self.player.get_value() > 21):
                    print("Player busted!")
                    return False
            elif choice == 's':
                break
            else:
                print("Not a valid input. ")
                print()
        return True

    # dealer round
    def dealer_round(self) -> bool:
        while self.dealer.get_value() < 17:
            print("Dealer hits!")
            self.dealer.add_card(self.deck.pop(0))
            print(f"Dealer value: {self.dealer.get_value()}")
            self.dealer.show_hand()
            print()
            if (self.dealer.get_value() > 21):
                print("Dealer busted!")
                return False
        return True
            
    def run(self) -> None:

        # print initial hands
        print("Player hand: ")
        self.player.show_hand()
        print()
        print("Dealer hand: ")
        self.dealer.show_card(0)
        print("____ of ____")
        print()

        # play out player hand
        if not self.player_round():
            return
        self.show_both_hands()

        # play out dealer hand
        if not self.dealer_round():
            return
        self.show_both_hands()

        # calculate winner
        if (self.player.get_value() > self.dealer.get_value()):
            print("Player wins!")
        elif (self.player.get_value() < self.dealer.get_value()):
            print("Dealer wins!")
        else:
            print("Standoff!")
    
game = BlackJackGame()
if __name__ == "__main__":
    game.run()