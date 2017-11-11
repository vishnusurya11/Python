#multiple assignments
a,b,c=1,2,"hola"
print(a)
print (b)
print (c)

#numbers
a=2
b=20
print(a)
print(b)
 

#strings

str="Hello world"
print(str)
print(str[0])
print(str[2:8])
print(str[2:])
print(str*2)   #repetition
print(str+" !!sup!!") #concatenation

#lists

list=['ronaldo',7,'bale',11,'bezema',9]
smalllist=['real madrid','hala madrid']
print(list)
print(list[0])
print(list[1:2])
print(list[2:])
print(list *2)
print(list+smalllist)

#tuple
tuple=('ronaldo',7,'bale',11,'bezema',9)
smalltuple=('real madrid','hala madrid')
print(tuple)
print(tuple[0])
print(tuple[1:2])
print(tuple[2:])
print(tuple *2)
print(tuple+smalltuple)
#you can not add inputs to a tuple unlike lists

#dictionary
dict={}
dict['one']='this is one'
dict[2]=3
print(dict['one'])
print(dict[2])
print(dict.keys())
print(dict.values())

#data conversions
num='45'
knum= int(num) #converts string to int
knum=knum+1
print(knum)