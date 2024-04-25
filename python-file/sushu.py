def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True


s=int(input())
x=int(input())
sum=0
y=[]
for m in range(s,x+1):
    if m==1:
        continue
    if sushu(m)==True:
        sum=sum+1
        y.append(m)
print(y)
print(f"素数一共{sum}个")


