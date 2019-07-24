'''7.	Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.'''



def add(num):
    sum=0
    while num !=0:
        rem=num % 10
        num = num // 10
        sum = sum + rem
    return sum
num=int(input("Enter the number:"))

res=add(num)
while res > 10:
    res=add(res)
   
print(res)

