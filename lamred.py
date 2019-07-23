from functools import reduce
lst=[1,2,3]
res = reduce(lambda a,b : a+b, lst)
print(res)