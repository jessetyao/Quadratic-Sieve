import math
from sympy.ntheory import primerange, isprime

def gen_list_of_primes(B):
    return list(primerange(2, B))

def legendre(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def tonelli_shanks(n,p):
    if legendre(n, p) != 1:
        return None
    
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    while t != 1:
        i, e = 0, 2
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2
        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * b * b) % p
        r = (r * b) % p

    return r

def get_factor_base(N, list_of_p):
    return [p for p in list_of_p if N ** ((p - 1) // 2) % p == 1]

def is_B_smooth(n, factor_base):
    if n == 0:
        return False
    for factor in factor_base:
        while n % factor == 0:
            n = n // factor
    return n == 1

def gen_smooth(N, factor_base, max_num, sieving_array_size):
    ret = set()
    startpoint = int(math.sqrt(N)) - sieving_array_size // 2
    endpoint = startpoint + sieving_array_size

    sieve = [x * x - N for x in range(startpoint, endpoint)]

    for factor in factor_base:
        if factor == 2:
            R_all = [0] if N % 2 == 0 else [1]
        else:
            R = tonelli_shanks(N, factor)
            assert R != 0
            R_all = [R, factor - R]

        for R in R_all:
            k_from = (startpoint - R + (factor - 1)) // factor
            k_to = k_from + (endpoint - (R + factor * k_from) + (factor - 1)) // factor

            for k in range(k_from, k_to):
                x = (R + factor * k) - startpoint
                val = x + startpoint
                assert sieve[x] % factor == 0

                sieve[x] //= factor
                while sieve[x] % factor == 0:
                    sieve[x] //= factor

                if sieve[x] == 1 and x != 0:
                    ret.add(val)
                    if len(ret) > max_num:
                        return list(ret)
    return list(ret)

def vector_gen(n, factor_base):
    ret = []
    for factor in factor_base:
        times = 0
        while n % factor == 0:
            times += 1
            n /= factor
        if times % 2 == 0:
            ret.append(0)
        else:
            ret.append(1)
    return ret

def find_linear_combination(matrix):
    if not matrix:
        return None

    height, width = len(matrix), len(matrix[0])

    if height < width:
        print(f"Insufficient matrix rows: {height} rows, {width} columns needed.")
        return None

    combinations = [[1 if i == j else 0 for j in range(height)] for i in range(height)]

    for i in range(width):
        if matrix[i][i] == 0:
            non_zero_column = next((col for col in matrix[i] if col != 0), None)

            if non_zero_column is None:
                return combinations[i]

            for j in range(i + 1, height):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    combinations[i], combinations[j] = combinations[j], combinations[i]
                    break
            else:
                continue

        for j in range(i + 1, height):
            if matrix[j][i] == 0:
                continue

            matrix[j] = [(col - matrix[i][k]) % 2 for k, col in enumerate(matrix[j])]
            combinations[j] = [(col - combinations[i][k]) % 2 for k, col in enumerate(combinations[j])]

    return combinations[-1]


def get_y(x, factor_base):
    y = 1
    for factor in factor_base:
        while x % (factor ** 2) == 0:
            x = x // (factor ** 2)
            y *= factor
    return y

def quadratic_sieve(N):
    if isprime(N):
        "Already prime"
        return None
    B = int(math.exp(math.sqrt(math.log(N)*math.log(math.log(N)))))
    primes = gen_list_of_primes(B)
    factor_base = get_factor_base(N, primes)
    smooth_nums = gen_smooth(N, factor_base, len(factor_base) + 20, 1000000)
    while True:
        matrix = [vector_gen(sn**2 - N, factor_base) for sn in smooth_nums]

        linear_combination = find_linear_combination(matrix)

        if not linear_combination:
            return 0, 0
        
        dependent_subset = [sn for i, sn in enumerate(smooth_nums) if linear_combination[i] == 1]

        x = math.prod(dependent_subset)
        pre_y = math.prod([sn**2 - N for sn in dependent_subset])

        y = get_y(pre_y, factor_base)
        if x == y:
            smooth_nums.remove(dependent_subset[0])
            continue

        f1, f2 = math.gcd(x + y, N), math.gcd(x - y, N)

        if all(factor not in (N, 1) for factor in (f1, f2)):
            return f1, f2
            
        smooth_nums.remove(dependent_subset[0])

