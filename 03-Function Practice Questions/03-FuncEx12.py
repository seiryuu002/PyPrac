def count_primes(n):
    if n < 2:
        return 0
    primes = [2]
    x = 3
    while x <= n:
        for i in primes:
            print("|", x, "|", i, "|", x % i, "|")
            if x%i == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    print(len(primes))

count_primes(100)
