# a = 10
# b = 5
# if  a > b:
#     print(True)
# else:
#     print(False)
#     print(False)
#     print(False)
# print("None")


# x,y = 2, 8
# if x < y:
#     print('x is less than y')




    
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')