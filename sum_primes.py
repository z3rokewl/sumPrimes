import prime_sieve


def sum_primes():
    prime_list = prime_sieve.sieve()
    counter = 0
    for prime in prime_list:
        if prime < 2000000:
            counter += prime
        else:
            return counter

def main():
    print sum_primes()
    return 0


if __name__ == '__main__':
    main()