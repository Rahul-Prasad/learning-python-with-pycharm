d = {
    "a": '10',
    "b": '20',
    "c": '30',
}

print(d)
del d['c']
print(d)
for k, v in d.items():
    print('key = ', k, ', value = ', v)

