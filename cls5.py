# poem = {'Twinkle', 'little', 'star', 'how', 'i', 'wonder'}

# for x in poem:
#     print(x)

# poem.remove('Twinkle')
# poem.discard('to')
# poem.pop()
# poem.clear()
# cars = {'BMW', 'Benz', 'Audi','star', 'how'}
# # poem.update(cars)
# print(poem)
# combo = poem | cars
# print(combo)
# poem.symmetric_difference_update(cars)
# print(poem)
# new_poem = poem.symmetric_difference(cars)
# print(new_poem)
num1 = {1,2,3,4,5,6}
num2 = {2,4,6,8,10}
# num3 = num2.symmetric_difference(num1)
# print(num3)
# # num1.symmetric_difference_update(num2)
# print(num1)
# x = num1.difference(num2)
# print(x)
# y = num2.difference(num1)
# print(y)
b = num1.isdisjoint(num2)
print(b)
c = num1.issubset(num2)
print(c)
d = num1.issuperset(num2)
print(d)


