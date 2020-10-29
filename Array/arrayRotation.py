def leftRotate(arr,d,n):
    for i in range(d):
        leftRotateByOne(arr,n)

def leftRotateByOne(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def printArray(arr,size):
    for i in range(size):
        print("% d"% arr[i])



arr = []
n = int(input("enter the size of array: "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
d=int(input("enter the index from where you want to rotate: "))
leftRotate(arr,d,n)
printArray(arr,n)