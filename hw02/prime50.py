from prime_number import is_prime


def main():
    # primes = []
    # for i in range(1,51):
    # if is_prime(i) == True:
    # primes.append()

    primes = [i for i in range(2, 51) if is_prime(i)]
    print(f"50까지의 소수: {primes}")


if __name__ == "__main__":
    main()
