def unique_in_order(str_or_arr):
    new_list = []
    for i in range(len(str_or_arr)):
        if str_or_arr[i] != str_or_arr[i + 1]:
            print(str_or_arr[i])
            new_list.append(str_or_arr[i])


unique_in_order('AAAABBBCCDAABBB')
