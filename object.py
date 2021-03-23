a = 'hi'
print(id(a))
x = 123
print(id(x))
y = x
print(id(y))
x = 456
print(id(x))
print(id(y))

a = True
print('a =',a)
print('a的类型是',type(a))
a = int(a)
print('a =',a)
print('a的类型是',type(a))
b= False
print('b =',b)
print('b的类型是',type(b))
b = int(b)
print('b =',b)
print('b的类型是',type(b))

a = '123'
a = int(a)
print(type(a))

#a = '123.4'
#a = int(a)
#print(type(a))
a = '123d'
# a = 123
a = float(a)
print('a =',a)
print(type(a))