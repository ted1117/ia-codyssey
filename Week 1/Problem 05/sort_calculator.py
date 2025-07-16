def main():
    while True:
        try:
            numbers_input: list[float] = list(
                map(float, input("2 이상의 숫자를 입력하세요: ").split())
            )

            # 숫자를 2개 이상 입력하도록 유도
            if len(numbers_input) > 1:
                break
            else:
                print("2개 이상의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 다시 입력하세요.")
    result: list[float] = sort_numbers(numbers_input)
    print("Sorted:", *(f"<{value}>" for value in result))


def sort_numbers(numbers: list[float]) -> list[float]:
    """
    ## 선택정렬
    1. numbers 리스트를 arr로 복사
    2. arr에서 가장 작은 수를 찾아 0번째 위치로 이동
    3. arr[i:]로 범위를 줄여 단계 2번 반복
    """
    arr: list[float] = numbers.copy()
    n: int = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx: int = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    main()
