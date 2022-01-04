import math
num=int(input("Enter a number1: "))
num1=int(input("Enter a number2: "))
for n in range(num,num1):
    i=n
    sum=0
    while(i>0):
        r=i%10
        f=math.factorial(r)
        sum=sum+f
        i=i//10
    if sum==n:
        print(n)
    