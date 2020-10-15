from random import randint,seed
import argparse
seed(0)

class Dice:
    """
    This program unfortunately does not work as I'd hoped, but at least I think I can explain why
    """
    @staticmethod
    def roll():
        return randint(1, 6)


class Player:
    """
    Dice and Player classes are OK, I think
    """
    def __init__(self, num):
        self.num = num
        self.total_score = 0
        self.play = True

    def __str__(self):
        return f"{self.num}"


# Here's where I lost the thread:
class Pig:
    def __init__(self, num_players):
        # I had wanted to try to make a version with a customizable number of players...
        self.pig_players = [Player(x) for x in range(0, num_players)]

    # ...but that led to me short-sightedly trying to define the entire game below:
    def play(self):
        # this is the current player
        p = 0
        winner = False
        while not winner:
            current_player = self.pig_players[p]
            # Looping through the player objects doesn't work
            # once you run out of players! It just terminates the loop without meeting endgame conditions.
            # I should have broken this up further for any hope of making it functional
            current_player.play = True
            current_score = 0
            while current_player.play:
                choice = input(f"Player {current_player}, would you like to hold (h) or  roll (r)? ")
                if choice.upper() == "H":
                    current_player.total_score += current_score
                    current_player.play = False
                elif choice.upper() == "R":
                    roll_score = Dice.roll()
                    if roll_score == 1:
                        print(f"Sorry Player {current_player}. You have rolled a 1 and your turn is over.")
                        current_player.play = False
                    else:
                        current_score += roll_score
                        print(f"Congratulations Player {current_player}, you rolled a {roll_score}, "
                              f" and your current score is {current_score} "
                              f" and your possible total score is {current_player.total_score + current_score} "
                              )
                        # check if the current player won
                        if current_player.total_score + current_score >= 100:
                            winner = True
                            current_player.play = False
                            current_player.total_score += current_score
                            print(f"Player {current_player} is the winner with {current_player.total_score}")
                else:
                    print("Not a valid input, please try again")

            # Move to next player
            if not winner:
                p += 1
                if p == len(self.pig_players):
                    p = 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayers', type=int, default=2)
    args = parser.parse_args()
    pig_game = Pig(args.numPlayers)
    pig_game.play()


if __name__ == "__main__":
    main()
