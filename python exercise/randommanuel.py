number=33
a=True
while a:
    b=int(input("enter a number ="))
    if b>number:
        print("lower")
    elif b<number:
        print("high")
    elif b==number:
        print("correct")
        break    # a=false          break for ve while dan cikarsin 
    else:
        print("again please")
