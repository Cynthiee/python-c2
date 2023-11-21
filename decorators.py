# def decorator_function(original_function):
#     def wrapper_function():
#         print('wrapper executed this before {}'.format(
#             original_function.__name__))
#         return original_function()
#     return wrapper_function

# decorator_function('original_function')

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))
# print(plus_one(3))
# print(function_call(4))

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi()
# hello = hello_function()
# print(hello)
# print(hello_function())
print(hello_function())