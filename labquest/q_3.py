res = int(input("Enter the no:"))
while res > 9:
    res = (res % 10) + (res // 10)
print(res)