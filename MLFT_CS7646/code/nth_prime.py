def nth_prime(n):
    """Compute the nth prime number
    :param int n:
    :rtype: int
    """
    # TODO: Write code here that computes the Nth prime
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1]


def test_run():
    print nth_prime(149896)


if __name__ == "__main__":
    test_run()