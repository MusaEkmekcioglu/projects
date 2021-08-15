
liste = [-1, 2, -3, 5, 7, 8, 9, -10]
list1 = list(filter(lambda x : x > 0, liste))
list2 = list(sorted(list(filter(lambda x : x < 0, liste))))
list1.extend(list2)
print(list1)