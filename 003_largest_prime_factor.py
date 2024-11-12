from collections import Counter
from random import randint, randrange
from math import gcd

def is_prime(n):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
        if not n % p: return n == p
    
    s, d = -1, n - 1
    while not d & 1:
        s, d = s + 1, d >> 1
        
    x = pow(randint(2, n - 1), d, n)
    
    if x == 1 or x == n - 1:
        return True

    for _ in range(s):
        x = pow(x, 2, n)
        if x == 1:
            return False
        if x == n - 1:
            break
    else:
        return False
    
    return True

def pollard_rho(n):
    while True:
        x = c = randrange(1, n)
        f = lambda x: (pow(x, 2) + c) % n
        y = f(x)
        while (d := gcd(abs(x - y), n)) == 1:
            x, y = f(x), f(f(y))
        if d != n:
            return d

def highest_factor(n):
    def _factor(n):
        if is_prime(n): return Counter([n])
        return _factor(r := pollard_rho(n)) + _factor(n // r)
    
    factors = _factor(n)
    return max(factors.keys())

print(highest_factor(600851475143))
