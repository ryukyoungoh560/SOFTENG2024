def f2c(temp_f: float) -> float:
    return (temp_f - 32) * 5 / 9 


def main():
    temp_f = float(input("온도입력(화씨): "))
    temp_c = f2c(temp_f)

    print(f"화씨온도{temp_f}F -> 섭씨온도{temp_c:.1f}C")    

if __name__ == "__main__":
    main()