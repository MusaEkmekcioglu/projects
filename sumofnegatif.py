
chars="-12 13%14&-11"
chars = chars.replace('%',' ').replace('&',' ').split(' ')
total = 0
for i in chars:
		if '-' in i:
			i = i.split('-')
			total += sum(list([int(x)*-1 for x in i if x != '']))
		else:
			continue
print(total)

    


def negative_sum(chars):
	chars = chars.replace('%',' ').replace('&',' ').split(' ')
	total = 0
	for eachnum in chars:
		if '-' in eachnum:
			eachnum = eachnum.split('-')
			total += sum(list([int(x)*-1 for x in eachnum if x != '']))
		else:
			continue
	return total
	#return sum(list([int(x) for x in chars if '-' in x]))