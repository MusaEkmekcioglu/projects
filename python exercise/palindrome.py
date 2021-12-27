def min_palindrome_steps(txt):
    if txt == txt[::-1]:
        return 0
    else:
        a = list(txt)
        a = a + [a[0]]
        count = 1
        if a == a[::-1]:
            return count
        else:
            for i in range(1,len(a)):
                count += 1
                a.insert(-i,a[i])
                if a == a[::-1]:
                    break
    return count