b = lambda a,b : a-b 
print(b(12,3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

# def name(a,b,c,d,e):
#   return a+b+c+d+e *3

# print(name(3,4,5,6,7))

# print((lambda x : x + 1)(2))

def add_one(x):
    return x + 1
print(add_one(5))

add_one = lambda x: x + 1
print(add_one(5))






full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))