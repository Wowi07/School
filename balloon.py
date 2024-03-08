#please 5 credits T_T
import random
def instruction():
  print('''      DON'T POP THE BALLOON🎈
  + Player can choose how many rounds they want to play, or join the infinite mode by enter 0
  + Your point gain per round depends on your streak, many streak ur having, many points you gain on that round( If your streak is 5, and if you win that round, you will get 6 points)
  + When the game starts, you can choose a number between 1 to 3. These numbers stand for the times you blow the ballon...
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
talk_win=[]
talk_lose=[]
talk_playing=[]
def playing_talk_win():
    
def playing_talk_lose():
    
def playing_talk_playing():
def game_round():
    input("How many rounds you want to play? (input 0 to join an infinite mode)")
    while True:
        error="Please enter an integer greater than 0, or enter 0 to join an infinite mode"
        try:
            ans=input()
            if(ans=="xxx"):
                return "exit"
            ans=int(ans)
            if(ans>0):
                return ans 
            elif(ans==0):
                return -1
            else:
                print(error)
        except ValueError:
            print(error)
        
#main 
if yes_no("Do you want to read the instruction")
  instruction()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
