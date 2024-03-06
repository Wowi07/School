import math
def instruction():
  print(''' 
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
    error=f"Please choose the number that greater than {int(greater)+2}.  "
    try:
        while True:
            ans=input()
            if ans=="xxx":
                return "exit"
            ans=int(ans)
            if ans>int(greater+2):
                return ans 
            else:
                print(error)
    except ValueError:
       print(error)
def check_int():
    error=f"Please choose the number that greater than -1, choose 0 to start the infinite mode."
    while True:
        try:
            ans=input()
            if int(ans)>0:
                return ans 
            elif int(ans) == 0:
                return -1
            else:
                print(error)
        except ValueError:
           print(error)
# golden_ans(n):
# int(log2(n))

# silver_ans(n):
#int(n/2)
import random
def game_play(left,right):
    dup=[]
    times=0
    number=random.randint(int(left),int(right))
    print(f"Testing only:{number}")
    while True:
        player=0 
        print("What number is the mystery number🤔❓     ",end=(""))
        while True:
            try:
                player=input()
                if(player=="xxx"):
                    return "exit"
                player=int(player)
                if player in dup:
                    print("You'd already input this number...")
                    continue
                if player in range(int(left),int(right)+1):
                    dup.append(player)
                    break;
                print(f"please enter an integer in range {left} to {right}...")
            except ValueError:
                print(f"please enter an integer in range {left} to {right}...")
        times=times+1
        if(player==number):
            print("\n"*2)
            print(f"🎉🎉 Noiceeee, the mystery number is {number}")
            return times
        elif player>number:
            print(f"Nuh uh... it's not that high...")
        elif player<number:
            print(f"nahhh... it's not that low...")
        print("\n"*2)
        print(f"Your guessing times: {times}")
#main 
print("    👆 👆 👆  Higher Lower Game 👇 👇 👇 ")
if yes_no("Do you want to read an instruction"):
    instruction()
golden_medal=0 
silver_medal=0 
bronze_medal=0 
medal=[]
history=[]
print("How many round you want? Input 0 to start an infinite mode")
temps=int(check_int())
rounds=0
while temps!=0:
    print(f"👾👾 Round {rounds+1}👾👾")
    temps=temps-1
    print("      Your range...🤏")
    print("Please enter the number on the left of your range  ",end=(""))
    left=rangee(-2)
    if left=="exit":
        print("You choose exit...")
        break;
    left=int(left)
    print("Please enter the number on the right of your range(minimum range is 4)   ",end=(""))
    right=rangee(left)
    if right=="exit":
        print("You choose exit...")
        break;
    right=int(right)
    print(f"Your guessing range is from {left} to {right}")
    time=game_play(left,right)
    if(time=="exit"):
        print("You choose exit...")
        break;
    time=int(time)
    rounds+=1
    #ranking the result
    rangeee=right-left+1
    if time<=round(math.log2(rangeee)):
        print("Congratulation!! You get the golden medal on this round🥇")
        golden_medal=golden_medal+1
        medal.append("🥇")
    elif time<=int((rangeee*75)/100):
        print("Nice try... You get the silver medal on this round 🥈")
        silver_medal=silver_medal+1
        medal.append("🥈")
    else:
        print("You can do better next time, you get the bronze medal on this round🥉 ")
        bronze_medal=bronze_medal+1
        medal.append("🥉")
    print(f"You get {rangeee-time+1} points on this round")
    history.append(rangeee-time+1)
##history
if rounds==0:
    print("You did not play any round")
else:
    lowest_point=history[0]
    highest_point=history[0]
    haha=0
    for i in history:
        lowest_point=min(lowest_point,i)
        highest_point=max(highest_point,i)
        haha=haha+i
    if yes_no("Do you want to see the history"):
        for i in range (0,rounds):
            print(f"Round {i+1}:"+"\n"+ f"   You had {history[i]} points {medal[i]}")
    #stat 
    print("📊📊 Game Statistics 📊📊")
    print(f"  You played {rounds} round ")
    print(f"Highest point: {highest_point}   || Lowest point: {lowest_point}")
    print(f"Your average points is {haha/rounds}"+"\n"*2)
    print("🥇🥈🥉"+"\n")
    print(f"You got {golden_medal} golden medal(s) 🥇")
    print(f"        {silver_medal} silver medal(s) 🥈")
    print(f"        {bronze_medal} bronze medal(s) 🥉")
    
    
        
