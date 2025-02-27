def is_reoccuring(items):
    sequence_numbers = []
    for index, item in enumerate(items):
        for number in sequence_numbers:
            if item == number and items[index - 1] != item:
                return True
        if index == 0:
            sequence_numbers.append(item)
            continue
        elif item not in sequence_numbers:
            sequence_numbers.append(item)   
    return False