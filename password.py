def instruction():
    print('''
        This is the problem...
-Huy's just bought a new laptop ASUS TUF GAMING A15. To make sure, he created his laptop ASUS TUF GAMING A15's password
and made it change everyday. 
-His first time of changing his password is in 31th December 2020.
-The password today is the sum of a list of numbers from 0 to n, with n is the day since his first time of changing password.
(if n=2, today is 2nd Jan 2021 and the password is 3)
-The program will display a random day from 1st January 2021 to 31th December 2023 
-First of all, you can pick the number of rounds you want to play or play "solve_til_out_of_problem"(STOOP) mode by input 0
-You will have 3 turns to answer.
-You can input the exit code "xxx" to exit the rounds
-Your mission is input the password of his laptop on that day, good luck....
''')


def yes_no(question):
    print(question + "?  ")
    while True:
        r = input().lower()
        if r == "y" or r == "yes":
            return True
        elif r == "n" or r == "no":
            return False
        else:
            print("You did not choose the valid response")


def how_many_rounds():
    while True:
        error = "Please input an integer greater than -1 and lesser than 1951, input 0 to start a STOOP mode..."
        try:
            ans = input()
            if (ans == "xxx"):
                return "exit"
            ans = int(ans)
            if ans < 0 or ans>1950:
                print(error)
                continue
            elif ans == 0:
                print("You choose STOOP mode")
                return 1096
            else:
                return ans
            return ans
        except ValueError:
            print(error)


# how many years in n day(s)
def how_many_years(n):
    return int(n / 365)


# return how many days on that month
def months(m):
    m = int(m)
    if m == 2:
        return 28
    elif (m % 2 != 0 and m < 8) or (m % 2 == 0 and m >= 8):
        return 31
    else:
        return 30





# control the input of player
def player():
    while True:
        ans = input()
        try:
            if (ans == "xxx"):
                return "exit"
            ans = int(ans)
            return ans
        except ValueError:
            print("Please input a valid response...")


history = []  # history save the result of each round
turns = []  # turns let me know how many times they need to give the right answer
quiz_content = []  # quiz_content save the content of quiz each round(for example: 1st September 2022,...)
round_win = 0  # count how many round player won
sum_guesses_used = 0  # count how many turn player used in whole game
dup_quiz = []  # save all the question to prevent program from generate the same quiz
# change the month from number to string form
months_in_word=["???","January","February","March","April","May","June","July","August","September","October","November","December"]
# each round
def quiz(n):
    dup = []  # this dup created to prevent player from input the same answer in a particular round
    # print(n)
    #initial_quiz is the variable which save the initial number of days on single a round
    initial_quiz = int(n)
    years = how_many_years(n)  # count the years
    n = n - years * 365  # subtract the days on "years" years
    month = 1  # initial month is 1, to make it easier to count the month
    # count the month
    for i in range(1, 13):
        if n == 0 and i==1:
            month = 12
            years = years - 1
            n=31
            break
        temp = months(i)
        if n < temp:
            break
        else:
            n = n - temp
            month = month + 1
        if n==0:
            n=n+temp 
            month=month-1
            break
    # calculate the consecutive list(1 to n). This is the right answer
    ans = int(((initial_quiz + 1) * initial_quiz) / 2)
    # print(ans)
    # these line just adding the st,nd,rd or th to the day
    if n==11:
        n = str(n) + "th"
    elif n == 12:  
        n = str(n) + "th"
    elif n == 13:  
        n = str(n) + "th"
    elif n % 10 == 1:   # btw, i used %10 to take the last number of n
        n = str(n) + "st"
    elif n % 10 == 2:
        n = str(n) + "nd"
    elif n % 10 == 3:
        n = str(n) + "rd"
    else:
        n = str(n) + "th"
    # display the question
    print(f"What is the password in {n} " + months_in_word[month] + f" {years + 2021}?  ", end="")
    # add the question into quiz_content, to print it then in the history
    quiz_content.append(n + " " + months_in_word[month] + " " + str(years + 2021))
    # range (1,4) which mean 1 to 3. So player has 3 times to answer
    for i in range(1, 4):
        # i had to use the loop to make sure that player input the valid value

        #this loop make sure that player input a valid answer
        while True:
            p = player()
            if p == "exit":
                print("You choose exit...")
                return "exit"
            # this condition mean if player had already answered that number
            if p in dup:
                print("You'd already input this answer...")
            else:  # this else mean if player has a valid input(no duplicated ans), im going to break this loop
                p = int(p)
                dup.append(p)
                break

        # correct condition
        if p == ans:  
            print("😱 🎉 That's a correct answer!!!!!!!!" + "\n" * 3)
            turns.append(i)  # save the turns player used on this round
            # save the result to display then in history
            history.append(
                f"You guessed the right answer in that round with {i} time(s) of guessing" + "   The answer is " + str(
                    ans))
            # return how many turn player used to adding to sum_guesses_used
            return i
        else:  # this else mean if player gave the wrong answer
            print("Sorry, it's not the correct answer....")
            if (i != 3):  # only display the turn left if it's !=0
                print(f"You only have {3 - i} turn(s) left...")  # display how many turn left
            else:  # if player give a wrong answer and out of turn
                print("😶 Sorry, you're out of turns...")
                print("The answer is " + str(ans) + "\n" * 3)
                history.append(
                    "Sadly, you did not have the correct answer in that moment..." + "    The answer is " + str(ans))
                turns.append(3)
                return 4  # i return 4 instead of 3 bc i need to mark if player lose this round

