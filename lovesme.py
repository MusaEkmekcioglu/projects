def loves_me(n):
	if n%2!=0:
		a= int(((n-1)/2))*("loves me, "+" loves me not, ")
		a=a+"LOVES ME"
		return a
	else:
		a= int(((n-2)/2))*("loves me, "+"loves me not, ")
		a=a+"loves me, "+"LOVES ME NOT"
		return a
print(loves_me(5))