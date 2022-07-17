## 문제 01. 수 구분하기

 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.

```
Input
n = 267
```

```
n = 264 # 참
```

```
n = 14 # 거짓
```

### 코드

반복문

```python
num = int(input())
ans = '참' if (num%3==0) and (num%2==0) else '거짓'
print(ans)
```



## 02. 문제 02. 길이 구하기

문자열 word의 길이를 출력하는 코드를 각각 작성하시오. len() 함수를 바로 쓰기보다는 반복문을 활용하세요.

Input

``` python
word = 'happy!'
```

output

``` pytho
6
```



## 코드

```python
cnt = 0
for i in word:
  cnt += 1
print(cnt)
```



## 문제 03. 합 구하기

1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오. sum() 함수 사용 금지

Input

```python
n = 10
```

output

```python
55
```



### 코드

``` python
import sys

n=int(sys.stdin.readline())
answer=0

for i in range(1,n+1):
    answer+=i
print(answer)
```





## 문제 04. 곱 구하기

1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

Input

```python
n = 5
```

Output

``` python
120
```

1부터 n까지의 곱: (1~n)



### 코드

```python
a = 1
result = 1

for a in range(1,6):
    result *= a

n = 5
a = 1
result = 1

while a <= n :
    result *= a
    a += 1
print(result)
```



## 문제 05. 평균 구하기

주어진 숫자의 평균을 구하는 코드를 작성하시오. sum(), len()  함수 사용 금지

Input

```python
numbers = [3, 10, 20]
```

Output

``` python
11
```



### 코드

``` python
numbers = [3, 10, 20]
sum = 0
n = 0
for i in numbers:
    sum += i
    n += 1
avg = sum / n
print(int(avg))
```



## 문제 06. 최댓값 구하기

주어진 리스트 numbers에서 최댓값을 구하여 출력하시오. max() 함수 사용 금지

Input

````python
numbers = [0, 20, 100]


아래의 테스트 케이스로도 확인 해보세요.


numbers = [0, 20, 100, 50, -60, 50, 100] # 100
numbers = [0, 1, 0] # 1
numbers = [-10, -100, -30] # -10 
```
````

Output

```python
100
```



### 코드

```python
from asyncio.windows_events import INFINITE

numbers = [-10, -100, -30] # -10 
max = -INFINITE
for i in numbers:
    if i > max:
        max = i

print('max =', max)
```



## 문제 07. 최솟값 구하기

주어진 리스트 numbers에서 최솟값을 구하여 출력하시오. min() 함수 사용 금지

````python
Input


numbers = [0, 20, 100]
```

아래의 테스트 케이스로도 확인 해보세요.


numbers = [0, 20, 100, 50, -60, 50, 100] # -60
numbers = [0, 1, 0] # 0
numbers = [-10, -100, -30] # -100
```

Output
0
````



### 코드

``` python
numbers = [-10, -100, -30]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)
```



## 문제 08. 두 번째로 큰 수 구하기

주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오. max() 함수 사용 금지

````python
Input

```python
numbers = [0, 20, 100]
```

아래의 테스트 케이스로도 확인 해보세요.

```python
numbers = [0, 20, 100, 50, -60, 50, 100] # 50
numbers = [0, 1, 0] # 0
numbers = [-10, -100, -30] # -30
```

Output
20
````



### 코드

``` py
numbers = list(set(map(int,input().split())))
numbers.sort(reverse=True)
print(numbers[1])
```

