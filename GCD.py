m = int(input())
n = int(input())
g = 1
if m > n :
    b = m 
else :
    b = n 
for i in range(1,b+1):
    
    if m%i == 0 and n%i == 0:

        if i > g:
            g = i
print(g)    
       
        
