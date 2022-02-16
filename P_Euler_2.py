

def fibonacci_of(n):
	if n in {0, 1}:
		return n
	return fibonacci_of(n-1)+fibonacci_of(n-2)


a= [fibonacci_of(n) for n in range(34)]

beta = tuple(a)

print(beta)

print(sum([i for i in beta if i % 2 == 0]))

#Technically, I got here -- but I had to have someone show me the method for the fibonacci sequence.
#Also, I had to do guess-and-check to keep the values <4mm

#Python ((From user on p.e.))

s, x, y =  0, 1, 2
while y < 4000000:
   if y % 2 == 0:
      s += y
   x, y = y, x + y
print(s)