'''2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1+ 1/2 + 1/3 + …….+ 1/n'''
num=int(input(" enter the number: "))
sum = 1
while num != 1:
    sum = sum + (1 / num)
    num = num - 1
print(f"the sum of the series is {sum}")