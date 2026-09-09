def main():
    data = input("Enter your sequences")
    print(get_gc_content(data))

def get_gc_content(x):
    raw_sequences = x.strip()
    separated_sequences = [single_seq.strip() for single_seq in raw_sequences.split('>') if single_seq.strip()]


main()