howmany_angle=input("triangle or rectangle = ").lower()

if howmany_angle=="triangle":
    
    angle_tri1=int(input("1.angle="))
    angle_tri2=int(input("2.angle="))
    angle_tri3=int(input("3.angle="))
    if angle_tri2==angle_tri1==angle_tri3:
        print("eskenar ucgen")
    elif angle_tri1== angle_tri2 or angle_tri1==angle_tri2 or angle_tri3==angle_tri2:
        print("ikizkenar ucgen")
    elif angle_tri3+angle_tri2<angle_tri1 or angle_tri1+angle_tri3<angle_tri2 or angle_tri1+angle_tri2<angle_tri3:
        print("ucgen olmuyor")
    else:
        print("ssiradan ucgen")
elif howmany_angle=="rectangle":
    rec1=int(input("1.angle="))
    rec2=int(input("2.angle="))
    rec3=int(input("3.angle="))
    rec4=int(input("4.angle="))
    if rec1==rec3==rec2==rec4:
        print("kare")
    else:
        print("siradan dortgen")
else:
    print("yanlis girdiniz..")