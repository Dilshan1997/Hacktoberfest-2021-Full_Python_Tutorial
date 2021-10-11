#leanear serching
list_1=[56,8,74,9,23,47,32,15]
x=74
for i in range(len(list_1)):
    if list_1[i]==x:
        print(i)

#Binary search
list_2=[8,87,96,45,47,23]

def binary_search(l,x):
    mid=len(l)//2

    if l[mid]==x:
        return l[mid]
    elif x>l[mid]:
        return binary_search(l[mid: ],x)
    else:
        return binary_search(l[ :mid],x)
result=binary_search(sorted(list_2),87)
print(list_2.index(result))

# Fibonacci Search
from bisect import bisect_left
 
def fibMonaccianSearch(arr, x, n):
 
    fibMMm2 = 0  # (m-2)'th Fibonacci No.
    fibMMm1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci
 
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
 
    offset = -1
 
    while (fibM > 1):
 
        i = min(offset+fibMMm2, n-1)
 
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
 
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
 
        else:
            return i
 
    if(fibMMm1 and arr[n-1] == x):
        return n-1
 
    return -1
 
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100,235]
n = len(arr)
x = 235
ind = fibMonaccianSearch(arr, x, n)
if ind>=0:
  print("Found at index:",ind)
else:
  print(x,"isn't present in the array");
 