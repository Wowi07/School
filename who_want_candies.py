def instructions():
    print("""     Who want candies? 🍬🍭
- Grandma want to test your calculate skill by asking tons of quiz about plus(+), minus(-), multiply(x) or divide(/) 2 numbers 'a' and 'b'.
- Before she give you a quiz, you can choose level of a quiz which is: 
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
- In any level, you still have a chance to get an easy question even in hard mode.
- With the divide quiz, you must round the answer to the nearest interger number(eg: 1.98 will be 2, 0.12 will be 0), if there is x.5(like 1.5 or 7.5) 
you must round to the nearest even number(if there is 1.5, round to 2; 7.5 round to 8, 10.5 round to 10).
- Every correct answer, you will have 1 candy(Easy), 2 candies(Normal) and 3 candies(Hard).
- You will have 3 times to answer each grandma's question.
         ~~ Don't make grandma sad.😉
    """)
def yes_no(question):
    print(question)
    error="You did not choose a valid response"
    while True:
        try:
            response=input().lower()
            if response=="y" or response=="yes":
                return True
            if response=="n" or response=="no":
                return False
            else:
                print(error) 
        except ValueError:
            print(error)
def how_many_rounds():
    print("How many rounds you want to play?( input 0 to start an infinite mode ♾️  ...)")
    while True:
        error = "Please input an integer greater than 0 or input 0 to start an infinite mode ♾️  ..."
        try:
            ans = input()
            if (ans == "xxx"):
                return "exit"
            ans = int(ans)
            if ans < 0:
                print(error)
                continue
            elif ans == 0:
                print("♾️  You choose an infinite mode  ♾️")
                return -1
            else:
                return ans
        except ValueError:
            print(error)
def change_symbol(s):
    if s==1:
        return "+"
    if s==2:
        return "-"
    if s==3:
        return "x"
    if s==4:
        return "/"
def level_choosing():
    while True:
        error = "Please input a valid response"
        response=input("""Please choose the following level by input the first letter or full word.
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
""").lower()
        if response=="easy" or response=="e":
            print("You choose an Easy quiz🟩")
            return 10,1,"You get 1 candy from this round 🟩"
        if response=="normal" or response=="n":
            print("You choose a Normal quiz🟨")
            return 1000,2 ,"You get 2 candies from this round 🟨"
        if response=="hard" or response=="h":
            print("You choose a Hard quiz🟥")
            return 10000000,3,"You get 3 candies from this round 🟥"
        print(error)
def calculate_the_answer(a,b,operator):
    if operator==1:
        return a+b
    if operator==2:
        return a-b
    if operator==3:
        return a*b
    if operator==4:
        return round(a/b)
import random
def single_round(boundary):
    #create quiz
    symbol=random.randint(1,4)
    a=random.randint(boundary*(-1),boundary)
    b=random.randint(boundary*(-1),boundary)
    print(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    correct_answer=calculate_the_answer(a,b,symbol)
    duplicated_answer=[]
    for i in range(1,4):
        print(f"You have {3-i+1} turn(s) left to answer...")
        while True:
            try:
                player_answer=input()
                player_answer=int(player_answer)
                if player_answer in duplicated_answer:
                    print("You entered this answer before")
                    continue
                break 
            except ValueError:
                print("You did not choose a valid response")
        if player_answer==correct_answer:
            return True
        duplicated_answer.append(player_answer)
    return False

#main 
player_total_candies=0
if yes_no("Do you want to read the instructions?  "):
    instructions()
win_speech="🎉 Haaaa, grandma is proud of you 🎉"
lose_speech="😒 Grandma is kinda disappointed about you 🤔"
rounds_left=how_many_rounds()
infinite_mode=""
if rounds_left==-1:
    infinite_mode="  ♾️  Infinite mode ♾️"
current_round=1
while rounds_left!=0:
    print("\n"*3)
    print(f"Round {current_round}"+infinite_mode)
    level=level_choosing()
    if single_round(level[0]):
        print(win_speech)
        player_total_candies=player_total_candies+level[1]
        print(level[2])
        print(f"Your total candies is {player_total_candies}...")
    else:
        print(lose_speech)
        print(f"You don't get any candy in this round, so your total candies is still {player_total_candies}...")
    rounds_left=rounds_left-1
    current_round=current_round+1


    





    
