def main():
    try:
        num_list: list[float] = sorted(map(float, input().split()))
    except ValueError:
        print("Invalid input.")
        return
    print(f"Min: {num_list[0]}, Max: {num_list[-1]}")


if __name__ == "__main__":
    main()
