#Əksəriyyət Elementini Tapın
a = int(input(""))
b = []
while a!=0:
	c = input("")
	b.append(c)
	a = a - 1
h = len(b)
s = 0
for i in range(h):
	k = b[i]
	e = b.count(k)
	if s<e:
		s = e
		d = k
	else:
		continue
t = h/2
if s > t:
	print(d)
else:
	print("None")