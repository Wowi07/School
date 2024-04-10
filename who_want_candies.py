def instructions():
    print("""     Who want candies? 🍬🍭
- Grandma want to test your calculate skill by asking tons of quiz about plus(+), minus(-), multiply(x) or divide(/) 2 numbers 'a' and 'b' 
(a+b,a-b,a x b or a/b).
- Before she give you a quiz, you can choose level of a quiz which is: 
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
- In any level, you still have a chance to get an easy question even in hard mode.
- With the divide quiz, you must round the answer to the nearest integer number(eg: 1.98 will be 2, 0.12 will be 0), if there is x.5(like 1.5 or 7.5) 
you must round to the nearest even number(if there is 1.5, round to 2; 7.5 round to 8, 10.5 round to 10).
- Every correct answer, you will have 1 candy(Easy), 2 candies(Normal) and 3 candies(Hard).
- You will have 3 times to answer each grandma's question.
- If you need a break, just say “I wanna sleep grandma” to end the game.(She won’t let you leave if you are not saying a correct sentence).
             ~~ Don't make grandma sad.😉
    """)
# This function return yes or no only depends on player response
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
# I use this one when I want to know how many rounds player wanna play
def how_many_rounds():
    print("How many rounds you want to play?( input 0 to start an infinite mode ♾️  ...)")
    error = "Please input an integer greater than 0 or input 0 to start an infinite mode ♾️  ..."
    while True:
        try:
            ans = input().lower()
            if (ans == "i wanna sleep grandma"):
                return "exit"
            ans = int(ans)
            if ans < 0:
                print(error)
                continue
            elif ans == 0:
                print("♾️  You choose an infinite mode ♾️")
                return -1
            else:
                return ans
        except ValueError:
            print(error)
# change number to operator
def change_symbol(s):
    if s==1:
        return "+"
    if s==2:
        return "-"
    if s==3:
        return "x"
    if s==4:
        return "/"
# This function will return a level player chose
def level_choosing():
    print("""Please choose the following level by input the first letter or full word.
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
""")
    error = "Please input a valid response"
    while True:
        response=input().lower()
        if (response == "i wanna sleep grandma"):
            return "exit"
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
# This function return the answer of quiz
def calculate_the_answer(a,b,operator):
    if operator==1:
        return a+b
    if operator==2:
        return a-b
    if operator==3:
        return a*b
    if operator==4:
        return round(a/b)
#history variables
quiz_content=[]
result_history=[]
turn_used_that_round=[]
import random
# single round here
def single_round(boundary):
    #create quiz
    symbol=random.randint(1,4)
    #random.randint(boundary*(-1),boundary) mean i will random a number from -boundary to boundary
    # eg: if my boundary is 10, so i will random a number from -10 to 10
    a=random.randint(boundary*(-1),boundary)
    b=random.randint(boundary*(-1),boundary)
    print(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    quiz_content.append(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    correct_answer=calculate_the_answer(a,b,symbol)
    # duplicated_answer is an array created to save player's answers
    duplicated_answer=[]
    # this will loop 3 times stand for 3 times answer the question
    for i in range(1,4):
        print(f"You have {3-i+1} turn(s) left to answer...")
        while True:
            try:
                player_answer=input().lower()
                #exit right here
                if (player_answer == "i wanna sleep grandma"):
                    return "exit"
                player_answer=int(player_answer)
                if player_answer in duplicated_answer:
                    print("You entered this answer before")
                    continue
                break 
            except ValueError:
                print("You did not choose a valid response")
        if player_answer==correct_answer:
            result_history.append(f"You gave a correct answer in this round which is {correct_answer}...")
            turn_used_that_round.append(i)
            return True,i
        #add the player_answer into duplicated_answer to mark that they have alr inputted this answer
        duplicated_answer.append(player_answer)
    print(f"The correct answer is {correct_answer}")
    result_history.append(f"You didn't give any correct answer in this round, the answer is {correct_answer}...")
    turn_used_that_round.append(i)
    return False,3

#main 
#statistics variable
total_win_round=0
total_guesses=0
player_total_candy=0
if yes_no("Do you want to read the instructions?  "):
    instructions()
win_speech="🎉 Haaaa, grandma is proud of you 🎉"
lose_speech="😒 Grandma is kinda disappointed about you 🤔"
exit_sign=True
rounds_left=how_many_rounds()
# in how_many_rounds() function, i will return "exit" if player input an exit code
# so if they wanna exit, i will change the exit_sign from True to False to mark that
# they wanted to exit
if rounds_left=="exit":
    print("👵 Ok sweetie...")
    exit_sign=False
# infinite_mode created because i wanna show "  ♾️  Infinite mode ♾️" if player chose inf mode
infinite_mode=""
if rounds_left==-1:
    infinite_mode="  ♾️  Infinite mode ♾️"
current_round=1
if exit_sign:
    while rounds_left!=0:
        print("\n"*3)
        print(f"Round {current_round}"+infinite_mode)
        #level will contain 
        #level[0] : a boundary to random
        #level[1] : how manycandy player can get if they win 
        #level[2]:  winning speech
        level=level_choosing()
        #once again, my level_choosing() will return "exit" if player inputted an exit code
        if level=="exit":
            print("👵 Ok sweetie...")
            break
        # single_round_result is a variable which contains True or False stand for win or lose, and how many turn(s) they used
        single_round_result=single_round(level[0])
        if single_round_result=="exit":
            print("👵 Ok sweetie...")
            break
        elif single_round_result[0]:
            total_win_round=total_win_round+1
            total_guesses=total_guesses+single_round_result[1]
            print(win_speech)
            player_total_candy=player_total_candy+level[1]
            print(level[2])
            print(f"Your total candies is {player_total_candy}...")
        else:
            print(lose_speech)
            print(f"You don't get any candy in this round, so your total candy is still {player_total_candy}...")
            total_guesses=total_guesses+3
        rounds_left=rounds_left-1
        current_round=current_round+1
if current_round==1:
    print("You did not played any round...")
else:
    if yes_no("Do you want to see the history?  "):
        print("     🕰️ History 🕰️")
        for i in range(1,current_round):
            print(f"    Round {i}:   ")
            print(f"Quiz:   ",quiz_content[i-1],"?")
            print(f"({turn_used_that_round[i-1]} turn(s) used)",result_history[i-1])
    #statistics
    print("     📊 Statistics 📊")
    print(f"You played {current_round-1} round(s)")
    print(f"Total rounds you gave a correct answer is {total_win_round} round(s)  ({(total_win_round*100)/(current_round-1)}%)")
    print(f"You used about {int((total_guesses)/(current_round-1))} turn(s) per round. ")




        
