def too_much_screen_time(hours):
    # For average of three
    start = 0
    stop = 3

    guage = True

    x, y, z = hours[start:stop]
    average = int(round((x + y + z)/3))
    while True:
        print(x, y, z, start, stop)
        if average < 8:
            start += 1
            stop +=1
            guage = False
        else:
            guage = True
            break

        if stop > 4 & average < 8:
            break
    return guage
    
   
    
print(too_much_screen_time([1, 2, 3, 4]))
    

#     for i in hours:
#         if i > 10:
#             return True

# def three_avg(hours):
#     loop_counter = 1
#     starter = 0
#     index = starter
#     three_total = 0
#     example = []

#     while True:
#         three_total += hours[index]
#         example.append(hours[index])
#         if loop_counter == 3:
#             avg = int(round(three_total / 3))
#             if avg >= 8:
#                 return True, example
#             else:
#                 starter += 1
#                 loop_counter = 1
#                 example = []


#         loop_counter +=1
#         index += 1
                

        



    