from random import randint as rd

k = int(input('k = '))
arr = list()
for i in range(k, 0, -1):
    x = rd(-100, 100)
    if x != 0:
        if x > 0 and i != k:
            arr.append(f'+{x}x^{i}')
        else:
            arr.append(f'{x}x^{i}')
x = rd(-100, 100)
if x > 0 and i != k:
    arr.append(f'+{x}')
else:
    arr.append(f'{x}')
print(''.join(arr),'= 0')