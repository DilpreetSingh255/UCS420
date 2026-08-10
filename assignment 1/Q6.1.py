def IsPrime(n):
	for i in range(2, n//2 + 1):
		if n%i==0:
			return 0
	return 1

print ( IsPrime(20))
print ( IsPrime(23))
print ( IsPrime(200))
print (IsPrime(37))