n = int(input())

for i in range(n):
    for a in range(i,n-1):
        print("0", end = " ")
    for a in range(i+1):
        print("1", end = " ") 
    for a in range(i):
        print("1", end = " ")
    for a in range(i,n-1):
        print("0", end = " ")    
    print
