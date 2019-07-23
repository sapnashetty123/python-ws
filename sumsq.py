from functools import reduce
lst=[1,2,3,4,5,6,7,8,10]
p=list(map(lambda x:x ** 2,lst))
q=list(filter(lambda x:x % 2==0,p))
lst=reduce(lambda a,b : a+b,q)
print(lst)