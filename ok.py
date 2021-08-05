def text(text):
    flag=True
    
    for i in range(len(text)):
        if "(" in text:
            if ")" in text:
                flag= True
                
            else:
                flag= False
        if "{" in text:
            if "}" in text:
                flag= True
            else:
                flag= False
        if "[" in text:
            if "]" in text:
                flag= True
            else:
                flag= False
        else:
            flag= False
    return flag

print(text("([)"))