# sequence types: list, tuple, range
lists = [[]] * 3 # [[], [], []]
print(lists)
print(lists[0])
print(lists[1])
print(lists[2])

lists[0].append(3)
lists[0].append(4)
lists[0] = [5, 6, 7]
print(lists[0])
print(lists[1])
print(lists[2])
print(lists)
