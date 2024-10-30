# Authors: Larnell Moore 
# Creation Date: October 26, 2024
# Date Modified: October 26, 2024
# Purpose: The game controls the logic of a single game in 'I DOUBT IT.'

from dealer import Dealer, getRanks
from player import Player


############################################
#          Game Logic Controller           #
############################################
class GameController:
    def __init__(self):
        """Creates dealer and three players"""
        self.dealer = Dealer()
        self.players = [Player(f"Player {i + 1}", hand) for i, hand in enumerate(self.dealer.deal(3))]
        self.curr_rank_index = 0
        self.rank_order = getRanks()
        self.curr_player_index = 0  

    def next_rank(self):
        """Move to the next rank in the game sequence."""
        self.curr_rank_index = (self.curr_rank_index + 1) % len(self.rank_order)
        return self.rank_order[self.curr_rank_index]
        

    def start_round(self):
        """Flow of the game each round."""
        #Displays the current round's rank
        current_rank = self.rank_order[self.curr_rank_index]
        print(f"\n===>New round! The target rank is {current_rank}.<===")

        # Current player chooses card they claim matches the rank
        player = self.players[self.curr_player_index]
        print("============================================")
        print(f"\n{player.name}'s turn to play.")
        selected_cards = player.chooseCard()
        
        # Remove selected cards and add into the discard pile
        player.removeCards(selected_cards, self.dealer)  
        print(f"{player.name} claimed to play {len(selected_cards)} card(s) of {current_rank}.")

        # The next player in the sequence gets to decide to call out the previous player
        next_player_index = (self.curr_player_index + 1) % 3
        next_player = self.players[next_player_index]
        doubt = input(f"{next_player.name}, do you doubt {player.name}'s claim? (yes/no): ").strip().lower() == 'yes'

        if doubt:
            if all(card.rank == current_rank for card in selected_cards):
                print(f"{player.name} told the truth! {next_player.name} picks up the discard pile.")
                self.challenge_failed(next_player)
            else:
                print(f"{player.name} was bluffing! They pick up the discard pile.")
                self.challenge_successful(player)
        else:
            print(f"{next_player.name} did not doubt {player.name}'s claim.")
        print("============================================")
        print(" ")
        # Check for a winner after each turn
        if not self.check_for_winner():
            # Move to the next rank for the following round if no one doubted
            if not doubt:
                self.next_rank()
            # Update the turn to the next player
            self.curr_player_index = next_player_index

    def challenge_successful(self, player):
        """Handle the case where a bluff was correctly challenged."""
        player.hand.extend(self.dealer.discard_pile)  # Add the discard pile to the bluffing player's hand
        self.dealer.discard_pile.clear()  # Clear the discard pile

    def challenge_failed(self, challenger):
        """Handle the case where a challenge was incorrect."""
        challenger.hand.extend(self.dealer.discard_pile)  # Add the discard pile to the challenger's hand
        self.dealer.discard_pile.clear()  # Clear the discard pile

    def check_for_winner(self):
        """Check if any player has won the game by emptying their hand."""
        for player in self.players:
            if not player.hand:
                print(f"\n{player.name} wins the game!")
                return True
        return False

    def play_game(self):
        print("Starting 'I Doubt It' game with 3 players!")
        while not self.check_for_winner():
            self.start_round()
        print("Game over!")


if __name__ == "__main__":
    game = GameController()
    game.play_game()
