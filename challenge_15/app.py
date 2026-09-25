def is_mirror(str1, str2):
    def only_letters(s):
        return ''.join(c for c in s.strip() if c.isalpha())
    
    str2 = str2.strip()
    array_2 = str2.split()
    array_3 =[]
    for word in array_2:
        word_array = []

        for letter in word:
            if letter.isalpha():
                word_array.insert(0, letter)

        part_result = ''.join(word_array)
        array_3.insert(0, part_result)


    return only_letters(str1) == ''.join(array_3)

print(is_mirror("abc def", "cba fed"))