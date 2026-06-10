import random

randomNo = random.randint(1, 100)
print(randomNo)

guess = 0
count = 0

while guess != randomNo:
    guess = int(input('Choose a whole number between 1 and 100. 1 and 100 are options: '))
    if guess > randomNo:
        print('Too high, choose again')
        count += 1
    elif guess < randomNo:
        print('Too low, choose again')
        count += 1
    else:
        print('You\'re right')
        print(f'It took you {count} turns.')

