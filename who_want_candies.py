import random
# this function display the instruction whenever it called
def instructions():
    print("""
- Grandma want to test your calculate skill by asking tons of question about plus(+), minus(-), multiply(x) or divide(/) 2 numbers 'a' and 'b' 
(a+b,a-b,a x b or a/b).
- Before she give you a question, you can choose level of a question which is: 
    * 🟩 Easy  (|a|,|b|<=10).
    * 🟨 Normal(|a|,|b|<=1000).
    * 🟥 Hard  (|a|,|b|<=10000000).
- In any level, you still have a chance to get an easy question even in hard mode.
- With the divide question, you must round the answer to the nearest integer number(eg: 1.98 will be 2, 0.12 will be 0), if there is x.5(like 1.5 or 7.5) 
you must round to the nearest even number(if there is 1.5, round to 2; 7.5 round to 8, 10.5 round to 10).
- Every correct answer, you will have 1 candy(Easy), 2 candies(Normal) and 3 candies(Hard).
- You will have 3 times to answer each grandma's question.
- If you need a break, just say “I wanna sleep grandma” to end.(She won’t let you leave if you are not saying a correct sentence).
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


#this function return the number of round depends on user's input
def how_many_questions():
    print("How many questions you want to answer?( input 0 to start an infinite mode ♾️  ...)")
    error = "Please input an integer greater than 0 or input 0 to start an infinite mode ♾️  ..."
    while True:
        try:
            #i know, it's interger, but i also have to check if users wanna leave the program here, so i have to change all cap letters to lower
            ans = input().lower()
            # check if they wanna leave, if they want, return "exit"
            if (ans == "i wanna sleep grandma"):
                return "exit"
            # i assign ans into an interger, so i can check if user input an interger or not, if not, it will get value error and go straight to line 52, then go back to line 36 bc of the loop
            ans = int(ans)
            #if user input the number that below 0, it will print error message and go back to line 36 bc of the loop
            if ans < 0:
                print(error)
                continue
            #inf mode
            elif ans == 0:
                print("♾️  You choose an infinite mode ♾️")
                return -1
            else:
                return ans
        except ValueError:
            print(error)


# "operator_in_number_form" is a variable that stored an interger from 1-4, each number stand for an operator
# 1 -> +
# 2 -> -
# 3 -> x
# 4 -> /
def change_symbol(operator_in_number_form):
    if operator_in_number_form==1:
        return "+"
    if operator_in_number_form==2:
        return "-"
    if operator_in_number_form==3:
        return "x"
    if operator_in_number_form==4:
        return "/"
    

# this function will return boundary, candy user will get if they answer correctly, and the correct speech
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
            print("You choose an Easy question🟩")
            return 10,1,"You get 1 candy from this question 🟩"
        if response=="normal" or response=="n":
            print("You choose a Normal question🟨")
            return 1000,2 ,"You get 2 candies from this question 🟨"
        if response=="hard" or response=="h":
            print("You choose a Hard question🟥")
            return 10000000,3,"You get 3 candies from this question 🟥"
        print(error)


# this function return the answer of the question
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
question_content=[]
result_history=[]
turn_used_that_question=[]


# this function will: generate the question, receive and check user answer, return the result of that question
def single_question(boundary):
    #create question
    symbol=random.randint(1,4)
    a=random.randint(boundary*(-1),boundary)
    b=random.randint(boundary*(-1),boundary)
    if b==0 and symbol==4:
        while b==0:
            b = random.randint(boundary * (-1), boundary)
    print(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    question_content.append(f"What is the answer of {a} {change_symbol(symbol)} {b}")
    correct_answer=calculate_the_answer(a,b,symbol)
    duplicated_answer=[]
    for i in range(1,4):
        print(f"You have {3-i+1} turn(s) left to answer...")
        while True:
            try:
                user_answer=input().lower()
                #exit right here
                if (user_answer == "i wanna sleep grandma"):
                    return "exit"
                user_answer=int(user_answer)
                if user_answer in duplicated_answer:
                    print("You entered this answer before")
                    continue
                break 
            except ValueError:
                print("You did not choose a valid response")
        if user_answer==correct_answer:
            result_history.append(f"You gave a correct answer in this question which is {correct_answer}...")
            turn_used_that_question.append(i)
            return True,i
        duplicated_answer.append(user_answer)
    print(f"The correct answer is {correct_answer}")
    result_history.append(f"You didn't give any correct answer in this question, the answer is {correct_answer}...")
    turn_used_that_question.append(i)
    return False,3


#main 
#statistics variable
total_correct_question=0
total_guesses=0
user_total_candy=0
print("     Who want candies? 🍬🍭")
if yes_no("Do you want to read the instructions?  "):
    instructions()
# i created correct and incorrect speech as a list, so whenever i get the question result, i will random a number (from 0-5) stand for the position of speech i will display
# for eg: if user won, I got 2, then the program will display "👵: Well done darling😊"
correct_speech=["🎉 Haaaa, grandma is proud of you 🎉","👵: Take the candy my love🍭, I have more for you😊","👵: Well done darling😊","👵: You are doing great😄","👵: Good job, take this new flavour candy🍬","👵: If you're keep doing great like this, i'll need more candies next time😄"]
incorrect_speech=[" Grandma is kinda disappointed about you 😓","👵: Seems like you don't like this candy flavor🥲","👵: That's ok darling, you just need to practice more","👵: Ha, try more if you want those candies my love😊","👵: That's fine, relax darling","👵: Is that question too hard, my love?"]
exit_sign=True
questions_left=how_many_questions()
# if user wanna leave, the return of how_many_questions gonna be "exit"
# i created exit_sign to mark that user wanna continue or not
if questions_left=="exit":
    print("👵 Ok sweetie...")
    exit_sign=False
infinite_mode=""
# if user chose inf mode, i'll change the value of infinite_mode, 
# infinite_mode is used to display the words if user chose inf mode, if not, it will display nothing
if questions_left==-1:
    infinite_mode="  ♾️ Infinite mode ♾️"
question_answered=1
if exit_sign:
    # program continue if user did not exit or did not out of questions
    while questions_left!=0:
        print("\n"*3)
        print(f"Question {question_answered} "+infinite_mode)
        level=level_choosing()
        # exit this loop if they input the exit code inside of level_choosing
        if level=="exit":
            print("👵 Ok sweetie...")
            break
        # exit this loop if they input the exit code inside of single_question()
        # single_question_result is now contain the result in that question ( result: correct or not(true or false), how many times user answer)
        single_question_result=single_question(level[0])
        if single_question_result=="exit":
            print("👵 Ok sweetie...")
            break
        #if user correct
        elif single_question_result[0]:
            total_correct_question=total_correct_question+1
            total_guesses=total_guesses+single_question_result[1]
            print(correct_speech[random.randint(0,5)])
            user_total_candy=user_total_candy+level[1]
            print(level[2])
            print(f"Your total candies is {user_total_candy}...")
        # if user incorrect
        else:
            print(incorrect_speech[random.randint(0,5)])
            print(f"You don't get any candy in this question, so your total candy is still {user_total_candy}...")
            total_guesses=total_guesses+3
        questions_left=questions_left-1
        question_answered=question_answered+1
if question_answered==1:
    print("You did not answer any question...")
else:
    if yes_no("Do you want to see the history?  "):
        print("     🕰️ History 🕰️")
        for i in range(1,question_answered):
            print(f"    Question {i}:   ")
            print(f"Question content:   ",question_content[i-1],"?")
            print(f"(You used {turn_used_that_question[i-1]} time(s) to answer)",result_history[i-1])
    #statistics
    print("     📊 Statistics 📊")
    print(f"You answered {question_answered-1} question(s)")
    print(f"Total questions you gave a correct answer is {total_correct_question} question(s)  ({(total_correct_question*100)/(question_answered-1)}%)")
    print(f"You used about {int((total_guesses)/(question_answered-1))} time(s) to answer per question. ")




        
