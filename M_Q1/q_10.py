'''10.	Write a program to print the following output pattern.
         1
        121
       12321
      1234321
     123454321'''
max = 6
for i in range(1, max + 1):
    for j in range(max,i-1,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(k-1,0,-1):
        print(l,end=" ")
    print()


    