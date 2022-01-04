num=int(input("enter number"))
count=0
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            count=count+1
            
if(count==0):
    print(" not prime")
else:
    print(" prime")