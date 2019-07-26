inp = int(input("Enter the 5 digit no:"))
n=5
sum=0
res=0
while n!= 0:
    n -=1
    res= inp // 10 ** n
    print(res)
    if res == 9:
        res= 0
    else:
        res +=1
    #print(res)
    inp = inp % 10 ** n
    sum=sum+ res*10 ** n
print(sum)