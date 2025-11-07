mport math
def gcd (a, b) :
while b:
a, b = b, as b
return a
det subtract_tractions a, b, c, d) :
numerator = a *d - c * b
denominator = b * d
common_divisor = gcd (abs (numerator),
abs (denominator))
return numerator // common_divisor,
denominator // common_divisor
def
find_divisors (n):
divisors = []
for i in range(1, int(math.sqrt(n)) +
1) :
if n % i == 0:
divisors.append (i)
if i* i != n:
divisors.append n // 1)
divisors.sort ()
print(' '•join(map(str, divisors) ))
