def instructions():
    print("""
- Grandma want to test your calculate skill by asking tons of quiz about plus(+), minus(-), multiply(x) or divide(/) 2 numbers 'a' and 'b' 
(a+b,a-b,a x b or a/b).
- Before she give you a quiz, you can choose level of a quiz which is: 
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
- In any level, you still have a chance to get an easy question even in hard mode.
- With the divide quiz, you must question the answer to the nearest integer number(eg: 1.98 will be 2, 0.12 will be 0), if there is x.5(like 1.5 or 7.5) 
you must round to the nearest even number(if there is 1.5, round to 2; 7.5 round to 8, 10.5 round to 10).
- Every correct answer, you will have 1 candy(Easy), 2 candies(Normal) and 3 candies(Hard).
- You will have 3 times to answer each grandma's question.
- If you need a break, just say “I wanna sleep grandma” to end the game.(She won’t let you leave if you are not saying a correct sentence).
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
def how_many_questions():
    print("How many questions you want to answer?( input 0 to start an infinite mode ♾️  ...)")
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
            return 10,1,"You get 1 candy from this question 🟩"
        if response=="normal" or response=="n":
            print("You choose a Normal quiz🟨")
            return 1000,2 ,"You get 2 candies from this question 🟨"
        if response=="hard" or response=="h":
            print("You choose a Hard quiz🟥")
            return 10000000,3,"You get 3 candies from this question 🟥"
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
#history variables
quiz_content=[]
result_history=[]
turn_used_that_question=[]
import random
def single_quiz(boundary):
    #create quiz
    symbol=random.randint(1,4)
    a=random.randint(boundary*(-1),boundary)
    b=random.randint(boundary*(-1),boundary)
    print(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    quiz_content.append(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    correct_answer=calculate_the_answer(a,b,symbol)
    duplicated_answer=[]
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
            result_history.append(f"You gave a correct answer in this question which is {correct_answer}...")
            turn_used_that_question.append(i)
            return True,i
        duplicated_answer.append(player_answer)
    print(f"The correct answer is {correct_answer}")
    result_history.append(f"You didn't give any correct answer in this question, the answer is {correct_answer}...")
    turn_used_that_question.append(i)
    return False,3

#main 
#statistics variable
total_correct_question=0
total_guesses=0
player_total_candy=0
print("     Who want candies? 🍬🍭")
if yes_no("Do you want to read the instructions?  "):
    instructions()
correct_speech="🎉 Haaaa, grandma is proud of you 🎉"
incorrect_speech="😒 Grandma is kinda disappointed about you 🤔"
exit_sign=True
questions_left=how_many_questions()
if questions_left=="exit":
    print("👵 Ok sweetie...")
    exit_sign=False
infinite_mode=""
if questions_left==-1:
    infinite_mode="  ♾️  Infinite mode ♾️"
question_answered=1
if exit_sign:
    #Game runs if player did not exit yet
    while questions_left!=0:
        print("\n"*3)
        print(f"Question {question_answered}? "+infinite_mode)
        level=level_choosing()
        if level=="exit":
            print("👵 Ok sweetie...")
            break
        single_quiz_result=single_quiz(level[0])
        if single_quiz_result=="exit":
            print("👵 Ok sweetie...")
            break
        elif single_quiz_result[0]:
            total_correct_question=total_correct_question+1
            total_guesses=total_guesses+single_quiz_result[1]
            print(correct_speech)
            player_total_candy=player_total_candy+level[1]
            print(level[2])
            print(f"Your total candies is {player_total_candy}...")
        else:
            print(incorrect_speech)
            print(f"You don't get any candy in this question, so your total candy is still {player_total_candy}...")
            total_guesses=total_guesses+3
        questions_left=questions_left-1
        question_answered=question_answered+1
if question_answered==1:
    print("You did not played any question...")
else:
    if yes_no("Do you want to see the history?  "):
        print("     🕰️ History 🕰️")
        for i in range(1,question_answered):
            print(f"    question {i}:   ")
            print(f"Quiz:   ",quiz_content[i-1],"?")
            print(f"(You used {turn_used_that_question[i-1]} time(s) to answer)",result_history[i-1])
    #statistics
    print("     📊 Statistics 📊")
    print(f"You played {question_answered-1} question(s)")
    print(f"Total questions you gave a correct answer is {total_correct_question} question(s)  ({(total_correct_question*100)/(question_answered-1)}%)")
    print(f"You used about {int((total_guesses)/(question_answered-1))} time(s) to answer per question. ")




        
