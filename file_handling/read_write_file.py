import json

f = open("books.json", 'r')
s=f.read()
print(s)
f.close()

f = open("building a file.txt", 'w')
f.write("Hello World")
f.close()

f = open("building a file.txt", 'a')
f.write("\nHave a good day")
f.close()

f = open("building a file.txt", 'r')
i=0
for line in f:
    #print("line number ", i, ':', line)
    #i = i + 1

    tokens = line.split(' ')
    print(tokens)
f.close()