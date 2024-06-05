def first_repeated_value(list):
    number_list = set()
    for value in list:
        if value in number_list:
            return value
        else:
            number_list.add(value)
    return None
    
print(first_repeated_value([1, 2, 3, 3, 4, 4]))  # This will print 3
