def unique_in_order(value):
    temp = list(value)   #  == ['A','A','A','A', 'B', 'B', 'B', 'C', 'D', 'A', 'B', 'B', 'B']
    storage = []                          # 'A',           'B'  'C'  'D'  'A'  
    storage.append(temp[0])
    for i in range(1, len(temp)):
        if temp[i] != temp[i-1]:
            storage.append(temp[i])

    print(storage)
    return storage

unique_in_order('AAAABBBCCDAABBB') # == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         # == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       # == [1,2,3]


# function unique_in_order(value) {
#     let splitted = value.split('')
# }

# unique_in_order('AAAABBBCCDAABBB') # == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         # == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       # == [1,2,3]