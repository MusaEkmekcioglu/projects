
def basamak(n):    
    a = 0    
    while(n != 0):    
        a = a + 1   
        n = n//10    
    return a    
     
number =int( input("bir sayi girin "))    
b = top = 0    
len = basamak(number)    
        
n = number   
    
while(number > 0):    
    b = number%10    
    top = top + int(b**len)    
    number = number//10    
    len = len - 1   
   
if(top == n):    
    print(str(n) + " disarium number")    
else:    
    print(str(n) + " disarium number degil")    
