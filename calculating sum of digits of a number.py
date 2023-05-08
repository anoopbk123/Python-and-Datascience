n=int(input('enter the phone number'))
i=0
sum=0
while i<10:
    r=n%10
    sum+=r
    n=n//10
    i+=1
print('sum of digits\t',sum)