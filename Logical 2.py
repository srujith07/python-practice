n=eval(input("Enter a number: "))
s=bin(n)
s1=s[2:]
print("The decimal conversion of binary",int(s1))
t=oct(n)
s2=t[2:]
print("The decimal conversion of octal",int(s2))
r=hex(n)
s3=r[2:]
print("The decimal conversion of hexadecimal",int(s3))

