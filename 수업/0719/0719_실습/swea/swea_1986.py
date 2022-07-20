import sys
sys.stdin = open("SWEA/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            result += i
        else:
            result -= i
    print(f'#{test_case} {result}')