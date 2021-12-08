def encode():
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	t = "ANNINHMANG"
	j=0
	k=16
	a = []
	for i in t:
		for j in range(len(x)):
			if i == x[j]:
				a.append(j)
	print(a)
	b = []
	for i in a:
		b.append((i+k)%26)
	print(b)
	q = []
	for i in b:
		for j in range(len(y)):
			if i == y[j]:
				q.append(x[j])
	for i in q:
		print(i,end='')
	print()
def encode2(t,k):
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
		b.append((i+k)%26)
	#print(b)
	q = []
	for i in b:
		for j in range(len(y)):
			if i == y[j]:
				q.append(x[j])
	# for i in q:
	# 	print(i,end='')
	#print()
	print("x=x1;x2;:::;x"+str(len(t))+" = "+t)
	print("Ta có: ")
	print("x=x1;x2;:::;x"+str(len(t))+" = "+";".join([str(i) for i in a]))
	print("Mã hóa: ")
	for i in range(0,len(t)):
		print("y"+str(i+1)+" = (x"+str(i+1)+"+k) MOD 26 = "+"("+str(a[i])+"+"+str(k)+") MOD 26\t = "+str((a[i]+k)%26)+" = "+q[i])
	print("Vậy y = "+"".join([str(i) for i in q]))
encode2("CONGNGHETHONGTIN",15)
def encode3(t,a1,b1):
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
#encode3("ANTOANBAOMAT",3,5)



def draw_table(number):
	i= []
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
def decode3(t,a1,b1):
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
		#b.append(((i-b1)//a1%26))

		k = (temp*(i-b1)) % 26
		b.append(k)
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
	print("y=y1;y2;:::;y"+str(len(t))+" = "+t)
	print("Ta có: ")
	print("y=y1;y2;:::;y"+str(len(t))+" = "+";".join([str(i) for i in a]))
	print("Giải mã: ")
	for i in range(0,len(t)):
		#print("x"+str(i+1)+"\t = "+str(a1)+"*"+str(a[i])+"+"+str(b1)+" (MOD 26)"+" \t= \t"+str(b[i])+" \t= \t"+q[i])
		print("x"+str(i+1)+"\t = a^-1 (y"+str(i+1)+"-b) (MOD 26) = "+ str(a1) + "^-1 (y"+str(i+1) + "-"+str(b1) + ") (MOD 26)")
		print("Với a^-1 = "+str(a1)+"^-1="+str(temp)+" vì "+str(a1)+"*"+str(temp)+"="+ str(a1*temp)+" mà "+str(a1*temp)+" chia 26 = "+str((a1*temp)//26)+" dư 1, có: ")
		print("x"+str(i+1)+"\t = "+str(a1)+"^-1 (y"+str(i+1)+"-"+str(b1)+") (MOD 26) = "+ str(temp)+"*("+str(a[i])+"-"+str(b1)+") (MOD 26) = "+ str(b[i])+" = "+ q[i])
		print()
	print("Vậy x = "+"".join([str(i) for i in q]))
#decode3("FSKVFSIFVPFK",3,5)



def encode4(t,m):
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
#encode4("ANTOANTHONGTIN","SECURE")
# encode4("HOTENSINHVIEN","BAOMAT")
# encode4("CONGNGHETHONGTIN","MAHOA")


def decode4(t,m):
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
#decode4("SRVIRRLLQHXXAR","SECURE")

def convert_to_matrix(k,m):
	k1=[]
	matran_k=[]
	for i in range(len(k)):
		k1.append(k[i])
		if (i+1)%m==0:
			matran_k.append(k1)
			k1=[]
	return matran_k
def encode_hill(t,k,m):
	print("Mã hóa: ",t)
	print("m =",m)
	matran_k=convert_to_matrix(k,m)
	print("k =",matran_k)
	x = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	y = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	j=0
	a = []
	for i in t:
		for j in range(len(x)):
			if i.upper() == x[j].upper():
				a.append(j)
	matran_p=convert_to_matrix(a,m)
	print(t,"=",matran_p)
	print()
	matran_x = []
	for i in range(len(matran_p)):
			for j in range(m):
				s=0
				for k in range(m):
					s+= matran_p[i][k]*matran_k[k][j]
				matran_x.append(s)
	matran_x2=[]
	for i in matran_x:
		k=i
		if i >=26:
			k = i%26
		matran_x2.append(k)
	matran_x3 = convert_to_matrix(matran_x2,m)
	#print(matran_x2)
	list_matrix=[]
	for i in range(len(matran_p)):
		list_key = []
		for j in range(len(matran_x3[i])):
			for k in range(len(y)):
				if matran_x3[i][j] == y[k]:
					list_key.append(x[k])
		list_matrix.append(list_key)
		print("Với P",i+1,"=",matran_p[i],"ta có:")
		print("C",i+1,"=","P",i+1,"* K =",matran_p[i],"*",matran_k,"=",matran_x3[i],"=",list_matrix[i])
		print()
	print("Vậy bản mã thu được là: ",end="")
	for i in list_matrix:
		for j in i:
			print(j,end="")
	print()
encode_hill("ANTOAN",[3,3,2,5],2)
