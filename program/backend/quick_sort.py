def quick_sort(sequence, start=0):
    if start == '':
        start = 0
    number_list = [x for x in sequence if isinstance(x, int)]
    alphabets_list = [x for x in sequence if not isinstance(x, int)]
    num = [x for x in alphabets_list if x.isnumeric()]
    alphabets_list = [ele for ele in alphabets_list if ele not in num]
    number_list += [int(x) for x in num]
    special_alphabets = []
    secondary_special_alphabets = []

    for item in alphabets_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(item.lower())[:len(str(start))] == str(start)[:]:
            special_alphabets.append(item)
        elif str(start)[:] in str(item):
            secondary_special_alphabets.append(item)
        elif str(start)[:] in str(item.lower()):
            secondary_special_alphabets.append(item)
    alphabets_list = [ele for ele in alphabets_list if ele not in special_alphabets + secondary_special_alphabets]

    length = len(number_list)
    if length <= 1:
        return special_alphabets + secondary_special_alphabets + alphabets_list + number_list
    else:
        pivot = number_list.pop()

    special = []
    item_greater = []
    item_lower = []

    for item in number_list:
        if str(item)[:len(str(start))] == str(start)[:]:
            special.append(item)
        elif item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)

    if str(pivot)[:len(str(start))] == str(start)[:]:
        return [pivot] + alphabets_list + quick_sort(item_lower) + quick_sort(item_greater)

    return sorted(special_alphabets) + sorted(secondary_special_alphabets) + quick_sort(special) + alphabets_list + quick_sort(item_lower) + [pivot] + quick_sort(item_greater)
