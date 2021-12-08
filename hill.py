import numpy
def sum_det(arrx1,arrx2):
	b=len(arrx1)
	sumx=0
	for i in range(b):
		s=1
		for j in range(len(arrx1[i])):
			s*=arrx1[i][j]
		for j in range(len(arrx2[i])):
			s*=arrx2[i][j]
		sumx+=s
	return sumx

def math_det(a):
	b=len(a)
	if b>2:
		#tren duong cheo chinh
		arrx1=[]
		for i in range(b):
			x=[]
			for j in range(i,b):
				x.append(a[j - i][j])
			arrx1.append(x)
		# duoi duong cheo chinh
		arrx2=[]
		for i in range(b):
			x=[]
			for j in range(1,b-i):
				x.append(a[j + i][j - 1])
			arrx2.append(x)
		arrx2=arrx2[::-1]
		# tong x
		sumx = sum_det(arrx1,arrx2)
		#duoi duong cheo phu
		arry1=[]
		for i in range(b):
			x=[]
			for j in range(b-1,i-1,-1):
				x.append(a[b - 1 + i - j][j])
				#print(a[b - 1 + i - j][j])
			arry1.append(x)
		#tren duong cheo phu
		arry2=[]
		for i in range(b-2,-1,-1):
			x=[]
			for j in range(i+1):
				x.append(a[i - j][j])
				#print(a[i - j][j])
			arry2.append(x)
		arry2.append([])
		arry2=arry2[::-1]

		#tong y
		sumy = sum_det(arry1,arry2)

		return sumx-sumy
	else:
		return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def dinh_thuc(a):
	det = numpy.linalg.det(a)
	if det>0:
		if det-int(det)>=0.5:
			return int(det)+1
		else:
			return int(det)
	else:
		if det-int(det)<=-0.5:
			return int(det)-1
		else:
			return int(det)
def nghich_dao(a):
	b=len(a)
	math_det_a=dinh_thuc(a)
	if math_det_a != 0:
		if b > 2:
			xxx=[]
			for i in range(b):
				for j in range(b):
					xx=[]
					for k in range(b):
						x=[]
						for l in range(b):
							if k!=i and l!=j:
								x.append(a[k][l])
						if x != []:
							xx.append(x)
					xxx.append(xx)
			#chuyen vi
			chuyenvi = convert_to_matrix(xxx,b)
			#print(chuyenvi)
			chuyenvi2=[]
			for i in range(b):
				for j in range(b):
					#chuyenvi2.append(dinh_thuc(chuyenvi[i][j])*((-1)**(i+j))/math_det_a)
					chuyenvi2.append(dinh_thuc(chuyenvi[i][j])*((-1)**(i+j)))
			chuyenvi2 = convert_to_matrix(chuyenvi2,b)
			chuyenvi=[]
			for i in range(b):
				for j in range(b):
					chuyenvi.append(chuyenvi2[j][i])
			chuyenvi = convert_to_matrix(chuyenvi,b)
			return chuyenvi
		else:
			return [[a[1][1],a[0][1]*-1],[a[1][0]*-1,a[0][0]]]
	else:
		return None
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
	if r[0] % r[1] != 0:
		while True:
				r[i] = r[i-2] % r[i-1]
				q[i] = r[i-2] // r[i-1]
				x[i] = x[i-2] - q[i]*x[i-1]
				y[i] = y[i-2] - q[i]*y[i-1]
				temp.append(y[i])
				if r[i] != 0:
					print(str(i+1)+"\t\t"+str(r[i])+"\t\t"+str(q[i])+"\t\t"+str(x[i])+"\t\t"+str(y[i]))
				if r[i] == 0:
					print(str(i+1)+"\t\t"+str(r[i])+"\t\t"+str(q[i]))
					t = temp[len(temp)-2]
					break
				i+=1
		key = (t+26)%26
		print("Vậy det(k)^-1= ("+str(t)+"+26)%26 = "+str(key))
		return key
	else:
		key = 1
		print("Vậy det(k)^-1= (1+26)%26 = "+str(key))
		return key
def convert_to_matrix(k,m):
	k1=[]
	matran_k=[]
	for i in range(len(k)):
		k1.append(k[i])
		if (i+1)%m==0:
			matran_k.append(k1)
			k1=[]
	return matran_k
def encode(t,k,m):
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
		print("Với P"+str(i+1)+" =",matran_p[i],"ta có:")
		print("C"+str(i+1)+" =","P"+str(i+1)+" * K =",matran_p[i],"*",matran_k,"=",matran_x3[i],"=",list_matrix[i])
		print()
	print("Vậy bản mã thu được là: ",end="")
	for i in list_matrix:
		for j in i:
			print(j,end="")
	print()
#encode("ANTOAN",[3,3,2,5],2)
#encode("ANHKYEUEM",[3,3,2,5,2,3,5,1,5],3)
#encode("DECODE",[3,3,3,2,5,5,3,5,2],3)
#encode("ANNINHMANG",[3,3,2,7],2)
#encode("BAOMAT",[7,5,2,3],2)
#draw_table(15)
def decode(t,k,m):
	print("Giải mã: ",t)
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
	nghichdao=nghich_dao(matran_k)
	elm=[]
	for i in nghichdao:
		for j in i:
			elm.append(j%26)
	nghichdao=convert_to_matrix(elm,m)
	print("Khóa giải mã là: k^-1 = det(k)^-1 *",nghichdao)
	print("det(k) =",dinh_thuc(matran_k))
	key=draw_table(dinh_thuc(matran_k))
	for i in range(len(elm)):
		elm[i]=(key*elm[i])%26
	matran_key=convert_to_matrix(elm,m)
	print("Vậy k^-1=",key,"*",nghichdao,"=",matran_key)

	matran_k=matran_key
	######
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
		print("Với C"+str(i+1)+" =",matran_p[i],"ta có:")
		print("P"+str(i+1)+" =","C"+str(i+1)+" * K =",matran_p[i],"*",matran_k,"=",matran_x3[i],"=",list_matrix[i])
		print()
	print("Vậy bản giải mã thu được là: ",end="")
	for i in list_matrix:
		for j in i:
			print(j,end="")
	print()
encode("ANNINHMANG",[7, 3, 2, 5],2)
decode("ANDBBWGKZR",[7, 3, 2, 5],2)