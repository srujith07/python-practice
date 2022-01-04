m = int(input())
n = int(input())

if m > n:
    b = m 
else:
    b = n 
s = []    
for i in range(2,b**2):
    if i%n == 0 and i%m == 0:
        print(i)
        break
