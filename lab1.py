def fib_sum(n, k) :

fib = 0, 1]

while len (fib) < k + n:

fib.append (fib[-1] + fib[-2])

return sum (fib k-1:k+n-1])

n = int(input())

k = int(input())

I print (fib_sum(n, k))
