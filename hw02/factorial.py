def pactorial(n:int) -> int:
    total = 1
    for i in range (1, n+1):
        total *= i
    
    return total

def main():
    n = int(input("정수입력: "))

    answer = pactorial(n)

    print(answer)
    
if __name__ == "__main__":
    main()
