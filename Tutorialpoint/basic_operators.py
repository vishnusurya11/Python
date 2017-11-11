#arithmetic operator
a=5
b=23
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b%a)
print(b**a)


#bitwise operators
a=1
b=2
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)

#membership operators
x=4
y=[2,4,5,7,8,9,10,14]
if(x in y):
	print ("aloha")
x=20
if( x not in y):
	print("omega")

#identity operator
a="this is one"
b="this is "
if(a is b):
	print ("yurekaaa!!!")
if( a is not b):
	print("naruto")