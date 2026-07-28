
# perfect number 
n=int(input("enter n:"))
temp=n
sum=0
for i in range(1,n):
    if temp%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("not")