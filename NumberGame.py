win=50
num=int(input("Guess a number between 0 and 100 :"))
if(num==win):
    print("You win!!!!",)
elif(num<win):
    print("Too Low!!!!",)
elif(num>win):
    print("Too High!!!!",)
else:
    print("The winning number is :",win)