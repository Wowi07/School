#please 5 credits T_T
import random
def instruction():
  print('''      DON'T POP THE BALLOON🎈
  + Player can choose how many rounds they want to play, or join the infinite mode by enter 0
  + Your point gain per round depends on your streak, many streak ur having, many points you gain on that round( If your streak is 5, if you win that round, you will get 6 points)
  + The game start, you can choose between 1 to 3. These number stand for the times you blow the ballon...
  + Don't blow too much or your balloon will pop. Huy(npc) will play with you, be careful from him, he talk too much tho...
  ''')
def yes_no(question):
  print(question+"?   ")
  while True:
    ans=input().lower()
    if ans=="n" or ans=="no":
      return False
    elif ans=="y" or ans=="yes":
      return True
    else:
      print("You do not input the valid response")
def playing_talk():
  

