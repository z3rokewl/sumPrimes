
def eliminate_composites(prime, sieve):
    temp_index = new_prime
    while temp_index < len(binary_sieve):
        binary_sieve[temp_index] = 1
        temp_index = temp_index + prime


def sieve():
    binary_sieve = 10000000*[0]
    binary_sieve[0] = 1
    binary_sieve[1] = 1
    prime_list = []

    for index in range(len(binary_sieve)):
        if binary_sieve[index] == 0:
            new_prime = index
            prime_list.append(new_prime)
            temp_index = new_prime
            while temp_index < len(binary_sieve):
                binary_sieve[temp_index] = 1
                temp_index = temp_index + new_prime

    return prime_list



