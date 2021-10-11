# Euclid's algorithm to find the greatest common divisor
def gcd(m, n):
	if m == n :
		res = m

	elif m > n :
		res = gcd(m -n, n)
		# 3 
		# 4
	else:
		res = gcd(m, n - m)
		# 2 
		# 5
	return res
a=round(float(input('Enter first number=')))
b=int(input('Enter second number='))
print("gcd : ", gcd(a,b))

# 1. gcd(65, 91)
# 2. gcd(65, 26)
# 3. gcd(39, 26)
# 4. gcd(13, 26)
# 5. gcd(13, 13)