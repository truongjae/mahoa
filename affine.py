def encode(t,a1,b1):
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	j=0
	a = []
	for i in t:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				a.append(j)
	#print(a)
	b = []
	for i in a:
		b.append((a1*i+b1)%26)
	#print(b)
	q = []
	for i in b:
		for j in range(len(y)):
			if i == y[j]:
				q.append(x[j])
	# for i in q:
	# 	print(i,end='')
	# print()
	print("Đề: a="+str(a1)+", "+"b="+str(b1)+" : y="+str(a1)+"x+"+str(b1)+" (MOD 26)")
	print("x=x1;x2;:::;x"+str(len(t))+" = "+t)
	print("Ta có: ")
	print("x=x1;x2;:::;x"+str(len(t))+" = "+";".join([str(i) for i in a]))
	print("Mã hóa: ")
	for i in range(0,len(t)):
		print("y"+str(i+1)+"\t = "+str(a1)+"*"+str(a[i])+"+"+str(b1)+" (MOD 26)"+" \t= \t"+str(b[i])+" \t= \t"+q[i])
	print("Vậy y = "+"".join([str(i) for i in q]))


def draw_table(number):
	i=[]
	r=[]
	q=[]
	y=[]
	x=[]
	for k in range(1000):
		i.append(k)
		r.append(k)
		q.append(k)
		y.append(k)
		x.append(k)
	i[0] = 0
	r[0] = 26
	r[1] = int(number)
	x[0] = 1
	y[0] = 0
	x[1] = 0
	y[1] = 1

	temp = []
	t=0
	i=2
	print("i\t\tr\t\tq\t\tx\t\ty")
	print("1\t\t"+str(r[0])+"\t\t\t\t"+str(x[0])+"\t\t"+str(y[0]))
	print("2\t\t"+str(r[1])+"\t\t\t\t"+str(x[1])+"\t\t"+str(y[1]))
	while True:
		r[i] = r[i-2] % r[i-1]
		q[i] = r[i-2] // r[i-1]
		x[i] = x[i-2] - q[i]*x[i-1]
		y[i] = y[i-2] - q[i]*y[i-1]
		temp.append(y[i])
		if r[i] != 0:
			print(str(i)+"\t\t"+str(r[i])+"\t\t"+str(q[i])+"\t\t"+str(x[i])+"\t\t"+str(y[i]))
		if r[i] == 0:
			print(str(i)+"\t\t"+str(r[i])+"\t\t"+str(q[i]))
			t = temp[len(temp)-2]
			break
		i+=1
	key = (t+26)%26
	print("Vậy a^-1= ("+str(t)+"+26)%26 = "+str(key))
	return int(key)
def decode(t,a1,b1):
	temp=draw_table(a1)
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	j=0
	a = []
	for i in t:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				a.append(j)
	#print(a)
	b = []
	for i in a:
		k = (temp*(i-b1)) % 26
		b.append(k)
	#print(b)
	q = []
	for i in b:
		for j in range(len(y)):
			if i == y[j]:
				q.append(x[j])
	print("Đề: a="+str(a1)+", "+"b="+str(b1)+" : y="+str(a1)+"x+"+str(b1)+" (MOD 26)")
	print("y=y1;y2;:::;y"+str(len(t))+" = "+t)
	print("Ta có: ")
	print("y=y1;y2;:::;y"+str(len(t))+" = "+";".join([str(i) for i in a]))
	print("Giải mã: ")
	for i in range(0,len(t)):
		#print("x"+str(i+1)+"\t = "+str(a1)+"*"+str(a[i])+"+"+str(b1)+" (MOD 26)"+" \t= \t"+str(b[i])+" \t= \t"+q[i])
		print("x"+str(i+1)+"\t = a^-1 (y"+str(i+1)+"-b) (MOD 26) = "+ str(a1) + "^-1 (y"+str(i+1) + "-"+str(b1) + ") (MOD 26)")
		print("Với a^-1 = "+str(a1)+"^-1="+str(temp)+" vì "+str(a1)+"*"+str(temp)+"="+ str(a1*temp)+" mà "+str(a1*temp)+" chia 26 = "+str((a1*temp)//26)+" dư 1, có: ")
		print("x"+str(i+1)+"\t = "+str(a1)+"^-1 (y"+str(i+1)+"-"+str(b1)+") (MOD 26) = "+ str(temp)+"*("+str(a[i])+"-"+str(b1)+") (MOD 26) = "+str(b[i])+" = "+ q[i])
		print()
	print("Vậy x = "+"".join([str(i) for i in q]))
encode("VUDUCKIEN",7,3)
decode("UNYNRVHFQ",7,3)