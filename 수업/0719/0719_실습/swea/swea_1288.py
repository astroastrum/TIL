import sys
sys.stdin = open("SWEA/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [0] * 10
    k = 1

    while 0 in data:
        num = str(N * k)
        for j in range(len(num)):
            data[int(num[j])] += 1
        k += 1
    
    print(f'#{test_case} {num}')