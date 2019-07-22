import random as rn
guess=rn.randint(1,6)
n=1
while n<=3:
    in_it=int(input("enter:"))
    if guess==in_it:
        print(f"guessed in {n} try")
        break
    elif in_it<guess:
        print("generated no is greater")
    else:
        print("generated no is less")
    n+=1
if n==4:
    print("better luck next time"