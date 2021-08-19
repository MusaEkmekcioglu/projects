def function(n):
    return lambda x: x+ ":" +n

sad=function("(")
smile=function(")")
notr=function("|")
print(sad("Hello"))