def reverse_sentence(x):
    
    reversed_array = []
    for word in x.split(" "):
        reversed_array.insert(0, word)

    # sentence = " ".join(reversed_array)
    return reversed_array


print(reverse_sentence("npm  install   apt    sudo"))