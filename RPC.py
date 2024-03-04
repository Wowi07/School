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
history_p=[]
history_c=[]
history_r=[]
def yes_no(question):
    print(question + "  ")
    while True:
        r=input().lower()
        if r == "y" or r== "yes":
            return True
        elif r=="n" or r=="no":
            return False
        else:
            print("You did not choose the valid response")
import random
def cp():
    return random.randint(1, 3)
def cook(decision) :
    if decision == "r" or decision == "rock" or decision==1:
        return "rock" , "paper"
    elif decision == "p" or decision == "paper" or decision == 2:
        return  "paper" , "scissor"
    elif decision == "s" or decision == "scissor" or decision == 3:
        return "scissor" , "rock"
    else:
        print("You did not choose the valid response")
        return 0 , 0
def check_int():
    print("How many rounds would you like? Press 0 to join the infinite mode")
    while True:
        try:
            error="Please enter an integer bigger than 0 to play a requested rounds, or choose 0 to start inf mode"
            choose=int(input())
            if(choose<0):
                print(error)
            else:
                return choose
        except ValueError:
            print(error)
def game_play():
    #player's turn
    print("Please input your decision:  ")
    while True:
        temp=input();
        if(temp=="xxx"):
            return "exit"
        player=cook(temp);
        if(player[0]==0):
            continue;
        break;
    history_p.append(player[0])
    print("You choose " +player[0])
    #computer's turn
    print("It's computer turn 🤖")
    print("Please press <Enter> to continue....")
    input()
    computer=cook(cp())
    history_c.append(computer[0])
    print("Computer choose "+ computer[0])
    #win or lose
    if(player[1]==computer[0]):
        return "Computer"
    elif(player[0]==computer[0]):
        return "Tie"
    else:
        return "Player"
#main 
print("💎📰✂️ Rock Paper Scissors ✂️📰💎") 
if yes_no("Do you want to read the instruction?"):
    instruction()
#round choose
loop=check_int()
temps=0
win=0 
lose=0
if(loop==0):
    loop=loop-1 
while loop!=0:
    input("Press <Enter> to start this round....")
    print("\n"*10+f"👾👾   Round {temps+1}  👾👾 ")
    res=game_play()
    if(res=="exit"):
        print("You chose exit...")
        break;
    temps=temps+1
    if(res=="Computer"):
        history_r.append("Computer won this round 🤖 🫶")
        print("Computer win this round  🤖 🫶")
        print("\n"*2)
        lose=lose+1
    elif(res=="Player"):
        history_r.append("Player won this round 🤫 🧏️")
        print("Player win this round 🤫 🧏️ ")
        print("\n"*2)
        win=win+1
    else:
        history_r.append("You guys were tie this round 🤝")
        print("You guys are tie 🤝")
    loop=loop-1
#history 
if yes_no("Do you want to see the history?"):
    print("\n"*10)
    print("🕰🕰 Game history 🕰🕰️")
    for i in range (0,temps):
        print(f'''Round {i+1}:  
Player chose {history_p[i]}   ; Computer chose {history_c[i]} ~~~ So {history_r[i]}''')
#Stat 
print("📊📊 Game Statistics 📊📊")
if temps!=0:
    tie=temps-win-lose
    print(f"You played "+str(temps)+" rounds:")
    wins=win
    win=(float(win)*100)/float(temps)
    print(f"You won {wins} rounds ; which is {win}%")
    loses=lose
    lose=(float(lose)*100)/float(temps)
    print(f"You lose {loses} rounds ; which is {lose}%")
    temps=(float(tie)*100)/float(temps)
    print(f"You tie {tie} rounds ; which is {temps}%")
else:
    print("You did not play any round...")


    

    
    
    
    
