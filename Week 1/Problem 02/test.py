def main():
    # 숫자 입력
    num_input = input("Enter number: ")
    try:
        number = float(num_input)
    except ValueError:
        print("Invalid number input.")
        return

    # 지수 입력
    exp_input = input("Enter exponent: ")
    try:
        exponent = int(exp_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    # 반복문을 이용한 거듭제곱 계산
    result = 1
    if exponent == 0:
        result = 1
    elif exponent > 0:
        for _ in range(exponent):
            result *= number
    else:  # 음수 지수
        for _ in range(-exponent):
            result *= number
        result = 1 / result

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
