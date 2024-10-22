from odd_even import is_even


def main():
    # total = 0
    # for i in range(1,101):
    # total += i
    sum_100 = [i for i in range(1, 101) if is_even(i)]
    print(f"100까지의 짝수의 합은 {sum(sum_100)}입니다")


if __name__ == "__main__":
    main()
