# WAP to read 3 subjects: project score, internal score , external score.
# if student got passed in project,internal and external then find total score.
# pass marks : 50
# total= 70% from project+ 20% external + 10% internal
# print grade A: 90+ B :75-90 C: 50-75
# print fail along with subject score.

project=int(input("Enter project score"))
external=int(input("Enter External score"))
internal=int(input("Enter internal score"))

if project>=50 and external>=50 and internal>=50:
    total=(70/100)*project+ (20/100)*external+(10/100)*internal
    print("Total score: ",total)
    if total>=90:
        print("A grade")
    elif total>=75:
        print("B grade")
    else:
        print("C grade")
else:
    if project<50:
        print("failed in project and the score is: ",project)
    if external<50:
        print("failed in external and the score is: ",external)
    if internal<50:
        print("failed in internal and the score is: ",internal)