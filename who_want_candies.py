def instruction():
    print("""     Who want candies? 🍬🍭
- Grandma want to test your calculate skill by asking tons of quiz about plus(+), minus(-), multiply(x) or divide(/) 2 numbers 'a' and 'b'.
- Before she give you a quiz, you can choose a difficulty of a quiz which is:
    * Easy  (|a|,|b|<=10).
    * Normal(|a|,|b|<=1000).
    * Hard  (|a|,|b|<=10000000).
- With the divide quiz, you must round the answer to the nearest interger number(eg: 1.98 will be 2, 0.12 will be 0), if there is x.5(like 1.5 or 7.5) 
you must round to the nearest even number(if there is 1.5, round to 2; 7.5 round to 8, 10.5 round to 10).
- Every correct answer, you will have 1 candy(Easy), 2 candies(Normal) and 3 candies(Hard).
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
    while True:
        error = "Please input an integer greater than 0 or input 0 to start an infinite mode...♾"
        try:
            ans = input()
            if (ans == "xxx"):
                return "exit"
            ans = int(ans)
            if ans < 0:
                print(error)
                continue
            elif ans == 0:
                print("♾ You choose infinite mode♾ ")
                return -1
            else:
                return ans
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
def difficulty_choosing():
    while True:
        error = "Please input a valid response"
        response=input("""Please choose the following difficulty by input the first letter or full word.
    * Easy  (|a|,|b|<=10).
    * Normal(|a|,|b|<=1000).
    * Hard  (|a|,|b|<=10000000).""").lower()
        if response=="easy" or response=="e":
            return 10,1 
        if response=="normal" or response=="n":
            return 1000,2 
        if response=="hard" or response=="h":
            return 10000000,3
        print(error)

#main 
import random
if yes_no("Do you want to read the instructions?  "):
    instructions()
rounds=how_many_rounds()
#create quiz
symbol=random.randint(1,4)
difficulty=difficulty_choosing()




    





