import random
import argparse

class Die:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0

    def roll_dice(self, die):
        roll = die.roll()
        print(f"{self.name} rolled a {roll}.")
        if roll == 1:
            print("Oops! Rolled a 1. Turn ends with no points added to the score.")
            return False
        else:
            self.turn_total += roll
            print(f"Current turn total: {self.turn_total}")
            return True

    def hold(self):
        self.score += self.turn_total
        self.turn_total = 0
        print(f"{self.name} chose to hold. Total score: {self.score}")
        return self.score

class Game:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.die = Die()

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"\nIt's {current_player.name}'s turn.")
        decision = input("Enter 'r' to roll or 'h' to hold: ")
        if decision == 'r':
            while current_player.roll_dice(self.die):
                pass
            self.switch_player()
        elif decision == 'h':
            current_player.hold()
            self.switch_player()
        else:
            print("Invalid input. Please enter 'r' or 'h'.")
            self.play_turn()

    def play_game(self):
        for player in self.players:
            player.score = 0  
        while max(player.score for player in self.players) < 100:
            self.play_turn()

        winner = max(self.players, key=lambda player: player.score)
        print(f"\nGame over! {winner.name} wins with a score of {winner.score}!")

def main():
    parser = argparse.ArgumentParser(description="Pig game with configurable number of players.")
    parser.add_argument("--numPlayers", type=int, default=2, help="Number of players in the game")
    args = parser.parse_args()

    players = [Player(f"Player {i+1}") for i in range(args.numPlayers)]

    while True:
        game = Game(players)
        game.play_game()
        play_again = input("Do you want to play another game? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    random.seed(0)  
    main()
