def is_mirror(str1, str2):
    str2 = str2.strip()
    array_2 = str2.split(' ')
    array_3 =[]
    for word in array_2:
        for letter in word:
            if letter.isalpha():
                array_3.insert(0, letter)

    return array_3

print(is_mirror("Hello World", "!dlroW !olleH"))