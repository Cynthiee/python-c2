# ft = open('C:/Users/islac/Downloads/U4PracticeWAWorksheet.docx', 'br')
# print(ft.read())

# # print(f.read())
# # print(f.readline())
# print(f.readlines())

# with open('abc.txt') as xyz:
#     if xyz.readable():
#         print(xyz.read())
#         xyz.close()
    

# f = open('abc.txt')
# for i in f:
#     print(i)

# a = open('abc.txt', 'a')
# a.writelines('Welcome back\n')
# a.close()
# a = open('abc.txt')
# print(a.read())

# b = open('xyz.txt', 'a')
# b.write('I am Batman\n')
# b.close()

# b = open('xyz.txt', 'r')
# print(b.read())

# c = open('byc.txt', 'w')
# c.write('We just overwrote you.')
# c.close()

# c = open('byc.txt', 'r')
# print(c.read())

# d = open('bfc.txt', 'x')
# d.close()

d = open('bfc.txt', 'w')
d.write('I am a superwoman\n')
d.close()

d = open('bfc.txt', 'r')
print(d.read())


import os 