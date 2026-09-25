def is_mirror(str1, str2):
    str2 = str2.strip()
    array_2 = str2.split(' ')
    array_3 =[]
    for word in array_2:
        word_array = []
        for letter in word:
            if letter.isalpha():
                word_array.insert(0, letter)
        array_3.insert(0, word_array)
        word_array = []

    return array_3

print(is_mirror("Hello World", "!dlroW !olleH"))