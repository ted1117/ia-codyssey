def main():
    # 밑 입력 받기
    try:
        base_input = input("Enter number: ")
        base = float(base_input)
    except ValueError:
        print("Invalid number input.")
        return

    # 지수 입력 받기
    try:
        exp_input = input("Enter exponent: ")
        exp = int(exp_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    # 결과값 초기화
    result = 1

    # 반복문으로 지수 계산
    for _ in range(abs(exp)):
        result *= base

    # 지수가 음수일 때
    if exp < 0:
        result = 1 / result

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
