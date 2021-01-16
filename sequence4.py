# 리스트 복사

lists1 = [ 1, 2, 3 ]
lists2 = lists1 # 얕은 복사가 진행된다. 즉, lists2는 lists1과 같은 객체를 가리킨다.
lists3 = lists1.copy() # lists1의 얕은 복사를 새로 생성하여 lists3이 가리킨다. 즉, lists3은 lists1과 다른 객체를 가리킨다.

# 참고: is와 not is, 그리고 ==
# is와 not is는 객체가 서로 같은지를 비교한다.
# ==는 객체의 값이 서로 같은지를 비교한다.
print(lists1 is lists2) # True
print(lists1 is lists3) # False
print()
print(lists1 == lists2) # True
print(lists1 == lists3) # True

lists1[0] = 100
lists2[1] = 200
lists3[2] = 300

print(lists1)
print(lists2)
print(lists3)
