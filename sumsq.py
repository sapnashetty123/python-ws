names=["p","a","pv","p","a","g","n","pv","k","v","m"]
c={}

for i in names:
    if i in c:
        c[i] +=1
    else:
        c[i]=1
print(c)
