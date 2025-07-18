"""
## 중위표기법 후위표기법 변환
1. 피연산자는 피연산자 스택에 push
2. 연산자는 연산자 스택의 가장 마지막 요소와 우선순위를 비교해서 마지막 요소보다 우선순위가 동급이거나 낮으면 연산자 pop하고 피연산자 스택에 push
3. 2번을 연산자 스택이 비거나 우선순위가 높을 때까지 반복
4. 1~3을 반복

## 후위표기법 계산
1. 피연산자는 피연산자 스택에 push
2. 연산자가 나오면 피연산자 2개 pop
3. 피연산자 2개와 연산자로 연산 후 결과값을 피연산자 스택에 push
4. 1~3 반복
"""

from typing import Any, Union


class Stack:
    def __init__(self) -> None:
        self._items: list = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Invalid input.")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def size(self) -> int:
        return len(self._items)


########### 사칙연산 함수 정의 ############
def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError
    return a / b


########### 입력 처리 ##############
def format_user_input(expression: str) -> list[str]:
    expression = expression.replace("(", " ( ")
    expression = expression.replace(")", " ) ")
    expression = expression.replace("+", " + ")
    expression = expression.replace("-", " - ")
    expression = expression.replace("*", " * ")
    expression = expression.replace("/", " / ")

    return expression.split()


def infix_to_postfix(expression: list[str]) -> list[Union[float, str]]:
    """중위표기법을 후위표기법으로 변환"""
    output: list[Union[float, str]] = []
    operators = Stack()
    priority = {"+": 0, "-": 0, "*": 1, "/": 1}

    for ch in expression:
        if ch == "(":
            operators.push(ch)
        elif ch == ")":
            while not operators.is_empty() and operators.peek() != "(":
                output.append(operators.pop())
            if operators.is_empty():
                raise ValueError("괄호 불일치: '('가 없습니다.")
            operators.pop()
        else:
            try:
                num = float(ch)
                output.append(num)
            except ValueError:
                op = ch
                if op not in priority:
                    raise ValueError("Invalid input.")

                while not operators.is_empty() and priority.get(
                    operators.peek(), -1
                ) >= priority.get(op, -1):
                    output.append(operators.pop())
                operators.push(op)

    while not operators.is_empty():
        output.append(operators.pop())

    return output


def calculate(postfix: list[Union[float, str]]) -> float:
    op_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
    operands = Stack()

    for ch in postfix:
        if isinstance(ch, float):
            operands.push(ch)
        else:
            operand2 = operands.pop()
            operand1 = operands.pop()

            op_func = op_dict[ch]  # type: ignore
            result = op_func(operand1, operand2)

            operands.push(result)

    if operands.size() == 1:
        return operands.pop()
    else:
        raise ValueError("Invalid input.")


def main():
    user_input: str = input("수식을 입력하세요: ")

    expression: list[str] = format_user_input(user_input)

    try:
        postfix_list = infix_to_postfix(expression)
        result = calculate(postfix_list)
        print(result)

    except ZeroDivisionError:
        print("Error: Division by zero.")

    except (ValueError, IndexError):
        print("Invalid input.")


if __name__ == "__main__":
    main()
