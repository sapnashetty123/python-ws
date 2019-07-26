inp = int(input("Enter the no:"))
def fact_no(num):
    if num <= 1:
        return num
    else:
        fact = num*fact_no(num - 1)
    return fact
f= fact_no(inp)
print(f)
