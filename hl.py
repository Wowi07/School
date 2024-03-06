def instruction():
  print('''    👆👆👆Higher Lower Game👇👇👇  
  - You can either choose the number of rounds or they can opt for infinite mode(by pressing 0).
  - You can choose the parameters for the game (ie: they choose the range involved which means they need to give us a low number and a high number where the mystery number will be between the two numbers we are given at the start of the game).
  - If you press the exit code ‘xxx’ or play the requested number of rounds, then the game end.
  - When the game ends, you are able to choose to see your game history.
  -There is a 3 different results in a single round, which is gold, silver or bronze depends on your number of guesses.
  -You will have an initial score for each round, which depend on the range you chose.(example: If you choose the range [1,100], your initial score gonna be 100. 
  -Each time you guess wrong, your score will be minus by 1
  ***🍀🍀 Good Luck 🍀🍀***
  ''')
def yes_no(question):
    print(question+"? ")
    while True:
        ans=input().lower()
        if ans=="y" or ans=="yes":
            return True
        elif ans=="n" or ans=="no":
            return False
        else:
            print("You do not input a valid response")

def rangee(greater):
    error=f"Please choose the number that greater than {greater}."
    try:
        while True:
            ans=input()
            if int(ans)>int(greater):
                return ans 
            else:
                print(error)
    except ValueError:
       print(error)
def check_int():
    error=f"Please choose the number that greater than -1, choose 0 to start the infinite mode."
    try:
        while True:
            ans=input()
            if int(ans)>0:
                return ans 
            elif ans == 0:
                return -1
            else:
                print(error)
    except ValueError:
       print(error)
def gold_rank_ans(n):
    return int(log2(n))
#main 
if yes_no("Do you want to read an instruction"):
    instruction()
print("How many round you want? Input 0 to start an infinite mode")
temps=int(check_int())
while temps!=0:
    temps=temps-1
    print("      Your range...🤏")
    print("Please enter the number on the left of your range  ",end=(""))
    left=rangee(0)
    print("Please enter the number on the right of your range",end=(""))
    right=rangee(left)
    print(f"Your guessing range is from {left} to {right}")
    


