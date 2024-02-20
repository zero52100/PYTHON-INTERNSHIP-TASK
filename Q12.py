def flat(lis):
    flatList = []
    for element in lis:
        if type(element) is list:
            flatList.extend(flat(element))
        else:
            flatList.append(element)
    return flatList

lis = [1, [2, 3], [4, [5, 6]]]
print('List:', lis)
print('List:', flat(lis))
