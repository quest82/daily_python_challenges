c = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

nucleotides = {}

def main():
    while True:
        sequence = input('Enter your sequence: ')
        try:
            result = nuc_counter(sequence.strip())
        except ValueError:
            continue
        else:
            print(result)
            print(nucleotides)
            break

def nuc_counter(input):
    for base in input:
        if base not in 'AGCT':
            raise ValueError
        if base in nucleotides.keys():
            nucleotides[base] += 1 
        else:
            nucleotides[base] = 1
    return f"{nucleotides["A"]} {nucleotides["C"]} {nucleotides["G"]} {nucleotides["T"]}"

main()