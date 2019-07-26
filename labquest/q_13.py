def sum_no(ls):
    sum=0
    for i in ls:
        sum=sum+i
    return sum
lst=[1,2,3,4]
sum=sum_no(lst)
print(f"The sum of {lst} is:{sum}")