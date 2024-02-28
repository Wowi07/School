def instruction():
    print('''
                *** INSTRUCTION ***
- Users can either choose the number of rounds or they can opt for infinite mode.

- If users press the exit code ‘xxx’ or play the requested number of rounds, then the game should end.

- When the game ends, you should be able to choose to see your game history.

- During the game, you are able to type either the full word (rock / paper / scissors) or the first letter of the word (R / P / S) to indicate your choice.

- Remember that…

    * Paper beats rock

    * Rock beats scissors

    * Scissors beats paper''')
def yes_no(question):
    r=input(question + "  ").lower
    while True:
        if r == "y" or r== "yes":
            return True
        elif r=="n" or r=="no":
            return False
        else:
            print("You did not choose the valid response")
import random
def cp():
    return random.randint(1, 3)
def check_res(decision) :
    while True:
        if decision == "r" or decision == "rock":
            return "rock" , "paper"
        elif decision == "p" or decision == "paper":
            return  "paper" , "rock"
        elif decision == "s" or decision == "scissor":
            return False
        else:
            print("You did not choose the valid response")


def game_play():
    player = input("Please input your decision:  ")

