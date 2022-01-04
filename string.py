str1= input("Enter a string 1:")
str2= input("Enter string 2:")
count=0
if len(str1)>len(str2):
    for i in range(len(str2)):
    
        if str1[i]==str2[i]:
            count=count+1
    print(count)
else:
    for i in range(len(str1)):
    
        if str1[i]==str2[i]:
            count=count+1
    print(count)
        
    
    