def turn(player?):
  s1=randnum()
  s2=randnum()
  dbscore=False
  if s1==s2:
    dbscore=True
  sum=s1+s2
  if(player?==True):
    print(f"You rolled {s1} and {s2}, your total score is {sum}")
    while True:
      if(yes_no("Do you want to continue rolling the dice? ")):
        temp=randnum()
        sum=sum+temp
        print("\n"+"\n"+f"You rolled {temp}"+"\n"+f"Your total score is now {sum}")
    else:
      return sum , dbscore
  #computer game play
  else:
  #roll until>=10
    while True:
      if sum<9:
        temp=randnum()
        sum=sum+temp
      else:
        return sum
  
