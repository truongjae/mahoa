def draw_table(number1,number2):
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
	r[0] = int(number2)
	r[1] = int(number1)
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
	if number2 % number1 != 0:
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
		key = (t+number2)%int(number2)
		print("Vậy gcd("+str(number1)+","+str(number2)+")=("+str(t)+"+"+str(number2)+")%"+str(number2)+" = "+str(key))
		return int(key)
	else:
		print(str(i+1)+"\t\t0\t\t"+str(number2//number1))
		print("Vậy gcd("+str(number1)+","+str(number2)+")=(1+"+str(number2)+")%"+str(number2)+" = 1")
		return 1
# print(draw_table(16,160))

def encrypt(p,q,e,m):
	n = p*q
	fiN = (p-1)*(q-1)
	print("Ta có: ")
	print("n=p.q=",n)
	print("fi n = (p-1)(q-1)=",fiN)
	print("gcd (e, fi n)=(",e,fiN,")=1")

	gcd = draw_table(e,fiN)
	d = (gcd+fiN)%fiN
	print("d =",d)

	print("KU = (e,n)=(",e,",",n,")")
	print("KR = (d,n)=(",d,",",n,")")

	print("C= ",m,"^",e,"mod",n)
	print("M= C^",d,"mod",n)

p = int(input("nhập vào p: "))
q = int(input("nhập vào q: "))
e = int(input("nhập vào e: "))
M = int(input("nhập vào M: "))
encrypt(p,q,e,M)