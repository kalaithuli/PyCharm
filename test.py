n=int(input("number: "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
print(s)
if s == n:
    print("Perfect")