n = int(input())

sum = 0
if n >= 1:
    sum = 1 
    for i in range(2,n+1):
        if i%2 != 0:
            sum = sum +i 
print(sum)        
