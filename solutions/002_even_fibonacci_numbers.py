a, b = 0, 1
res = 0

while a < 4 * 10 ** 6:
    if a % 2 == 0:
        res += a
    
    a, b = b, a + b

print(res)
