def mapping(lst, func):
    mapped_list = []

    for item in lst:
        mapped_list.append(func(item))

    return mapped_list

print(mapping([1, 2, 3, 4, 5], lambda x: x ** 2))
