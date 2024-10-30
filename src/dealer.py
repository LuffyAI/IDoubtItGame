# Author: Larnell Moore
# Creation Date: October 26, 2024
# Last Modified: October 26, 2024
# Purpose: This class simulates a standard 52-card deck and the dealer.
# A "suit" represents one of the four categories of cards: Hearts, Diamonds, Clubs, and Spades.
# Each suit contains 13 "ranks" or card values: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King.
# Together, they compromise the standard 52-Deck of cards (4 suits x 13 = 52 cards)
# The dealer deals the card to each player.

import random

############################################
#           Helper Functions               #
############################################
def getSuits():
    return ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def getRanks():
    return ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

############################################
#  Individual Card from Standard 52-Deck   #
############################################
class Card:
    def __init__(self, rank, suit):
        """Each card has a specific rank & suit"""
        self.rank = rank
        self.suit = suit

    def getCardName(self):
        """Returns the suit and rank of a given card, 
        such as Ace of Spades."""
        return f"{self.rank} of {self.suit}"
    
###############################################
# Creates 52-Deck & shuffles them for players # 
###############################################
class Dealer:
    def __init__(self):
        """Creates the 52-standard deck and ensures each suit has the following 13 cards:
        Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10. Jack, Queen, King"""

        self.deck = []
        self.discard_pile = []

        for suit in getSuits():
            for rank in getRanks():
             self.deck.append(Card(rank, suit))
        random.shuffle(self.deck)

    def getSize(self):
        """Returns the # of cards in the deck"""
        return len(self.deck)

    def deal (self, numOfPlayers):
        """Returns the player hands"""

        # Sets the number of decks based on # of players
        playerHands = []
        for x in range(numOfPlayers):
            playerHands.append([])

        # Give each card to the next player in turn
        while self.deck:
            for hand in playerHands:
                if self.deck:
                    hand.append(self.deck.pop(0))
        return playerHands
    
