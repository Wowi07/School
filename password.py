def instruction():
    print('''This program can generate the quiz 
        This is the problem...
-Huy created his laptop's password and made it changes everyday. 
-His first time of changing password is in 31th December 2020.
-The password today is the sum of a list of number from 0 to n, with n is the day since his first time of changing password.(if n=2, today is 2nd Jan and the password is 3)
-The program will display a random day before 1st Jan 2024
-Your mission is input the password of his laptop on that day, goodluck....
''')
print("      Password💻🔑")
import random
def year(n):
    return int(n/356)
def month(n):
    if n==2:
        return 28
    elif (n%2!=0 and n<8) or (n%2==0 and n>=8):
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
    ans=input()
    while True:
        try:
            if(ans=="xxx"):
                return "exit"
            ans=int(ans)
            return ans 
        except ValueError:
            print("Please input a valid response...")
def quiz():
    n=random.randint(1,1095)
    ##count the years
    years=year(n)
    n=n-years*356
    month=1
    #count the month
    for i in range(1,13):
        temp=int(month(i))
        if n<i:
            break;
        else:
            n=n-temp
            month=month+1
    ans=((n+1)*n)/2
    print(f"What is the password in {n} {month_change(month)} {years+2021}?  ",end="")
    p=int(player())
    for i in range(1,4):
        if p==ans:
            print("😱 🎉 That's a correct answer!!!!!!!!")
        else:
            print("Sorry, it's not the correct answer....")
            print(f"You only have {})
