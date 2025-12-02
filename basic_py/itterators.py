for i in ['abc', 'efg', 'hij']:
    print("['abc', 'efg', 'hij'] -> ", i)

print("*"*5)

for i in ('abc', 'efg', 'hij'):
    print("('abc', 'efg', 'hij') -> ", i)

print("*"*5)

for i in {'abc', 'efg', 'hij'}:
    print("{'abc' : 1, 'efg' : 2, 'hij' : 3} -> ", i)

print("*"*5)

for i in 'abc':
    print("abc ->", i)

print("*"*5)

for line in open('../file_handling/building a file.txt', 'r'):
    t_line = line.strip('\n')
    print("building a file's lines -> ", t_line)