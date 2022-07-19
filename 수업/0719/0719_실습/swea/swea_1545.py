import sys
sys.stdin = open("SWEA/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    print(T, end=' ')
    T -= 1
print(0)