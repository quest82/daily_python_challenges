def tribonacci_sequence(start_sequence, length):
    final_arr = list(start_sequence)
    
    while True:
        running_arr = start_sequence
        if len(final_arr) == 6:
                    break
        print("running array", running_arr)
        sum_of_three = sum(running_arr[:3])
        print(sum_of_three)
        running_arr.append(sum_of_three)
        final_arr.append(sum_of_three)
        del(running_arr[0])
        





        


    # return length


tribonacci_sequence([1,2,3], 6)