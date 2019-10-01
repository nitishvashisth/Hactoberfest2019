#################
# Python Basics #
#################


##  Python
	# Interpreted , Object Oriented
	# Case Sensitive
	# 3.4.3 version


# variables Assignment

counter = 100   # Integer
miles = 100.56	#Floating point
name = "John"	#String

print(counter)
print(miles)
print(name)
print()

# Multiple assignement

a = b = c = 1

d,e,f = 1,3.5,"Ram"

print(a,b,c,d,e,f)

del a,b,c,d,e,f

# Standard Data Type

	# 1.Number
	# 2.String 
	# 3.List  []
	# 4.Tuples () : read only 
	# 5.Dictionary {} : key value pair


# Python Numbers

var1 = 1
var2 = 10
var3 = 23

print(var1)
del var1     # Deleting variable

del var2,var3

# Numbers --> int , long , float , complex

# Python Strings

str = "Hello World"

print(str)
print(str[0])
print(str[2:7])
print(str[2:])
print(str * 2) 		# Prints string two times
print(str + "Test")


# Python List : all slice opreations applicabe , as that for string

list = ['a' , 12 , 2.30 , 'b' , 45]
tinylist = ['g' , 10]

print(list)
print(list + tinylist)  # print merged list


list[2] = 67      # changing list element

print(list)

# Python Tuple
	# Same as list , but it is Read Only

# Python Dictionary

dict = {}
dict['one'] = "First element"
dict[2] = "Second element"

tinydict = {'name' : 'John' , 'rollno' : 39}

print(dict)
print(tinydict)

print(dict['one'])
print(dict.keys())
print(dict.values())

# Data Type Conversion

# Types of Operator

	# 1.Arithmatic
	# 2.Comparision
	# 3.Assignment
	# 4.Logical
	# 5.Bitwise
	# 6.Memembership Operators
	# 7.Identity Operators

# Arithmetic

a = 2
b = 5

c = b+a
d = b-a
e = b*a
g = b/a
h = b%a
i = a**b   # a**b = a to the power b
j = b//a   # Floor Division

print(a , b , c , d , e , g , h , i , j)


# Python Comparision Operators

	# == , != , > , < , >= , <=

# Python Assignment Operators

	# = , += , -= , *= , /= , %= , **= , //=

# Python Bitwise Operators

	# & , | , ^ , ~ , << , >>

# Python Logical Operators

	#There are following logical operators supported by Python language. 
	#Assume variable a holds True and variable b holds False		

    # (a and b) , (a or b) , Not(a)

#  Python Membership Operators

	# testing membership in a sequence, such as strings , list , tuple

	# in , notin

# Python Decision Making

	# if statements
	# if...else statements
	# nested if statements

var1 = 100

if var1:
	print("evaluated to true")
	print(var1)

var2 = 0	
if var2:
	print("evaluated to true")
	print(var2)

var3 = -100	
if var3:
	print("evaluated to true")
	print(var3)	

amt = 100

if amt<90:
	print("less than 90")
else:
	print("more than 90")	

# Loops

	# While loop
	# for loop
	# nested loops

	# While loop

count = 0
while (count<9):
		print("The count is :",count)
		count = count +1
print("good by")			


count = 0

while (count<5) :
	print("count is :",count)
	count+=1
else:
	print("out of loop")	

	# for loop

for letter in 'Python':
	print('current Letter :',letter)	

roll = [2,10,3,19,5]
for a in roll:
	print(a,end='')


print()



# Functions in Python #
#######################

def printme(str):
	"This is my first python function"
	print(str)
	return

printme("hello");	

def changelist(mylist):
	"Second python function"
	mylist.append([4,5,6]);
	print("values are ",mylist)

mylist = [1,2,3];
changelist(mylist);

### All parameters in python are passed by reference

# Function Arguments
	#Required Arguments
	#KeyWord argument
	#Default argument
	#variable-length arguments


def printinfo(*vartuple):
	"Function showing variabele length arguments"
	print("Output is")
	#print(argu)
	for var in vartuple:
		print(var)
	return;

printinfo(11)	
printinfo(10,20,30,40)

sum = lambda ar,br: ar+br;

print("The total is ",sum(10,20))	

# To read command line agruments
if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="run json file path")
    parser.add_argument("-p", dest="regression_run_json_path",
                        required=True, type=str, help="input path for run json file path")

    args = parser.parse_args()

    runJson_filepath = args.regression_run_json_path


