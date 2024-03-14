def instruction():
    print('''
        This is the problem...
-Huy's just bought a new laptop ASUS TUF GAMING A15. To make sure, he created his laptop ASUS TUF GAMING A15's password
and made it changes everyday. 
-His first time of changing password is in 31th December 2020.
-The password today is the sum of a list of number from 0 to n, with n is the day since his first time of changing password.
(if n=2, today is 2nd Jan and the password is 3)
-The program will display a random day since 1st January 2021 to 31th December 2023 
-First of all, you can pick the number of round you want to play or play "solve til out of question" mode by input 0
-You will have 3 times to answer.
-You can input exit code "xxx" to exit the rounds
-Your mission is input the password of his laptop on that day, goodluck....
''')
def yes_no(question):
    print(question + "?  ")
    while True:
        r=input().lower()
        if r == "y" or r== "yes":
            return True
        elif r=="n" or r=="no":
            return False
        else:
            print("You did not choose the valid response")
def how_many_rounds():
    while True:
        error="Please input an integer greater than -1, input 0 to start a solve-til-out-of-question mode..."
        try:
            ans=input()
            if(ans=="xxx"):
                return "exit"
            ans=int(ans)
            if ans<0:
                print(error)
                continue
            elif ans==0:
                return 1095
            else:
                return ans
            return ans 
        except ValueError:
            print(error)
import random
def year(n):
    return int(n/365)
def months(m):
    m=int(m)
    if m==2:
        return 28
    elif (m%2!=0 and m<8) or (m%2==0 and m>=8):
        return 31
    else:
        return 30
def month_change(n):
    if n=="1":
        return "January"
    if n=="2":
        return "February"
    if n=="3":
        return "March"
    if n=="4":
        return "April"
    if n=="5":
        return "May"
    if n=="6":
        return "June"
    if n=="7":
        return "July"
    if n=="8":
        return "August"
    if n=="9":
        return "September"
    if n=="10":
        return "October"
    if n=="11":
        return "November"
    if n=="12":
        return "December"
def player():
    while True:
        ans=input()
        try:
            if(ans=="xxx"):
                return "exit"
            ans=int(ans)
            return ans 
        except ValueError:
            print("Please input a valid response...")
#history save the result of each round
history=[]
#turns letme know how many times they need to gave the right answer
turns=[]
#quiz_content save the content of quiz(for example: 1st September 2022,...)
quiz_content=[]
round_win=0 
sum_guesses_used=0
dup_quiz=[]
#each round
def quiz(n):
    dup=[]
    print(n)
    haha=int(n)
    ##count the years
    years=year(n)
    n=n-years*365
    month=1
    #count the month
    for i in range(1,13):
        if n==0:
            month=12
            years=years-1
            break;
        temp=months(i)
        if n<temp:
            break;
        else:
            n=n-temp
            month=month+1
    n=int(n)
    ans=int(((haha+1)*haha)/2)
    print(ans)
    if n==0:
        n=31
    if n%10==1:
        n=str(n)+"st"
    elif n%10==2:
        n=str(n)+"nd"
    elif n%10==3:
        n=str(n)+"rd"
    else:
        n=str(n)+"th"
    print(f"What is the password in {n} "+str(month_change(str(month)))+ f" {years+2021}?  ",end="")
    quiz_content.append(n+" "+str(month_change(str(month)))+" "+str(years+2021))
    for i in range(1,4):
        while True:
            p=player()
            if p=="exit":
                print("You choose exit...")
                return "exit"
            if p in dup:
                print("You'd already input this answer...")
            else:
                p=int(p)
                dup.append(p)
                break;
        if p==ans:
            print("😱 🎉 That's a correct answer!!!!!!!!"+"\n"*3)
            turns.append(i)
            history.append(f"You guessed the right answer in that round with {i} time(s) of guessing"+"   The answer is "+str(ans))
            return i
        else:
            print("Sorry, it's not the correct answer....")
            if(i!=3):
                print(f"You only have {3-i} turn(s) left...")
            else:
                print("😶 Sorry, you're out of turn...")
                print("The answer is "+str(ans)+"\n"*3)
                history.append("Sadly, you did not have any correct answer in that moment..."+"    The answer is "+str(ans))
                turns.append(3) 
                return 4

#main 
print("      Password💻🔑")
#print(month(2)) 
if yes_no("Do you want to read an instruction"):
    instruction()
rounds=0
print("How many rounds you want to play? ",end="")
#haha just the the variable to count how many round left till it reach 0
haha=how_many_rounds()
#play? is that variable to mark that they exit and dont want to play any round
playy=True
if(haha=="exit"):
    print("You choose exit")
    playy=False
    
if playy:
    while haha!=0:
        print(f"Quizz {rounds+1}...")
        #avoid from duplicate the quiz
        while True:
            n=random.randint(1,1095)
            if n in dup_quiz:
                continue
            dup_quiz.append(n)
            break
        what_now=quiz(n)
        if what_now==4:
            rounds=rounds+1
            sum_guesses_used=sum_guesses_used+int(what_now)-1
            haha=haha-1
        elif what_now=="exit":
            break
        else:
            sum_guesses_used=sum_guesses_used+int(what_now)
            rounds=rounds+1
            haha=haha-1
            round_win=round_win+1
if rounds!=0:
    if yes_no("Do you want to see your history"):
        for i in range(1,rounds+1):
            print("🕰🕰 Game history 🕰🕰️")
            print(f"Round {i}"+"\n"+f"The quiz is what is that password in {quiz_content[i-1]}: ")
            print(history[i-1])
    print("📊📊 Game Statistics 📊📊")
    print(f"You played {rounds} round(s)")
    print(f"You won {round_win} round(s)🎉  ||  You used about {int(sum_guesses_used/rounds)} turn(s) to guess per round")
else:
    print("You did not play any round...")
            
    
        
            
            
