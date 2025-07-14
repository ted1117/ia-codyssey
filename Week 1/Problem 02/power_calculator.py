def main():
    try:
        base_input = input("Enter number: ")
        base = float(base_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exp_input = input("Enter exponent: ")
        exp = int(exp_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    result = 1

    for _ in range(abs(exp)):
        result *= base

    if exp < 0:
        result = 1 / result

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
