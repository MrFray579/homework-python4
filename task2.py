def Factor(n):
    arr_factor = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            arr_factor.append(d)
            n //= d
            #print(n)
        else:
            d += 1
            #print(d)
    if n > 1:
        arr_factor.append(n)
    return arr_factor 
print(Factor(int(input('Введите число: '))))
