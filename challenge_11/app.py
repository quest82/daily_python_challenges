def main():
    print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))

def array_diff(arr1, arr2):
    set_1 = set(arr1)
    set_2 = set(arr2)
    result = set_1 ^ set_2

    return sorted(list(result))

main()