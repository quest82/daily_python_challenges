def main():

    sequence_header = ''
    sequence_database = {}

    print('Enter your all sequences one by one below and press CTRL + D to get your result\n')

    while True:
        try:
            line = input().strip()
        except EOFError: 
            break 
        else:
            if not line:
                continue
            if line.startswith('>'):
                sequence_header = line[1:].strip()
                sequence_database[sequence_header] = ''
            else:
                sequence_database[sequence_header] += line
    result = get_gc_content(sequence_database)
    print(result)
def get_gc_content(dictionary):
    sequence_amount = []
    for sequence in dictionary.values():
        gc_total = 0
        for base in sequence:
            if base == 'G' or base == 'C':
                gc_total+=1
            sequence_amount.append((len(sequence), gc_total))


    return sequence_amount    


main()