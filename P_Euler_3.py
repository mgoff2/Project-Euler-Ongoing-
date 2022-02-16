
#Question = What is the largest prime factor of 600851475143?


def factors(b):
	for i in range(1, b+1):
		if b % i == 0:
			print(i)

a = 600851475143


#This appears to be working, but it's awfully rough on my CPU...


c=int(a/71)
print(c)

#factors(c)
d = int(c/839)
print(d)

factors(10086647)

factors(6857)

#Since I knew 71 was a factor, I figured I could reduce the burden by dividing by the
#smallest known factor. 
#^Note that I had to indicate "int" in the definition of c so that I could perform 
#arithmetic operations. 

#factors(a)
#This is still chewing up my computer. 

#KK originally I had the range starting at 1, but since we are obviously not looking for a 
#small number, I'm upping it quite a bit. 


#The new approach certainly cut down the computing time, but it's not exactly speedy rn.
#Began at 100 million, but the figure is 600 billion, so I'm going to go up again. Starting 
#with 1 billion 

#So, I just divided by existing factors until I reached a value that had no lower factor. 
#I"m not sure how I did it, but I'm tired... it's 6857




