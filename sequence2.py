# append()와 extend() 메서드의 차이점을 비교한다.
# s.append(x): s[len(s):len(s)] = [x] 와 동일, 원소를 리스트에 덧붙인다. s += [x] 와도 동일한 연산이다.  
# s.extend(t): s[len(s):len(s)] = t 와 동일, 리스트를 리스트에 덧붙인다. s += t 와도 동일한 연산이다.  

# sequence types: list, tuple, range
lists = []
print(len(lists))
print(lists)
print(lists[0:0])

print()
lists[0:0] = [1] # lists[0:0] = 1 은 에러 발생
lists += [3]
lists[len(lists):len(lists)] = [5]
lists[len(lists):len(lists)] = [7]
lists.append(9)
lists.append(11)
lists.append([13])
lists.append([15])
lists.extend([17])
lists.extend([19])
lists.extend([21, 23, 25])
lists.append([27, 29])
print(lists)
print()

for i in lists:
    print(i)
print()

# print() 함수의 인자
# sep: 구분자
# end: 마지막에 출력
