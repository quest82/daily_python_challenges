def main():
    sequence = input('Enter sequence: ')
    result = rev_comp(sequence)
    print(result)

def rev_comp(x):
    reversed = []
    for base in x:
        reversed.insert(0, base)

    for index, base in enumerate(reversed):
        if base == 'A':
            reversed[index] = 'T'
        elif base == 'T':
            reversed[index] = 'A'
        elif base == 'C':
            reversed[index] = 'G'
        elif base == 'G':
            reversed[index] = 'C'
    return "".join(reversed)

main()