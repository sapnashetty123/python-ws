def searchLinear(lst,ele):
    index=0
    for i in lst:
        if i ==ele:
            return index
        index +=1

    return -1
def bubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

l = [3,4,5,6,2]
bubbleSort(l)
print(l)

def binarySearch(lst,key):
    l=0
    h=len(lst)-1
    while l<=h:
        mid = (l +h ) //2
        if lst[mid] ==key:
            return mid
        elif lst[mid] > key:
            h=mid -1
        else:
            l=mid +1
    return -1





ele=int(input("enter ele to search:"))
res = binarySearch([1,2,3,4,5,6,7,8],ele)   #res = searchLinear([1,2,3,4,5,6,7,8],ele) 
if res ==-1:
    print("elem not found")
else:
    print(f"{ele} found at {res}")
