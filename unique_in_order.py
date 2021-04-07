def unique_in_order(arr):
    new_list = []
    # loop through each words
    for i in range(len(arr)):
        if(arr[i] == arr[i - 1]): 
           i += 1
        else:
            new_list.append(arr[i])
        
        
    return print(new_list)
        
    # compare the left to the right if its duplicated
    # store the value to the new list

unique_in_order('AAAABBBCCDAABBB') # == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         # == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       # == [1,2,3]