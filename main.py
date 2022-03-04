import random


def miller_rabin(n):
    m = 0
    for k in range(1, n):
        m = (n-1)//2**k
        if m % 2 == 1:
            break
    a = random.randint(2, n-1)
    b = pow(a, m, n)
    if b % n == 1:
        return True
    for i in range(1, k+1):
        if b % n == n-1:
            return True
        else:
            b = pow(b, 2, n)
    return False


def square_multiply(x, m, n):
    y = 1
    r = m.bit_length()
    for i in range(0, r):
        if m % 2 == 1:
            y = y * x % n
        x = pow(x, 2, n)
        m = m >> 1
    return y


def generate_prime():
    list_of_primes = [1, 7, 11, 13, 17, 19, 23, 29]
    z = random.randint(2**400, 2**401-1)
    p = 30 * z
    is_prime = False
    for i in range(200):
        for j in list_of_primes:
            n = p + j + i * 30
            for k in range(50):
                is_prime = miller_rabin(n)
                if not is_prime:
                    break
            if is_prime:
                return n


def is_prime(number):
    for k in range(50):
        if not miller_rabin(number):
            return False
    return True


def generate_pg():
    while True:
        q = generate_prime()
        p = 2 * q + 1
        if is_prime(p):
            g = random.randint(2, p-2)
            return p, g


if __name__ == '__main__':
    p, g = generate_pg()

    a = random.randint(2, p)
    A = square_multiply(g, a, p)

    b = random.randint(2, p)
    B = square_multiply(g, b, p)

    s_a = square_multiply(B, a, p)
    s_b = square_multiply(A, b, p)
    print(s_b == s_a)
