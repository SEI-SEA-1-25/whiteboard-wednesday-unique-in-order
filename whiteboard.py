# def unique_in_order(arr):
#     stack = []

#     for i in arr:
#         if i not in stack:
#             stack.append(i)
#     return stack

def unique_in_order(iterable):
    result = []
    prev = None
    for element in iterable:
        if element != prev:
            result.append(element)
            prev = element
    return result


print(unique_in_order('AAAABBBCCDAABBB'))
