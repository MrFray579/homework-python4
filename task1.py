n = int(input('Введите количество цифр числа Пи после запятой: '))
pi = 0
for k in range(n):
    number_pi = (1/(16**k)) * ((4/(8*k + 1)) - (2/(8*k + 4)) - (1/(8*k + 5)) - (1/(8*k + 6)))
    pi += number_pi
print(f'Пи = {round(pi, n)}, {n} цифр после запятой ')
# возможно ли сделать так, чтобы в числе пи после запятой было больше 15 символов?


