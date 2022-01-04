s1 = "aaabbb"
s2 = "cccddd"

s3 = ""

s2 = s2[::-1]


if len(s1)>len(s2):
    l = len(s1)
else:
    l = len(s2)

for i in range(l):
    if i <len(s1):
        s3 = s3 + s1[i]
    if i <len(s2):
        s3 = s3 +s2[i]
print(s3)