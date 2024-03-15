print('\nтаблица умножения, используя цикл while')
a=1
b=1
while 0 < a < 10:
    while 0 < b < 10:
        print(a * b, end = '\t')
        b += 1
    print('\r')
    b = 1
    a += 1

print('\nтаблица умножения, используя цикл for')
for i in range(10):
    i += 1
    for j in range(10):
        j += 1
        print(j * i, end="\t")
    print('\r') # просто перевод корретки







