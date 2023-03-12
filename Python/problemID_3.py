# https://projecteuler.net/archives
# Problem 3

def prime_Factor(number):
    primes = []
    n = 2

    while (number != 1):
        if (number % n == 0):
            primes.append(n)
            number /= n
        else:
            n += 1
    return primes[-1] 
#or just 'return primes' if u want to see the full list, this only shows the highes prime factor

if __name__ == "__main__":

    print(prime_Factor(13195))
    print(prime_Factor(600851475143))