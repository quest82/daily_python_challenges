def too_much_screen_time(hours):

    for i in hours:
        if i > 10:
            return True

def three_avg(hours):
    loop_counter = 1
    starter = 0
    index = starter
    three_total = 0
    example = []

    while True:
        three_total += hours[index]
        example.append(hours[index])
        if loop_counter == 3:
            avg = int(round(three_total / 3))
            if avg >= 8:
                return True, example
            else:
                starter += 1
                loop_counter = 1
                example = []


        loop_counter +=1
        index += 1
                

        
print(three_avg([1, 2, 3, 4, 5, 6, 7]))


    