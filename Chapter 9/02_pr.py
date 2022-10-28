# here we will add a high score in a text file. 
def game():
    return 455
s=game()
with open("highscore.txt","r") as f:
     d=f.read(s)
print("previous high score:",d)

if d=='':
    f=open('highscore.txt','w')
    hs=f.write(str(s))
    print(int(hs))    
elif int(d)<s:
    f=open('highscore.txt','w')
    hs=f.write(str(s))
    print("New high score is",s)  
elif int(d)>s:
    print("Your score is less than  previous high score....")
elif int(d)==s:
    print("previous High score is equal to new score....")
f.close()

