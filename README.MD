# I Doubt It

A Python implementation of the classic card game "I Doubt It (also called Bullshit)." The objective of the game is to be the first player to get rid of all your cards. The game uses a standard 52-deck of cards. Each round a specific rank is announced. Players take turns playing cards face down and declaring their ranks, and other players can challenge whether or not the rank they declared matches the card they placed face down. If a player is caught lying, they must take all the cards from the discard pile. If the player was telling the truth, the accuser must take all the cards in the discard pile. The first player to get rid of all their cards wins the game. The game requires three players.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Classes and Methods](#classes-and-methods)
4. [Game Rules](#game-rules)
5. [Authors](#authors)
6. [License](#license)

## Features

- **Interactive Gameplay**: Players can choose cards, challenge claims, and pick up discard piles.
- **Game Controller**: Manages game rounds, turns, challenges, and victory conditions.
- **Modular Design**: Classes for `Player`, `GameController`, `Dealer`, and `Card` to encapsulate game logic.
- **Error Handling**: Handles invalid inputs and ensures a smooth game flow.

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LuffyAI/IDOUBTITGAME.git
    cd i-doubt-it
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Run the game:
    ```bash
    python main.py
    ```

### Basic Usage

The game starts automatically with three players. Follow the on-screen prompts to play your turn and challenge other players' claims.

## Classes and Methods

### Player

- **`readHand()`**: Displays the player's hand sorted by rank.
- **`chooseCard()`**: Allows the player to select cards to play.
- **`removeCards()`**: Removes chosen cards from the hand and adds them to the discard pile.
- **`pickupDiscardPile()`**: Adds all cards from the discard pile to the player's hand.

### GameController

- **`start_round()`**: Runs each round, allowing players to play and challenge.
- **`check_for_winner()`**: Determines if any player has emptied their hand and won the game.

### Dealer

- **`deal()`**: Distributes cards among players.
- **`discard_pile`**: Keeps track of cards discarded by players.

## Game Rules

- **Objective**: Get rid of all cards in your hand.
- **Turn Order**: Each player takes turns choosing cards and declaring them.
- **Challenge**: Players can challenge others if they suspect they are bluffing.
- **Winning**: The first player to empty their hand wins the game.

## Authors

- Larnell Moore

## License

This project is licensed under the MIT License.
