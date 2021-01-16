num1 = 100
num2 = num1

lists1 = [ 1, 2, 3, 4, 5 ]
lists2 = lists1

print(num1 is num2)         # True
print(lists1 is lists2)     # True
num1 = 500
print(num1 is num2)         # False
print(num1)
print(num2)
print()

lists1[-1] = 5000
print(lists1)
print(lists2)

# 왜 10행은 False로 나오는가?
# -> num1이 기존의 객체 대신 500이라는 새로운 객체를 가리키기 때문에?
# -> 파이썬은 (흔히 기본 자료형으로 알려진 자료형들의)리터럴을 어떻게 관리하는지 알아볼 것
