y = []
for i in range(100,1000):
	a = i // 100
	o = i % 100
	b = o//10
	c = o%10
	t = a**2 + b**2+ c**2
	while t != 1:
		t = (t//100)**2 + ((t%100)//10)**2 + ((t%100)%10)**2
		if t == 4:
			break
		if t == 5:
			break
		if t == 1 :
			y.append(i)
print(y)
print(len(y))
