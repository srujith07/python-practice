n = int(input())
c =0
for i in range(1,n+1):
    div = 0
    
    for j in range(2,11):
        if i % j == 0:
            div = div+1 
    if div == 0:
        c = c+1 
print(c)        
