x = y = 0
C = ["right 20", "right 30", "left 50", "up 10", "down 20"]
for i in range(len(C)) :
    if C[i].startswith("r") : x = x + int(C[i].split()[1])
    elif C[i].startswith("l") : x = x - int(C[i].split()[1])
    elif C[i].startswith("u") : y = y + int(C[i].split()[1])
    elif C[i].startswith("d") : y = y - int(C[i].split()[1])
        
print([x, y])