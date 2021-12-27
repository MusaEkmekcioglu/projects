

def binary(decimal):
    result = ""
    while decimal >=1:
        result += str(int(decimal%2))
        decimal -= (decimal/2)
    return result[::-1]
print(binary(17))