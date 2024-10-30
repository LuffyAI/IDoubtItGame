# Authors: Larnell Moore 
# Creation Date: October 26, 2024
# Date Modified: October 26, 2024
# Purpose: This file encapsulates all of the player's actions that they can perform
# in the game 'I DOUBT IT.' 

from dealer import getRanks


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

############################################
#           Reading Operations             #
############################################
    def readHand(self):
        """Sorts the player's hand based on rank order defined in getRanks()
        and displays the cards in a player's hand and its corresponding index"""
        self.hand.sort(key=lambda card: getRanks().index(card.rank))  
        print(f"{self.name}'s hand:")
        for index, card in enumerate(self.hand, start=1):
            card_name = card.getCardName() 
            print(f"{index}: {card_name}")
        return self.hand

    def readDiscardPile(self, dealer):
        """Displays the cards that have been discarded by the players"""
        print("Discard pile:")
        for card in dealer.discard_pile:
            print(card.getCardName())

############################################
#             Player Actions               #
############################################
    def chooseCard(self):
        """Returns the cards that a player wants to discard in a round"""
        self.readHand()
        while True:
            choice = input("Enter the number(s) of the card(s) you want to choose (separated by spaces): ")
            try:
                # Parse and validate given input
                input_numbers = choice.split()  # Splits input into a list when space detected
                valid_inputs = [] 

                for num in input_numbers:
                    if num.isdigit():  # We first check if it is a number, no letters allowed.
                        index = int(num) - 1  # Sub by 1 since lists are zero-indexed
                        if index not in valid_inputs:  # We want to avoid duplicate inputs
                            valid_inputs.append(index)  # If valid, add to valid_inputs list.


                # Ensures valid_inputs is not empty and and that all items in valid_inputs
                # is a valid index within the range of self.hand
                if valid_inputs and all(0 <= idx < len(self.hand) for idx in valid_inputs):
                    # If is in within range, we consider that card as selected for play.
                    selected_cards = []
                    for i in valid_inputs:
                        selected_cards.append(self.hand[i])
                    return selected_cards  # Return selected cards without removing them from hand

                else:
                    # If any index is out of range or no valid corresponding card, throw error
                    print("Error: Please enter valid numbers that correspond to the cards in your hand.")
            
            except ValueError:
                # Handles any non-integer inputs 
                print("Error: Invalid input. Please enter only numbers.")


    def removeCards(self, selected_cards, dealer):
        """Removes the chosen cards from the player's hand and adds them to the discard pile."""
        # Add selected cards to the dealer's discard pile
        dealer.discard_pile.extend(selected_cards)

        # Remove selected cards from hand
        updated_hand = []
        for card in self.hand:
            if card not in selected_cards:
                updated_hand.append(card)
        self.hand = updated_hand
        print("")
        print("===> New Hand <===")
        self.readHand()
        print (" ")
        print("===> New Discard Pile <===")
        self.readDiscardPile(dealer)
        print(" ")

      

    def pickupDiscardPile(self, dealer):
        """Adds all cards from the discard pile to the player's hand and clears the discard pile."""
        # Add cards from discard pile to player's hand
        self.hand.extend(dealer.discard_pile)
        
        # Clear the discard pile
        dealer.discard_pile.clear()
        self.hand.sort(key=lambda card: getRanks().index(card.rank))
        print(f"\n{self.name}'s hand after picking up the discard pile:")
        for card in self.hand:
            print(card.getCardName())


