def big(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    else:
        if num2>num3:
            return num2
        else:
            return num3

n1=int(input("enter the num:"))
n2=int(input("enter the num:"))
n3=int(input("enter the num:"))
res=big(n1,n2,n3)
print(f"biggest no is {res}")