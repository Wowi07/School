import random


# random a num
def randnum():
    respone = random.randint(1, 6)
    return respone


# return true or false depend on an answer
def yes_no(question):
    while True:
        player = input(question + '  ').lower()
        if player == 'yes' or player == 'y':
            return True
        if player == 'no' or player == 'n':
            return False
        else:
            print('You did not choose a valid response')


# check does the input is value(int, >13)
def check_int():
    while True:
        try:
            error = "Please enter an integer that is 13 or more."
            num = int(input("Please enter your target score: "))
            if (num < 13):
                print(error)
            else:
                return num
        except ValueError:
            print(error)


def instruction():
    intruc = bool(yes_no("Do you want to read the instruction:"))
    if intruc:
        print('''
        To begin, decide the overall score needed to be crowned the winner of the game (eg: first person to get a score of 50 or more).

    At the start of each round, the user and the computer each roll two dice. The initial number of points for each player is the total shown by the dice. Then, taking turns, the user and computer each roll a single die and add the result to their points. The goal is to get 13 points (or slightly less) for a given round. Once you are happy with your number of points, you can ‘pass’.

    - If you go over 13, then you lose the round (and get zero points).

    - If the computer goes over 13, the round ends and your score is the number of points that you have earned.

    - If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score stays the same).

    - If you get more points than the computer (but less than 14 points), you win and add your points to your score. The computer’s score stays the same.

    - If the first roll of your dice is a double, then your score is increased by double the number of points, provided you win. If the computer’s first roll of the dice is a double, then its points are not doubled (this gives the human player a slight advantage).

    - The ultimate winner of the game is the first one to get to the specified score goal.''')


# show who is heading
def update(n1, n2):
    print("*** Round Update ***:", end=" ")
    if n1 > n2:
        print("You are heading")
    elif (n2 > n1):
        print("Computer is heading")
    else:
        print("You guys are tie")
    print("\n" + "\n")


# gamepay in a single round
def game_play():
    input("Press <Enter> to start this round....")
    print("\n" + "\n")
    # create variables
    s1 = randnum()
    s2 = randnum()
    s3 = randnum()
    s4 = randnum()
    # signal is used to mark when player chose pass
    signal_c = 0
    signal_p = 0
    feedback = "If you win this round, you gain double point"
    P_score = s1 + s2
    C_score = s3 + s4
    # show player initial score,mark in variable db_score and feedback if player got db score
    db_score = False
    if s1 == s2:
        print(f"You rolled {s1} and {s2}, your total score is {P_score}" + f"   #{feedback}#" + "\n")
        db_score = True
    else:
        print(f"You rolled {s1} and {s2}, your total score is {P_score}" + "\n")
    # score of cp
    print(f"Computer rolled {s3} and {s4}, computer's total score is {C_score}" + "\n" + "\n")
    update(P_score, C_score)

    for i in range(0, int(10)):
        # player
        # only roll when signal_p==0, which mean if player pass 1 time, player cant roll again in this round
        if signal_p == 0 and yes_no("Do you want to continue rolling the dice? "):
            temp = randnum()
            P_score = P_score + temp
            print("\n" + "\n" + f"You rolled {temp}" + "\n" + f"Your total score is now {P_score}")
            # if cp score higher than target score
            if (P_score > 13):
                print(f"Your total score is over {13}, so computer win this round...")
                return "Computer is the winner" , db_score ,C_score
            # if player reach target score
            update(P_score, C_score)
            print("\n" + "\n")
        else:
            signal_p = 1

        # computer game play

        # this if line is marking when cp reach target score - 3 and heading the round, the condition signal_c==0 to make sure that it just work 1 time
        if (((C_score >= P_score) and C_score >= 10) or (signal_p == 1 and (C_score > P_score))) and signal_c == 0:
            signal_c = 1
            print("Computer is passing...."+"\n"*2)
        if signal_c == 0:
            trash=input("Press <Enter>  It's computer turn....")
            temp = randnum()
            C_score = C_score + temp
            print("\n" + "\n" + f"Computer rolled {temp}" + "\n" + f"Computer's total score is now {C_score}")
            # if player score higher than target score
            if (C_score > 13):
                print(f"Computer's total score is over {13}, so player win this round...")
                return "Player is the winner" , db_score, P_score
            # if cp reach target score
            update(P_score, C_score)
        if (signal_c > 0 and signal_p > 0):
            break
            # This case will return the result of this round if both didnt go over target score
    if (P_score > C_score):
        return "Player is the winner" , bool(db_score), int(P_score)
    elif (P_score < C_score):
        return "Computer is the winner" , db_score ,C_score
    else:
        return "tie" , db_score , int(P_score)


# main
print("🎲🎲 Roll it to 13 🎲🎲")
instruction()
P_total=int(0)
C_total=int(0)
history= []
target_score = int(check_int())
while True:
    result = game_play()
    if result[1]==True and result[0]=="Player is the winner":
        print("\n" + "\n" + "\n" + str(result[0]) + f", You gain x2 score, you will have {str(int(result[2]*2))} points adding to your total score")
        P_total=P_total+(int(result[2])*2)
    elif result[1]== False and result[0]=="Player is the winner":
        print("\n" + "\n" + "\n" + str(result[0])+ f" and have {str(result[2])} points adding to your total score")
        P_total=P_total+int(result[2])
    elif result[0]=="Computer is the winner":
        print("\n" + "\n" + "\n" + str(result[0])+ f" and have {str(result[2])} points adding to his total score")
        C_total=C_total+int(result[2])
    elif result[0]=="tie":
        print (f"You guys are tie in this round with {result[2]} score; both of you. Your point will not be change  ")
    if C_total>=target_score:
        print("\n"*7 +f"The game is over, with {C_total} point total,    COMPUTER WIN THIS GAME 😎 🤖 .")
        break;
    elif P_total>=target_score:
        print("\n"*7 +f"The game is over, with {P_total} point total,    PLAYER WIN THIS GAME 🤫 🧏️   .")
        break;
    print(f"Computer total score is now {C_total}" + "\n"*2 + f"Player total score is now {P_total}")
