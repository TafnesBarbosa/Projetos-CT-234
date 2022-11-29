# Funções de pattern matching
from math import ceil

def KarpRabinMatch(P, T, d = 10):
    m = len(P)
    n = len(T)
    q = major_prime(m)
    print(m, q)
    h = d ** (m - 1) % q
    p = 0
    t = []
    t.append(T[0])
    t[0] = 0
    for i in range(m):
        p = (d * p + P[i]) % q
        t[0] = (d * t[0] + T[i]) % q
    for s in range(n-m+1):
        if p == t[s]:
            if P == T[s:s+m]:
                return s
        if s < n - m:
            t.append(0)
            t[s+1] = (d * (t[s] - T[s] * h) + T[s + m]) % q
    return -1

def is_prime(n):
    for i in range(2, ceil(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def major_prime(m):
    q = m + 1
    while True:
        if is_prime(q):
            return q
        else:
            q += 1

def main():
    print(KarpRabinMatch([5, 4, 2, 6], [3, 1, 5, 4, 2, 6, 8]))

main()