# main
print("      Password💻🔑")
# print(month(2))
if yes_no("Do you want to read the instructions"):
    instruction()
rounds_played = 0  # this variable was created to mark how many rounds_played player played
print("How many rounds do you want to play?(input 0 to start a STOOP mode) ", end="")
# round_left just the variable to count how many round left till it reach 0
round_left = how_many_rounds()
STOOP = ""
# playy is that variable to mark that they exit and dont want to play any round
playy = True
#exit condition
if (round_left == "exit"):
    print("You choose exit")
    playy = False
#STOOP mode condition
if(round_left==1096):
    STOOP="(STOOP MODE)"
    round_left=1095
#game on =)))
if playy:  # only play when player didn't want to exit in above input
    while round_left != 0:  # i'll minus the round_left by 1 every round til it reach 0
        print(f"Quizz {rounds_played + 1} "+STOOP)
        # avoid from duplicate the quiz
        import random
        while True:
            n = random.randint(1, 1095)
            if n in dup_quiz:
                continue
            dup_quiz.append(n)
            break
        round_result = quiz(n)
        if round_result == 4:  # if player lost
            rounds_played = rounds_played + 1
            round_left = round_left - 1  # i only +1 to rounds_played here because sometimes, player can exit in above line,
            # so if I +1 too early, i will get the wrong output bc player didnt play that round
            sum_guesses_used = sum_guesses_used + int(round_result) - 1  # i'll add how many turn they used
        elif round_result == "exit":
            break  # break to exit and go straight to history and Statistics
        else:  # if player win
            sum_guesses_used = sum_guesses_used + int(round_result)  # i'll add how many turn they used
            rounds_played = rounds_played + 1
            round_left = round_left - 1
            round_win = round_win + 1  # i'll +1 to round_win to mark that they have 1 more win.

if rounds_played != 0:  # i only display the history and Statistics if player'd alr played at least 1 round
    #History
    if yes_no("Do you want to see your history"):
        for i in range(1, rounds_played + 1):  # i is also stand for the current round i want to print
            print("🕰️🕰 Game history 🕰🕰️")
            print(f"Round {i}" + "\n" + f"The quiz is what is that password in {quiz_content[i - 1]}: ")
            # i had to print quiz_content[i-1] instead of quiz_content[i] bc i my start-value in position 0
            print(history[i - 1])
    #Stat
    print("📊📊 Game Statistics 📊📊")
    print(f"You played {rounds_played} round(s)")
    print(
        f"You won {round_win} round(s)🎉, {int((round_win * 100) / rounds_played)}%  ||  You used about {int(sum_guesses_used / rounds_played)} turn(s) to guess per round")
    
#this condition mean if player did not play any round   
else:
    print("You did not play any round...")
