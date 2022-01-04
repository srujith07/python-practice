str=input("Enter your string ")
count=1;
words=str.split(" ")
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i]==words[j]:
            count=count+1
            words[j]=None
    if  words[i]!=None:
        print(words[i],",",count)
    count=1