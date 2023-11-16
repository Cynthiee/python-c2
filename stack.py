stack = []

def my_stack(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

my_stack(3)
my_stack(2)
my_stack(1)

print(pop())
print(pop())
print(pop())