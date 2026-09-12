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
    def pure_gc(seq):
        total = 0
        for x in seq:
            if x == 'G' or x == 'C':
                total += 1
        return total

    sequence_amount = {}
    for index, sequence in enumerate(dictionary.values()):
        sequence_amount[index] = [len(sequence), pure_gc(list(sequence))]
    return sequence_amount

        

main()