n = int(input())
m = int(input())
sum = 0
c = 0

for i in range(n,m+1):
    num = i

    i = str(i)
    l = len(i)
    for a in range(l):
        
        sum = sum + int(i[a])**l 
     
        
        
    if num == sum:
        c = c+1
        print(num,end = " ")
            
    sum = 0
if c == 0:
    print(-1)
        
