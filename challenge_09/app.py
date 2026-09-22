def main():

    sequence_header = ''
    sequence_database = {}

    print('Enter your all sequences one by one below and press CTRL + D to get your result\n')

    while True: # Creates a loop for continous entry until CTRL + D is pressed
        try:
            line = input().strip() # Prompts user for their FASTA file. 
        except EOFError: 
            break  # Exits the loop once CTRL + D is pressed
        else:
            if not line: # If the entry is not an input, it skips
                continue
            if line.startswith('>'): # Reads each line for the FASTA header. If true, saves the header as a key in sequence_database
                sequence_header = line[1:].strip()
                sequence_database[sequence_header] = ''
            else:
                sequence_database[sequence_header] += line # Reads each line for bases. If true, concatenates it with previous value.
    result = get_gc_content(sequence_database)
    print(result)

def gc_content(seq = []): # Takes a sequence and returns the sum of its GC content
    total = 0
    for x in seq:
        if x == 'G' or x == 'C':
            total += 1
    return total

def get_gc_content(sequences):

    base_info = {} 
    for key, sequence in sequences.items(): # Creates a dictionary with the total no of bases and total sum of GC bases for each sequence
        base_info[key] = [len(sequence), gc_content(list(sequence))] 



    return 

        

main()