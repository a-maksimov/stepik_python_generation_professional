def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def tribonacci_rec(n):
        result = cache.get(n)
        if result is None:
            result = tribonacci_rec(n - 3) + tribonacci_rec(n - 2) + tribonacci_rec(n - 1)
            cache[n] = result
        return result

    return tribonacci_rec(n)
