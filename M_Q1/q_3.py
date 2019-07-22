'''3.	Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.'''
def is_prime(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

for num in range(num1,num2+1):
    if is_prime(num):
        print(f"{num}")