def BinarySearch(b,c):
    l=0
    u=len(b)-1
    Found= False
    while l<=u and not Found:
       mid = (l+u)//2
       if c == b[mid]:
           Found = True
       elif c>b[mid]:
           l = mid + 1
       else:
           u = mid - 1
    if Found == True:
       print("Number Found")
    else:
       print("Number Not Found")

print("Enter Random Number List")
a=input()
n=a.split(",")
n.sort()
b= [int(i) for i in n]
print(b)
print("Number You want to search")
c= int(input())



BinarySearch(b,c)


