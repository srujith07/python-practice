n = input()

if n.isupper():
    print("Uppercase Letter")
elif n.islower():
    print("Lowercase Letter") 
elif n.isdigit():
    print("Digit")
else:
    print("Special Character")