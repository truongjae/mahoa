def encode(t,m):
	t = t.upper()
	m = m.upper()
	print("Mã hóa: ",t)
	print("key: ",m)
	print("m =",len(m))
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	j=0
	a = []
	for i in t:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				a.append(j)
	print(t,": ",a)
	b=[]
	for i in m:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				b.append(j)
	print(m,": ",b)
	c=[]
	temp=0
	for i in range(len(a)):
		if i%len(b)==0:
			temp=0
		z = a[i]+b[temp]
		if z>=26:
			z=z%26
		c.append(z)
		temp+=1
	#print(c)
	key = []
	for i in c:
		for j in range(len(y)):
			if i == y[j]:
				key.append(x[j])
	for i in a:
		print(i,"\t\t",end="")
	print()
	tmp = 0
	for i in range(len(a)):
		if tmp==len(b):
			tmp=0
		print(b[tmp],"\t\t",end="")
		tmp+=1
	print()
	for i in c:
		print(i,"\t\t",end="")
	print()
	print("".join(key))



def decode(t,m):
	t= t.upper()
	m = m.upper()
	print("Giải mã: ",t)
	print("key: ",m)
	print("m =",len(m))
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	j=0
	a = []
	for i in t:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				a.append(j)
	print(t,": ",a)
	b=[]
	for i in m:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				b.append(j)
	print(m,": ",b)
	c=[]
	temp=0
	for i in range(len(a)):
		if i%len(b)==0:
			temp=0
		z = a[i]-b[temp]
		if z<0:
			z=z+26
		c.append(z)
		temp+=1
	print(c)
	key = []
	for i in c:
		for j in range(len(y)):
			if i == y[j]:
				key.append(x[j])
	for i in a:
		print(i,"\t\t",end="")
	print()
	tmp = 0
	for i in range(len(a)):
		if tmp==len(b):
			tmp=0
		print(b[tmp],"\t\t",end="")
		tmp+=1
	print()
	for i in c:
		print(i,"\t\t",end="")
	print()
	print("".join(key))
print("1. mã hóa")
print("2. giải mã")
print("bản quyền thuộc về thầy trường buff bẩn")
choice = input("nhập lựa chọn: ")
if choice == "1":
	code = input("nhập vào chuỗi cần mã hóa: ")
	a = input("nhập vào key: ")
	encode(code,a)
elif choice == "2":
	code = input("nhập vào chuỗi cần giải mã: ")
	a = input("nhập vào key: ")
	decode(code,a)
else:
	print("lựa chọn không chính xác")
input("enter để thoát!")