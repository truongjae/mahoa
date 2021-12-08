def convert_to_binary(n):
	if n!=0:
		string=""
	else:
		string="0"
	while n>0:
		string+=str(n%2)
		n//=2
	return int(string[::-1])
def convert_to_decimal(n):
	i=0
	result = 0
	while n!=0:
		temp = n%10
		if temp==1:
			result+=(2**i)
		#print(i)
		n//=10
		i+=1
	return result
def sum_binary(a,b):
	s = ""
	for i in range(len(a)):
		if a[i] != b[i]:
			s += "1"
		else:
			s += "0"
	return s
def encode(plaintext,key):
	print("Hàm mã hóa:")
	result=""
	j=1
	for i in plaintext:
		x = ord(i)
		binary = str(convert_to_binary(x))
		en=sum_binary(binary,key)
		en_to_binary = chr(convert_to_decimal(int(en)))
		result+=en_to_binary
		print("plaintext x"+str(j)+": "+i+" = "+binary)
		print("key stream z"+str(j)+": "+key)
		print("ciphertext y"+str(j)+": "+en+" = "+str(en_to_binary))
		print()
		j+=1
	print("Bản mã thu được là : "+result)
def decode(plaintext,key):
	print("Hàm giải mã:")
	result=""
	j=1
	for i in plaintext:
		x = ord(i)
		binary = str(convert_to_binary(x))
		en=sum_binary(binary,key)
		en_to_binary = chr(convert_to_decimal(int(en)))
		result+=en_to_binary
		print("ciphertext y"+str(j)+": "+i+" = "+binary)
		print("key stream z"+str(j)+": "+key)
		print("plaintext x"+str(j)+": "+en+" = "+str(en_to_binary))
		print()
		j+=1
	print("Bản giải mã thu được là : "+result)
encode("MAHOADULIEU","1010110")
#decode("","1010110")