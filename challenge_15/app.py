def is_mirror(str1, str2):
    str2 = str2.strip()
    array_2 = str2.split(' ')
    array_3 =[]
    for word in array_2:
        string = ''
        for letter in word:
            if letter.isalpha():
                string += letter
        array_3.insert(0, string)
        string = ''

    return array_3

print(is_mirror("Hello World", "!dlroW !olleH"))