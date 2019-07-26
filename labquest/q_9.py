def prime(num):
    if num <2:
        return False
    for i in range (2,num // 2 + 1):
        if num % i == 0:
            return False
    return True

inp=int(input("enter the no:"))
c=0
while inp != 0:
    if prime(inp%10):
        c+=1
    inp=inp //10
print(c)
            