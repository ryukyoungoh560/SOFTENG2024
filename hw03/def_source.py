def is_even(n):
    return n % 2 == 0

def f2c(temp):
    return (temp - 32) * 5 / 9 

def c2f(temp):
    return (temp + 32) * 9 / 5

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

def main():
    pass
    # print(is_even(4))
    # print(f2c(5))
    # print(c2f(5))
    # print(is_prime(13))

if __name__ == "__main__":
    main()