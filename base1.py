# 진법
# int(str, base=10)
print(int('300'))
print(int('0b11111111', 2))
print(int('0o777', 8))
print(int('0xabc', 16))
print(bin(int('0xabcd', 16)))
print()

# format() 내장함수를 사용하면 숫자를 다른 진수의 문자열로 바꿀 때 접두어를 제외할 수 있다.
print(format(42, 'b')) # '101010'
print(format(42, 'o')) # '52'
print(format(42, 'x')) # '2a'
print(format(42, 'X')) # '2A'
print(format(42, 'd')) # '42'
print()

# #를 포함시키면 접두어를 포함시킬 수 있다.
print(format(42, '#b'))
print(format(42, '#o'))
print(format(42, '#x'))
print(format(42, '#X'))

# format 함수에 대한 자세한 내용은 파이썬 문서 참조
# https://docs.python.org/3/library/functions.html#format
# https://docs.python.org/3/library/string.html#formatspec
