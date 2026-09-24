def too_much_screen_time(hours):
    if not hours:
        return "Function requires an array with at least one value"

    for i in hours: # If any day in the array is above 10, it returns True for too much screen time
        if i > 10:
            return True

