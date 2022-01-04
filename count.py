def countW(s):
    s1=s.split()
    word=0
    for i in s1:
        word=word+1
    print('word:',word)
    #print(word+1)

countW("hi hellow good hi")