def second_largest(arr):
    new_arr = sorted(arr)

    return new_arr[len(new_arr) - 2]

print(second_largest([20, 139, 94, 67, 31]))