str="Hi hello bitLabs hi hello hi hi hello welcome to bitLabs".lower()

words=str.split(" ")
count=0;

l=len(words)

for i in words:
    for j in range(len(words)):
        if i==words[j]:
            count=count+1
            words[j]=" "
    if(i!=' '):
        d=(count/l)*100
        print(i,": Density: ",d)
#print(i," : ",count)
    count=0