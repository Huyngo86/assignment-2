# 1.1
def a(n):
    kq = 1
    for _ in range(n):
        kq = (3 * kq) % 9999
    return kq

print("1.1 | a1000 mod 9999 =", a(1000))

# 1.1 bonus
A = ['a', 'b', 'c']
count = 0
result = ""

def sinh_chuoi(prefix, n):
    global count, result
    if n == 0:
        count += 1
        if count == 100:
            result = prefix
        return
    for ch in A:
        if count >= 100:
            return
        sinh_chuoi(prefix + ch, n - 1)

sinh_chuoi("", 10)
print("1.1 BONUS | Phần tử thứ 100:", result)

# 1.2  
def b(n):
    m = (n + 1) // 2
    kq = 1
    for _ in range(m):
        kq = (3 * kq) % 9999
    return kq

print("1.2 | b1000 mod 9999 =", b(1000))

# 1.2 BONUS 
palindromes = []


def sinh_palindrome(prefix, n):
    if len(prefix) == (n + 1) // 2:
        if n % 2 == 0:
            s = prefix + prefix[::-1]
        else:
            s = prefix + prefix[-2::-1]
        palindromes.append(s)
        return
    for ch in A:
        sinh_palindrome(prefix + ch, n)

sinh_palindrome("", 10)
print("1.2 BONUS | Palindrome thứ 100:", palindromes[99])

# 1.3 
def fact(n):
    kq = 1
    for i in range(1, n + 1):
        kq *= i
    return kq

def c(i, j, k):
    n = i + j + k
    return fact(n) // (fact(i) * fact(j) * fact(k))

print("1.3 | c(100,90,80) mod 9999 =", c(100, 90, 80) % 9999)

# 1.4  
def d(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    d0, d1 = 1, 3
    for _ in range(2, n + 1):
        d0, d1 = d1, (2 * d1 + 2 * d0) % 9999
    return d1

print("1.4 | d1000 mod 9999 =", d(1000))

# 1.5  
def e(n):
    e0 = 1
    for _ in range(n):
        e0 = (3 * e0 - 1) % 999
    return e0

print("1.5 | e1000 mod 999 =", e(1000))
#2
MOD = 9901

def coeffs_iterative(n):
    a, b, c, d = 1, 0, 0, 0  
    for _ in range(n):
        na = 2*b - 15*c
        nb = a - 15*d
        nc = -5*a + 2*d
        nd = -5*b + c
        a, b, c, d = na % MOD, nb % MOD, nc % MOD, nd % MOD
    return a, b, c, d

a, b, c, d = coeffs_iterative(1000)
S = (a + b + c + d) % MOD
print("2 | (a1000 + b1000 + c1000 + d1000) mod 9901=" ,S)  






