#!/usr/bin/env python3

############
import random

############
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    ## moves string list was added to the Player class due to a
    ## traceback error, object has no attribute, meaning when called
    ## by the class it was not found !!!!
    moves = ["rock", "paper", "scissors"]

    def __init__(self):
        self.my_move = ["rock", "paper", "scissors"]
        self.their_move = random.choice(["rock", "paper", "scissors"])

    def move(self):
        return random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


#################################
class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


#################################


#################################
class HumanPlayer(Player):
    def move(self):
        while True:
            next_move = input(
                "Please type Rock, Paper, Scissors or quit  ./././././.......\n"
            )
            if next_move.lower() in self.moves:
                return next_move.lower()
            elif next_move.lower() not in self.moves:
                print("Wrong input mate, Try again!!!!!")
            elif next_move.lower() == "quit":
                print("Your Journey ends here !!!!")
                exit()


##################################

##################################
class ReflectPlayer(Player):
    def move(self):
        return self.their_move


##################################

##################################
class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


##################################


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        ################ Adding a score recorder to the game
        self.P1_Score = 0
        self.P2_Score = 0

    ## beats function was trasnfered to the game class to determine who ## wins each round by comparing each choice made
    def beats(self, one, two):
        return (
            (one == "rock" and two == "scissors")
            or (one == "scissors" and two == "paper")
            or (one == "paper" and two == "rock")
        )

    def play_round(self):
        move_1 = self.p1.move()
        move_2 = self.p2.move()
        print(f"Player 1: {move_1}  Player 2: {move_2}")
        if self.beats(move_1, move_2):
            print("Player 1 wins this round--> here is a point")
            self.P1_Score += 1
        elif move_1 == move_2:
            print("Round ended in Tie!!!!!!!!!!!!")
        else:
            print("Player 2 wins this round--> here is a point")
            self.P2_Score += 1
        self.p1.learn(move_1, move_2)
        self.p2.learn(move_2, move_1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round+1}:")
            self.play_round()
        if self.P1_Score > self.P2_Score:
            print("Player 1 wins this round ! Hooooraaay")
        elif self.P2_Score > self.P1_Score:
            print("Player 2 wins this round ! Hooooraaay")
        else:
            print("Game ends in a Tie")
        print("Game over!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
