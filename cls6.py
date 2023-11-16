my_dict= {'name':'Cynthia', 
        'age':50,
        'city':'Aba',
        'fruits':['orange', 'mango', 'pawpaw'], 
          }
print(my_dict)
print(len(my_dict['fruits']))
a = my_dict.items()
print(a)

for x in my_dict.values():
    print(x)


fruits=['orange', 'mango', 'pawpaw']
if 'orange' in fruits:
    print(fruits[0])