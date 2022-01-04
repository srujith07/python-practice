def factors():
    num=int(input('enter the number'))
    for i in range(1,num):
        if(num%i==0):
            print( i)
factors()
        
