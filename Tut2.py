# taking input from users

#print("enter number")
#a = input()
#print("entered number is")
#print(a)


# Method to print from 1 to N
#print(*range(1, int(input())+1), sep='')


# List comprehensions Examples
import builtins

nums = [1,2,3,4,5]
odd=[]
for n in nums:
	if n%2 == 1:
		odd.append(n*2)

#print(odd)

podd = []

podd = [n*2 for n in nums if n%2  ==1]
#print(podd)

n=2
x=1
y=1
z=1
outlist=[]
lol = [[i,j,k] for i in range(x+1)
		for j in range(y+1)
		for k in range(z+1)
		if (i+j+k)<=n
		]
#print(lol)


#Functional Programming Tools

k = [1,2,3,4]
t = list(map(lambda x:x*x ,k))
print(t)


items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

 #  allows us to implement this in a much simpler and nicer way. Here you go:
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

k  = hash(1)
print(k) 



# Other things

	Generate random number in python  

		random.randint(50,100)

# string formatting
txt = "The price is {:.2f} dollars"
txt = "The price is {:.2f} dollars"
