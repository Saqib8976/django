if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = sorted(arr, reverse=True)

    runner_up_arr = None
    for score in sorted_arr:
        if score < sorted_arr[0]:
            runner_up_arr = score
            break

    print(runner_up_arr)
