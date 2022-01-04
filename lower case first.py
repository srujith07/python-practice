s = str(input())
ns = ""
l = []
u =[]
for i in s:
    if i.islower():
        l.append(i)
    if i.isupper():
        u.append(i)


for i in l:
    ns = ns+i 


for i in u:
    ns = ns+i
print(ns)