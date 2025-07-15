def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by Zero")
        return
    return result


def calculate(a, b, operator) -> int | None:
    op_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}

    if op_func := op_dict.get(operator):
        if (result := op_func(a, b)) is not None:
            print(f"Result: {result}")
    else:
        print("Invalid operator.")


def calculate_1(a, b, operator) -> int | None:
    match operator:
        case "+":
            result = add(a, b)
        case "-":
            result = subtract(a, b)
        case "*":
            result = multiply(a, b)
        case "/":
            if not (result := divide(a, b)):
                return
        case _:
            print("Invalid operator.")
            return
    print(f"Result: <{result}>")


if __name__ == "__main__":
    while True:
        try:
            user_input = input("계산식을 입력하세요: ")

            # quit을 입력하면 프로그램 종료
            if user_input == "quit":
                quit()

            num1, operator, num2 = user_input.split()
            a, b = (int(float(x)) for x in (num1, num2))
            break
        except ValueError:
            print("잘못된 입력입니다. 다시 입력하세요.")

    calculate(a, b, operator)
