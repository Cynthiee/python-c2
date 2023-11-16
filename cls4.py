# print(fruits)
# print(fruits[2])
# fruits.append('tangerine')
# fruits.clear()
# another_fruits = fruits.copy()
# print(another_fruits)
# print(fruits.count('cucumber'))
# x = fruits.count('cucumber')
# print(x)
# vegetables = ['carrot', 'pumpkin', 'spinash']
# # fruits.extend(vegetables)
# m = fruits.index(19)
# print(m)
# fruits.insert(2, 'coconut')
# fruits.pop(2)
# fruits.remove('apple')
# fruits.reverse()
# fruits.sort(reverse=True)
# print(fruits)



# def function(e):
#     return len(e)

# fruits = ['mang', 'orang', 'pawpaw', 'ape', 'cucumber']

# fruits.sort(key=function)
# print(fruits)

# def another_func(h):
#     return h['year']

# cars = [
#     {'car':'Ford', 'year':2005},
#     {'car':'Mitsubishi', 'year':2000},
#     {'car':'BMW', 'year':2011},
#     {'car':'VW', 'year':2019}
# ]

# cars.sort(reverse=True, key=another_func)
# print(cars)  

# fruits = ['mango', 'orange', 'pawpaw', 'apple', 'cucumber', 'cucumber']
# print(len(fruits))
# print(type(fruits))

travel_list = list(('Autralia', 'Autralia', 'Dubia', 'USA', 'Finland',
                    'England', 'Germany', 'Japan', 'Russia', 'Tibet',
                    'Ghana', 'Austria', 'Kuwait', 'Korea', 'Israel', 'Czech'))

# print(travel_list)
# travel_list[7] = 'Istanbul'
# travel_list[11:15] = ['Switzerland', 'Canada', 'China', 'Iceland']
# print(travel_list)

# travel_list[11:13] = ['Switzerland', 'Canada', 'China', 'Iceland']
# print(travel_list)
# del travel_list[7]
# print(travel_list)

# for i in travel_list:
#     print(i)

# for i in range(len(travel_list)):
#     print(i)

# i = 0
# while i < len(travel_list):
#     print(travel_list[i])
#     i = i+1

# [print(x) for x in travel_list]

# new_travel_list = []
# for i in travel_list:
#     if 'ra' in i:
#         new_travel_list.append(i)

# print(new_travel_list)

another_travel_list= [a for a in travel_list if 'an' in a ]
print(another_travel_list)
