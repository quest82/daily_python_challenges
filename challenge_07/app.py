def main():
    sequence = input("Enter DNA sequence: ")
    result = transcriber(sequence)
    print(result)

def transcriber(x):
    base_list = list(x)
    for index, base in enumerate(base_list):
        if base == 'T':
            base_list[index] = 'U'
    return "".join(base_list)


main()