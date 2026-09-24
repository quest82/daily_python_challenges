def is_perfect_square(n):
    sqrt = int(n ** 0.5)
    print(sqrt)
    if sqrt ** 2 == n:
        return True
    else:
        return False

print(is_perfect_square(6))