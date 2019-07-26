lower = int(input("Enter the lower bound:"))
upper = int(input("Enter the upper bound:"))
for i in range (lower,upper+1):
    if i >1 :
        for j in range (2,i // 2 + 1):
            if i % j == 0:
                break
        else:
            print(i)
    