num = int(input("Enter the number :"))
temp = num
rev = 0

while num != 0:
    rev = rev * 10 num % 10
    num //= 10

print(f"Reverse of {temp}is {rev}")