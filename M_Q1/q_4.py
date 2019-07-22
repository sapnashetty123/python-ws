'''4.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/23+1/33+1/43 + ……+1/n3'''
'''def cube_of(num):
    cube = num * num * num
    return cube'''
num=int(input("Enter the number: "))
sum=0
while num != 1:
    sum = sum + ( 1 / (num * num * num) )
    num = num - 1
print(f"the sum of the series is {sum}")