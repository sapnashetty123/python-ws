'''1.	Write a program to accept a number and determine whether it is a prime number or not.'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
num=int(input("enter the number:"))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
        
