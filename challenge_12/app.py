def too_much_screen_time(hours):
    if not hours:
        return "Function requires an array with at least one value"

    screen_time = False

    for i in hours: # If any day in the array is above 10, it returns True for too much screen time
        if i >= 10:
            screen_time = True
            return screen_time

    avg_of_seven = sum(hours) / len(hours) # If the avg screen time for the week is 6 or above, it returns True
    if avg_of_seven >= 6:
        screen_time = True 
        return screen_time


    while True:
        if len(hours) < 3:
            break

        array_of_threes = []
        for i in hours:
            if len(array_of_threes) < 3:
                array_of_threes.append(i)
        if (sum (array_of_threes) / len(array_of_threes)) < 8:
            screen_time = False
            del hours[0]

        else:
            screen_time = True
            break
    return screen_time

print(too_much_screen_time([1, 2, 3, 10, 2, 1, 0]))


            



