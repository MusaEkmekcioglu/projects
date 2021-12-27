def rubiks(cube):    
    leng_c = len(cube)
    full = True
    non_full = False
    missing = True
    full_list = []
    toplam = 0
    for i in cube:
        if len(i) != leng_c:
            full = False
        full_list.append(len(i))
    if len(full_list) == leng_c and len(set(full_list)) > 1:
        missing = True   
    if full and missing:
        return 'Full'
    elif not full and missing:
        if leng_c == max(full_list):
            for i in full_list:
                i = leng_c - i
                toplam += i
            return f'Missing, {toplam}'
        else:
            if len(set(full_list)) != 1:
                for i in full_list:
                    i = max(full_list) - i
                    toplam += i
                return f"This is a {leng_c}X{max(full_list)} Rubik's cube with {toplam} missing."
            else:
                return 'Non-Full'
            
print(rubiks((
  ["O", "O", "O"],
  ["O", "O", "O"],
  ["O", "O", "O"]
)))