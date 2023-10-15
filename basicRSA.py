import math
from Crypto.Util import number
from quadratic_sieve import quadratic_sieve

def generate_prime(n):
    return number.getPrime(n)

def generate_e(H):
    e = 3
    while(e<H):
        if (math.gcd(e, H) == 1):
            return e
        else:
            e += 2

p = generate_prime(20)
q = generate_prime(20)
N = p * q
print(p,q,N)
H = (p-1) * (q-1)
e = generate_e(H)
public_key = (N,e)
d = pow(e, -1, H)
msg = generate_prime(10)
print(msg)
encrypt = pow(msg, e, N)
print(encrypt)
decrypt = pow(encrypt, d, N)
print(decrypt)

def break_Rsa (public_key, encrypt):
    N, e = public_key
    p, q = quadratic_sieve (N)
    H = (p-1) * (q-1)
    d = pow(e, -1, H)
    decrypt = pow(encrypt, d, N)
    return decrypt

print(break_Rsa(public_key, encrypt))
