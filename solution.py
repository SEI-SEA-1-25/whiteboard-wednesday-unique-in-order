def unique_in_order(str_or_arr):
    new_list = []
    for i in range(len(str_or_arr)):
        j = i - 1
        if str_or_arr[j] != str_or_arr[j + 1]:
            new_list.append(str_or_arr[i])
    return(new_list)



unique_in_order([1,2,2,3,3])
