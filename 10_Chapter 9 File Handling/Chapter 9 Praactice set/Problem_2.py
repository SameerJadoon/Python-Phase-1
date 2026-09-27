import random
def game():
    print("You are playing a game.....")
    score=random.randint(1,100)
    with open("Hi_Score.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

    print(f"Your score is :{score}")
    if(score>highscore):
        print(f"Your New High Score is: {score}")
        with open("Hi_Score.txt","w") as f:
            f.write(str(score))
game()