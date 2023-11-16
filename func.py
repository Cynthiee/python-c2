# def f(qty, item, price):

#     print(f'{qty} {item} cost ${price:.2f}')

# f(6, 'banana', 1.3)
# f(6, 'banana', price=1.20)
# f(qty=6, item='banana', price=1.20)


# def f(qty=6, item='banana', price=1.20):

#     print(f'{qty} {item} cost ${price:.2f}')

# # f(6, 'banana', 2.8)  
# f()


# def f(my_list=[]):
#     my_list.append('###')
#     return my_list

# print(f())
# print(f())
# print(f())
# print(f())
# print(f(['gh', 'jk', 'hk', 'jk']))


def f(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('###')
    print(my_list)
    # return my_list

f()
f()
f()
f()

# print(f(['foo', 'bar', 'baz']))
# print(f([1, 2, 3, 4, 5]))