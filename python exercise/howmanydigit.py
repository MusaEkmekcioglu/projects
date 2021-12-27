def length_string(number):
    result = 0
    if number == 0 or number == 1:
        return 0
    else:
        for i in range(1, number):
            index = len(str(i))
            result += index
        return result

print(length_string(2020))




def ndigit(n):
    result = 0
    for i in range(1, n):
        count = 0
        while i!=0:
            i//=10
            count+=1
        result+=count
    return result
print(ndigit(2020))


