n=int(input("enter number"))
d=n//2
p=1
for i in range(2,d):
    if n%i==0:
        print('not prime number')
        p = 0
        break

if p==1:
    print('prime number')

