def main():
    sequence = input('Enter sequence: ')
    result = rev_comp(sequence)
    print(result)

def rev_comp(x):
    reversed = []
    for base in x:
        reversed.insert(0, base)

    reverse_complement = reversed

    for index, base in enumerate(reverse_complement):
        if base == 'A':
            reverse_complement[index] = 'T'
        elif base == 'T':
            reverse_complement[index] = 'A'
        elif base == 'C':
            reverse_complement[index] = 'G'
        elif base == 'G':
            reverse_complement[index] = 'C'
    return reverse_complement

main()