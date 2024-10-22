def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("정수입력: "))

    if is_prime(n) == True:
        print(f"정수{n}은 소수입니다.")
    else:
        print(f"정수{n}은 소수가 아닙니다.")


if __name__ == "__main__":
    main()
