def main():
    # try:
    #     num_list: list[float] = sorted(map(float, input().split()))
    # except ValueError:
    #     print("Invalid input.")
    #     return
    # print(f"Min: {num_list[0]}, Max: {num_list[-1]}")

    while True:
        num_list: list[float] = [float(x) for x in input().split()]

        if num_list:
            break
        else:
            print("하나 이상의 숫자를 입력하세요.")

    min_num, max_num = get_min_max(num_list)
    print(f"Min: {min_num}, Max: {max_num}")


def get_min_max(arr: list[float]) -> tuple[float, float]:
    min_num, max_num = arr[0], arr[0]

    for num in arr:
        if max_num < num:
            max_num = num

        if min_num > num:
            min_num = num

    return min_num, max_num


if __name__ == "__main__":
    main()
