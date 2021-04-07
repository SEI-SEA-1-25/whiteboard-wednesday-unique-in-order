def unique_in_order(arr):
    result = []
    for i in range(len(arr)):
        current = arr[i]
        next_one = arr[i - 1]
        if current == next_one:
            i += 1
        else:
            result.append(arr[i])
    return result

print(unique_in_order('ABBCcAD'))

