#return true or false depend on an answer
def yes_no(question):
    while True:
        player=input(question+'  ').lower()
        if player=='yes' or player=='y':
            return True
        if player=='no' or player=='n':
            return False
        else:
            print('You did not choose a valid response')
#check does the input is value(int, >13)
def check_int():
    while True:
        try:
            error="Please enter an integer that is 13 or more."
            num=int(input("Please enter your number: "))
            if(num<13):
                print(error)
            else:
                return num
        except ValueError:
            print(error)

#main 
instruction()
target_score = check_int()



