"""
age=33
a=True
while a:
    b=int(input("enter a age ="))
    if age==b:
        print("yasiniz dogry")
        a=False
    else:
        print("dogru degil tekrar gir ")
"""
##############################################3

age =input("enter a age=")
while not age.isdigit():                                        #isdigit boolean turned/// age de digitten mi olusuyor ?
    print("you entered incorrect. write out correct format ")
    age =input("enter a age=")