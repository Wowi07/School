def game_play():
  s1=randnum()
  s2=randnum()
  dbscore=False
  if s1==s2:
    dbscore=True
  sum=s1+s2
  while True:
    if(yes_no("Do you want to continue rolling the dice? "):
      sum=sum+randnum()
    else:
      return sum , dbscore
