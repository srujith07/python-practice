amt=int(input("Enter your withdraw amount")) # 1800

if amt%100==0:
    if amt>=500:
        a=amt//500 # 1800//500: 3
        amt=amt-(a*500)
        print("500 rupees notes are: ",a)
    if amt>=200:
        b=amt//200
        amt=amt-(b*200)
        print("200 ruppes notes are: ",b)
    if amt>=100:
        c=amt//100
        print("100 ruppes notes are: ",c)

else:
    print("please enter valid amount")