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
print(convert_to_binary(3))