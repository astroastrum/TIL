import sys
sys.stdin = open("SWEA/input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    word = input()
    re_word = ''

    for char in word:
        re_word = char + re_word
    
    if word == re_word:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
    