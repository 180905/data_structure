def reverseArray(arr,start,end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
def leftRotate(arr):
    if d==0:
        return
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1)
# function to print array
def printArray(arr):
    for i in range(0,n):
        print arr[i]



arr = []
n = int(input("enter the size of array: "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
d=int(input("enter the index from where you want to rotate: "))
leftRotate(arr)
printArray(arr)
