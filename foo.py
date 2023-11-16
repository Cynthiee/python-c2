# def f():
#     return 'foo'
    
# print(f())


def f():
   return dict(foo=1, bar=2, baz=3)

print(f())
print(f()['baz'])
print(f().keys())
print(f().items())

