#Project Euler_Problem 1
#The challenge is to sum all multiples of 3 and 5 from 0 to 1000.

#I can easily generate lists of all of the numbers. 

a = seq(from =3, to= 1000, by=3)

b = seq(from =5, to= 1000, by=5)

print(a)
print(b)

#The problem, however, is that all multiples of 3 AND 5 repeat. 


#########################

z =sum(c(a,b))            #Interesting-- this outputs 267333
print(z)


d=a+b                   #But this outputs 311888, and generates a warning
e=sum(d)                #message that the length of the longer item is
print(e)h               #not a mulitple of the shorter one.


g=sum(a)
print(g)
j=sum(b)
print(j)
print(sum(g,j))
j+g                       #this results in the same 267333

#^ This is just an attempt to resolve confusion I have about the sum() 
# vs. the "+" operations
##############################


#Dplyr library supplies a function for the deletion of duplicates


library(dplyr)

x=c(a,b)

S= x[!duplicated(x)]

print(S)


#Visual inspection confirms that all duplicates have been removed.

Solution = sum(S)
print(Solution)

#More concisely, the above can be condensesd into the following line.

t=sum(x[!duplicated(x)])

#Answer = 234168

#Oops! They got me on a technicality -- the questions requests the sum of all
#3/5 multiples *LESS* than 1000. Corrected = t - 1000, since 1000 is a multiple
#of five. 


a = seq(from =3, to= 999, by=3)

b = seq(from =5, to= 999, by=5)

library(dplyr)

x=c(a,b)

t=sum(x[!duplicated(x)])

print(t)

#Answer= 233168
