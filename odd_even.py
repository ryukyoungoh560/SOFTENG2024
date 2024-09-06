def is_even(n):
    return n % 2 == 0




def main():
    n = int(input("정수를 입력하세요"))

    if is_even(n) == True:
        print(f"숫자 {n}은 짝수입니다.")
    else:
        print(f"숫자 {n}은 홀수입니다.") 

if __name__ == "__main__":
    main()