def second_largest(arr):
    sing_arr = set(arr)
    new_arr = sorted(sing_arr)
    return new_arr[len(new_arr) - 2]

print(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]))