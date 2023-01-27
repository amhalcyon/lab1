a = "Hello World"
print(type(a)) #<class 'str'>	
b = 20	
print(type(b)) #<class 'int'>
c = 20.5	
print(type(c)) #<class 'float'>	
d = 1j
print(type(d)) #<class 'complex'>
e = ["apple", "banana", "cherry"]
print(type(e)) #<class 'list'>
f = ("apple", "banana", "cherry")	
print(type(f)) #<class 'tuple'>	
g = range(6)
print(type(g)) #<class 'range'>	
h = {"name" : "John", "age" : 36}	
print(type(h)) #<class 'dict'>
i = {"apple", "banana", "cherry"}	
print(type(i)) #<class 'set'>
j = frozenset({"apple", "banana", "cherry"})
print(type(j)) #<class 'frozenset'>	
k = True	
print(type(k)) #<class 'bool'>
l = b"Hello"
print(type(l)) #<class 'bytes'>
m = bytearray(5)	
print(type(m)) #<class 'bytearray'>	
n = memoryview(bytes(5))
print(type(n)) #<class 'memoryview'>	
o = None
print(type(o)) #<class 'NoneType'>