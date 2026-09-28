def tribonacci_sequence(start_sequence, length):
    final_arr = list(start_sequence)
    
    
    while len(final_arr) <= length:



        total = sum(final_arr[-3:])
        final_arr.append(total)








        


    return final_arr


tribonacci_sequence([1,2,3], 6)