'''5.	Write a program to print the Fibonacci series up to the number 34. 
(Example: 0,1,1,2,3,5,8,13,… The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)
'''
def fib(num):
    if num < 2:
        return num
    else:
        return (fib(num-1)+fib(num-2))

num=(int(input("Enter the num")))
for i in range(num):
    print(fib(i))

