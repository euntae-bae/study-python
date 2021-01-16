# 리스트의 pop()과 remove() 메서드 비교, 그리고 reverse() 메서드

lists = [ 0, 1, 2, 3, 4, 4, 5, 4, 4, 6, 7 ]
print(lists)
print(lists.pop())      # 7
print(lists.pop(2))     # 2
print(lists.pop(-1))    # 6
print(lists)
lists.remove(4)
lists.remove(4)
print(lists)
lists.reverse()
print(lists)