def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float | None:
    # try:
    #     result = a / b
    # except ZeroDivisionError:
    #     print("Error: Division by Zero")
    #     return
    # return result
    if b == 0:
        print("Error: Division by Zero.")
        return
    return a / b


def calculate(a, b, operator) -> int | None:
    op_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}

    if op_func := op_dict.get(operator):
        if result := op_func(a, b):
            print(f"Result: <{result}>")
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
            num1, num2 = (int(float(x)) for x in input("Enter 2 numbers: ").split())
            break
        except ValueError:
            print("올바른 입력이 아닙니다. 숫자를 입력하세요.")

    op_input: str = input("Enter operator: ")

    calculate(num1, num2, op_input)
    # calculate_1(num1, num2, op_input)
