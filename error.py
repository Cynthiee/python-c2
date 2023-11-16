a = ['foo', 'bar', 'baz', 'qux']

try:
    print(a.index('corge'))
except ValueError:
    print('courge not found')