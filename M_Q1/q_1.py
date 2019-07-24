'''1.	Write a program to accept a number and determine whether it is a prime number or not.'''
num=int(input("enter the number:"))
if num < 2:
    print(f"{num} is not prime")
else:
    for i in range (2,num // 2 +1):
        if num % i == 0:
            print(f"{num} is not a prime no")
            break
    else:
        print(f"{num} is prime")
        
