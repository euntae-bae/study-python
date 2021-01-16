- 파이썬의 모든 데이터는 객체다. C, C++, Java처럼 기본자료형으로 구성되어 있지 않고, 모두 클래스 객체라는 것이다. 그러므로 리터럴이 메서드를 호출하는 것이 가능하다. (이 점은 C#과 마찬가지다.)
- 파이썬의 변수는 힙 영역에 동적할당된 객체의 참조를 가리킨다. 따라서 다음 코드는 얕은 복사를 수행한다.
  
  
## 순서열
- 파이썬의 순서열(sequence type): list, tuple, range (+ binary data, text strings)
- 순서열에서 +는 접합(concatenation), *는 반복(repetition) 연산이다.
  
```python
x in s # x가 s에 포함되어 있으면 True, 아니면 False
x not in s
s + t
s * n 또는 n * s
s[i]
s[i:j]
s[i:j:k] # k step
len(s)
min(s)
max(s)
s.index(x[, i[, j]]) # s에서 x가 처음 등장하는 인덱스 (또는 i 다음부터 j 이전까지의 범위에서)
s.count(x)
```
  
### Immutable Sequence Types
- `class tuple([iterable])`
- `class range(stop)`
- `class range(start, stop[, step])`

### Mutable Sequence Types
```python
s[i] = x
s[i:j] = t
del s[i:j]
s[i:j:k] = t
del s[i:j:k]
s.append(x) # 요소 x를 s에 덧붙인다. s[len(s):len(s)] = [x] 와 동일
s.clear() # del s[:]와 동일
s.copy  # s의 얕은 복사를 생성한다. s[:]와 동일
s.extend(t) 또는 s += t # 리스트 t를 s에 덧붙인다. s[len(s):len(s)] = t 와 동일
s *= n
s.insert(i, x) # s[i:i] = [x] 와 동일
s.pop([i]) # [i]는 리스트를 의미하는 게 아니라, 옵션을 의미한다. s.pop()은 맨 마지막 원소를 뽑아낸다. 즉, s.pop(-1)과 동일한 연산을 수행한다.
s.remove(x) # 요소 x와 동일한 값의 첫 번째 원소를 제거한다.
s.reverse()
```

* 리스트와 튜플은 모두 순서열에 속한다. 따라서 리스트에도 index나 count 메서드를 사용할 수 있다.  
