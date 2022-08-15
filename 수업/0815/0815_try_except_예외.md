## try~except 특정 예외

```python
import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.7)
    except KeyboardInterrupt:
        print('무한 반복 종료')
        
while True가 실행되면 0.7초 동안 멈추고 다시 print와 count를 돌게됩니다. 그러나 Ctrl + C를 입력하면 except KeyboardInterrupt로 넘어가 '무한 반복 종료'를 출력하게 됩니다.
```

