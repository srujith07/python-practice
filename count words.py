str=input("Enter string ") # hi@3 hello nagul
words=str.split(" ") # hi -2 hello-5 nagul-5
count=0
for word in words:
    for ch in word:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            count=count+1
    print(word," : ",count)
    count=0