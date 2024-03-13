def instruction():
    print('''This program can generate the quiz 
        This is the problem...
-Huy created his laptop's password and made it changes everyday. 
-His first time of changing password is in 31th December 2020.
-The password today is the sum of a list of number from 0 to n, with n is the day since his first time of changing password.
(if n=2, today is 2nd Jan and the password is 3)
-The program will display a random day before 1st Jan 2024
-You will have 4 times to answer.
-You can input exit code "xxx" to exit the rounds
-If you want to exit the game, you just have to say "no" when program display "Do you want to continue?"
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
def rounds():
    while True:
        error="Please input an integer greater than -1, input 0 to start an infinite mode..."
        try:
            ans=input()
            if(ans=="xxx"):
                return "exit"
            ans=int(ans)
            if ans<0:
                print(error)
            elif ans==0:
                return -1
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
history=[]
turns=[]
def quiz():
    n=random.randint(1,1095)
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
    for i in range(1,4):
        p=int(player())
        if p=="exit":
            print("You choose exit...")
            break;
        if p==ans:
            print("😱 🎉 That's a correct answer!!!!!!!!")
            turns.append(i)
            history.append(p)
            break
        else:
            print("Sorry, it's not the correct answer....")
            if(i!=4):
                print(f"You only have {4-i} turn(s) left...")
            else:
                print("😶 Sorry, you're out of turn...")
                history.append("Sadly, you did not have any correct answer in that momment...")
                turns.append(4) 
    return 0
#main 
print("      Password💻🔑")
#print(month(2)) 
if yes_no("Do you want to read an instruction"):
    instruction()
rounds=1
while True:
    print(f"Quizz {1}...")
    quiz()
    if yes_no("Do you want to continue"):
        rounds=rounds+1 
    else:
        break
    
            
            
