def too_much_screen_time(hours):
    if not hours:
        return "Function requires an array with at least one value"

    for i in hours: # If any day in the array is above 10, it returns True for too much screen time
        if i > 10:
            return True

    avg_of_seven = sum(hours) / len(hours) # If the avg screen time for the week is 6 or above, it returns True
    if avg_of_seven >= 6:
        return True 

    # array_of_threes = []
    # for i in hours:
    #     if 



