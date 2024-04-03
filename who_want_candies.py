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
