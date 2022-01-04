def product():
    num=int(input("Enter a number :"))
    pro=1
    while(num!=0):
        rem=num%10
        pro=pro*rem;
        num=num//10
    print(pro)
    
product()